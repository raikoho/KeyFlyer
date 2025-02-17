# KeyFlyer
![KeyFlyer](KeyFlyer.png)
> *"In the age of information, the greatest weapon is not a sword or a gun, but the keystroke. Vigilance in the digital realm is the key to both freedom and security." – Unknown*

## 🕵️‍♂️Overview

**KeyFlyer** 2-component script and keylogger written in Python that captures keystrokes, including special keys and mouse clicks with their coordinates. The program allows for seamless logging of all user inputs and provides an additional utility for converting the logged keystrokes to different keyboard layouts.

## ✨Features

- Logs all keystrokes, including special keys and key combinations.
- Logs mouse clicks (right, left) and their coordinates.
- Start and stop keylogger with custom key combinations.
- Seamlessly convert logged keystrokes to different keyboard layouts (English, Russian, Ukrainian, Danish).
- Organized session logs with timestamps for easy analysis. The files will be stored in the main folder along with the script.

## 🛠️Installation

### Installation for Linux:

```bash
git clone https://github.com/raikoho/KeyFlyer.git
cd KeyFlyer
python KeyFlyer.py
or
python KeyFlyerConverter.py
```
## Installation for Windows:

Just use windows terminal to execute .py files. Or build .py files by any compilator or write me - i will send arlready builded files to you.

## 🧩Dependencies
To install the necessary dependencies, use pip:

```bash
pip install keyboard mouse
```

## 📋Example
### To use the keylogger:

1. Run the KeyFlyer (keylogger) script.
2. Stop logging by pressing alt + space.
3. Resume recording and logging by pressing ctrl + space.
   
### To convert the logged keystrokes:

  - Run the keyboard layout converter script - KeyFlyerConverter.
  - Follow the prompts to specify the input log file, output log file, source language, and target language.
  - The translated log file will be generated at the specified output path.

## 🤝Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or additions.

## 📄License
This project is licensed under the MIT License. See the LICENSE file for details.

## ⚠️Disclaimer
KeyFlyer is intended for ethical use only. Ensure that you have proper authorization before deploying this tool on any system. Unauthorized use of keylogging software is illegal and unethical.

