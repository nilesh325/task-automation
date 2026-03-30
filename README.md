# 🤖 Jarvis — Voice Assistant in Python

Jarvis is a simple **AI Voice Assistant** built using Python that can listen to your voice commands and perform tasks like searching Wikipedia, opening websites, and telling the current time.

---

## 🚀 Features

* 🎙️ Voice recognition using microphone
* 🗣️ Text-to-speech response system
* 🌐 Open popular websites (YouTube, Google)
* 📚 Fetch information from Wikipedia
* ⏰ Tell current system time
* 👋 Smart greeting based on time of day

---

## 🛠️ Tech Stack

* Python
* `pyttsx3` → Text-to-Speech
* `speech_recognition` → Voice input
* `wikipedia` → Information retrieval
* `webbrowser` → Open websites

---

## 📂 Project Structure

```id="d9sj3k"
jarvis-voice-assistant/
 ┣ main.py
 ┣ README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```id="k3n91d"
git clone https://github.com/your-username/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

### 2. Install dependencies

```id="m2k8s0"
pip install pyttsx3 SpeechRecognition wikipedia pyaudio
```

⚠️ Note:
If `pyaudio` installation fails, install it using:

```id="z8x1qv"
pip install pipwin
pipwin install pyaudio
```

---

## ▶️ How to Run

```id="p0s8jd"
python main.py
```

---

## 🎯 How It Works

1. Jarvis greets the user based on the time of day
2. Listens to voice commands through the microphone
3. Converts speech to text using Google Speech Recognition
4. Processes the command and performs actions:

   * Searches Wikipedia
   * Opens websites
   * Tells the current time
5. Responds using text-to-speech

---

## 🧠 Supported Commands

* "Search Wikipedia for Python"
* "Open YouTube"
* "Open Google"
* "What is the time"

---

## 🔮 Future Improvements

* Add more commands (weather, news, apps)
* Integrate AI models (ChatGPT / LLMs)
* Add GUI interface
* Add wake word detection ("Hey Jarvis")
* Multi-language support

---

## 📌 Limitations

* Requires internet for speech recognition and Wikipedia
* Background noise may affect accuracy
* Works best with clear voice input

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* Python community
* Open-source libraries used in this project

---

⭐ If you like this project, consider giving it a star on GitHub!

