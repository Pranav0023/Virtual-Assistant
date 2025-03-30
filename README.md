# Panther Virtual Assistant 🐆🎙️

## Overview
Panther is a Python-based voice-controlled virtual assistant designed to simplify tasks and provide entertainment. 
It recognizes voice commands, performs actions like playing music, telling the time, cracking jokes, opening websites, and more. With a fun personality and an interactive experience, Panther is a great starting point for AI-driven automation projects.

## Features
- 🎤 **Voice Recognition:** Uses speech recognition to interpret voice commands.
- 🎵 **Play Songs:** Opens YouTube and plays requested songs.
- ⏰ **Tell Time:** Announces the current time when asked.
- 🤣 **Crack Jokes:** Tells random jokes for entertainment.
- 🌐 **Open Websites:** Opens any website specified by the user.
- 😆 **Personality:** Engages in casual conversation (Try asking if it's single!).
- 👋 **Exit on Command:** Says goodbye and shuts down when the user says "bye."
- ⏳ **Auto-Exit:** Closes automatically if no command is detected for a period of time.

### Running Panther
To launch the assistant, run the script:
```bash
python panther.py
```

## How It Works
1. Panther listens for voice input using the **speechrecognition** library.
2. The command is processed and mapped to a predefined function.
3. If a valid command is detected, Panther executes the corresponding task.
4. If the user says "bye," Panther says a farewell message and exits.
5. If no command is received within a timeout period, Panther exits automatically.

## Commands List
Here are some example commands Panther understands:
- **"Play [song name] on YouTube"** – Opens YouTube and plays the song.
- **"What time is it?"** – Tells the current time.
- **"Tell me a joke"** – Responds with a random joke.
- **"Open [website name]"** – Opens the specified website in the browser.
- **"Are you single?"** – Responds with a fun answer.
- **"Bye"** – Exits the program.

## Future Enhancements 🚀
Planned updates for Panther include:
- AI-powered responses using NLP for more natural conversations.
- Home automation integration to control smart devices.
- Customizable voice selection and personality settings.
- Context-aware conversations with memory storage.
- Multi-language support for a broader user base.

## Troubleshooting
### Common Issues & Fixes
**1. No microphone detected:**
   - Ensure your microphone is properly connected and enabled.
   - Check your system’s sound settings.

**2. "ModuleNotFoundError: No module named 'pyaudio'":**
   - On Windows, try installing PyAudio with:
     ```bash
     pip install pipwin
     pipwin install pyaudio
     ```
   - On macOS, use:
     ```bash
     brew install portaudio
     pip install pyaudio
     ```

**3. Speech recognition not working:**
   - Ensure you are speaking clearly into the microphone.
   - Try increasing the microphone sensitivity in system settings.

Happy coding! 🚀
