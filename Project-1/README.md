# 🌍 Language Translation Tool

A simple web-based tool that translates text between multiple languages, with text-to-speech and copy support.

## Features

- Enter any text and select source & target languages
- Translate instantly using Google Translate's public API
- Swap source/target languages with one click
- Copy translated text to clipboard
- Listen to the translated text using text-to-speech

## Technologies Used

- **HTML** – page structure
- **CSS** – styling and layout
- **JavaScript** – logic, API calls, speech synthesis
- **Google Translate API (unofficial endpoint)** – for translation
- **Web Speech API** (`SpeechSynthesis`) – for text-to-speech, built into the browser

## How It Works

1. User types text in the input box and selects source/target language.
2. On clicking **Translate**, the app sends the text to Google Translate's API.
3. The API returns the translated text, which is displayed on screen.
4. User can copy the result or have it read aloud using the Speak button.

## Project Structure

```
translation-tool/
│
├── index.html      # Page structure (input box, dropdowns, buttons)
├── style.css       # Styling
└── script.js       # Translation logic, API calls, speech synthesis
```

## How to Run

1. Download/clone the project folder.
2. Open `index.html` in any browser
   (or use VS Code's "Live Server" extension for best results).
3. Type text, select languages, click **Translate**.

## Known Limitations

- Requires an internet connection (API-based translation).
- Text-to-speech depends on voices installed/available in the user's browser/OS —
  some languages may need their voice pack installed manually
  (Windows: Settings → Time & Language → Speech → Add a language).

## Future Improvements

- Auto-detect source language
- Translation history
- Support for voice input (speech-to-text)
