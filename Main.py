import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import sys

# Initialize recognizer & TTS engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set UK English Voice
voices = engine.getProperty('voices')
uk_voice = next((voice.id for voice in voices if "english" in voice.name.lower() and "gb" in voice.id.lower()), None)
if uk_voice:
    engine.setProperty('voice', uk_voice)

last_response = ""  # Avoid repeating same response


def talk(text):
    """Speaks text only if it's different from the last response."""
    global last_response
    if text != last_response:
        engine.say(text)
        engine.runAndWait()
        last_response = text


def take_command():
    """Listens for a voice command and returns the recognized text. If no command, exits."""
    command = ""
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=0.2)
            print('Listening... Speak now!')
            voice = listener.listen(source, timeout=3, phrase_time_limit=5)
            command = listener.recognize_google(voice, language="en-GB").lower()
            command = command.removeprefix('panther').strip()
            print(f"Command detected: {command}")
    except:
        print("No command detected. Exiting...")
        sys.exit()  # Exit the program if no command is given
    return command


def open_website(cmd):
    """Opens the specified website."""
    cmd = cmd.replace('open', '').strip()
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "facebook": "https://www.facebook.com",
        "linkedin": "https://www.linkedin.com"
    }

    for site in websites:
        if site in cmd:
            talk(f"Opening {site}.")
            webbrowser.open(websites[site])
            return

    talk("Website not recognized. Please try again.")
    print(f"Website {cmd} is not recognized.")


# Dictionary for direct command mapping
commands = {
    'play': lambda cmd: (
        talk(f"Playing {cmd.replace('play', '').strip()}"),
        pywhatkit.playonyt(cmd.replace('play', '').strip())
    ),
    'time': lambda _: (
    current_time := datetime.datetime.now().strftime('%I:%M %p'),
    print(f"The current time is {current_time}"),
    talk(f"The current time is {current_time}")
    ),

    'are you single': lambda _: (
        print("Sorry, I have a girlfriend"),
        talk("Sorry, I have a girlfriend.")
    ),
    'joke': lambda _: (
    joke := pyjokes.get_joke(),  # Store joke in a variable
    print(joke),
    talk(joke)
    ),
    'bye': lambda _:(
        print("Goodbye! Have a great day!"),
        (talk("Goodbye! Have a great day!"), sys.exit())
    ),
    'open': open_website
}


def run_panther():
    """Processes the user's command using dictionary mapping."""
    command = take_command()
    for key in commands:
        if key in command:
            commands[key](command)
            return

    talk("Please say the command again.")


# Main loop
while True:
    run_panther()
