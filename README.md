# PyDejavuBot
[![CodeFactor](https://www.codefactor.io/repository/github/zhymabekroman/pydejavubot/badge)](https://www.codefactor.io/repository/github/zhymabekroman/pydejavubot)

|**English verssion** | [Русская версия](https://github.com/ZhymabekRoman/PyDejavuBot/blob/master/README-RU.md) |

**PyDejavuBot** (a.k.a. **LenDejavuBot**) - Free Open Source Telegram Bot, designed for recognize a melody. The main focus of the bot is stability, speed, and audio recognitions quality. It can be considered an analogue of Shazam, but compared to Shazam and other similar audio recognition services, PyDejavuBot does not have its own centralized database with fingerprint, the user himself adds audio recordings and indicates the name. Audio recognition system based on Landmark audio fingerprinting system.

## Destination
In musical institutions, in addition to theory and practice, and the study of composers, you additionally need to know by heart all the famous works of the composer, as well as how they sound. And to check in what condition the student knows the works by heart, teachers periodically arrange music quizzes. For this, teachers pre-quiz give students audio recordings that will be on the quiz. In principle, learning 5-10 works is not difficult. But it happens that this list reaches up to 40 (!) Works, which is not so simple, and you need to know not only the name of the work, but also the composer, what tonality and exactly where (what action, part or act). This is still the beginning that I voiced, some teachers, for example, do not first put a record, but let's say from the middle. Here Shazam, with its base work will not help, you need to create your own flexible base with works.

Bot operation principle:
1 > You upload to bot the audio recording that the teacher gave you to prepare for the quiz
2 > During a quiz, you go to a bot, turn on Quiz Mode, and send an audio message with a quiz and bot give you the title of the recording

Shazam is not particularly useful here, since it sometimes does not correctly recognize the audio recording itself. If even correctly recognized, then the information of the recognized record is not enough for the teacher.

## Features
- [x] Fully asynchronous Telegram Bot written in Python 3 with aiogram.
- [x] High speed and accuracy recognition

## Installation
1) In Ubuntu or Debian based distribution install ffmpeg, python3, pip3 and git via apt:
```
sudo apt install python3 python3-pip ffmpeg git -y
```
2) Clone this repository :
```
git clone https://github.com/ZhymabekRoman/PyDejavuBot
```
3) Install all python depends, that required for bot operation, via pip3: 
```
cd PyDejavuBot/
pip3 install -r requirements.txt
```

4) Initialize bot configurations. This should only be done at the very first start of the bot:
```
cd src/
python3 first_start.py
```
and answer to the script's questions.

5) On some Debian distributions, you may need to add the ~/.local/bin folder to PATH variable, since pip installs some libraries there:
```
echo export PATH=~/.local/bin:$PATH >> ~/.bashrc
```

6) Launching the bot:
```
python3 main.py
```

## Used libraries and third-party programs
[audfprint](https://github.com/dpwe/audfprint) - Python version of Matlab implementation of Landmark audio recognition system. This is the heart of the bot itself. A huge thank to Dan Ellis, Columbia University, and Google.

[aiogram](https://github.com/aiogram/aiogram) - a pretty simple and fully asynchronous framework for Telegram Bot API written in Python 3.7 with asyncio and aiohttp.

[ffmpeg](https://ffmpeg.org/) - third-party super-powerful program for working with audio and video. Used for converting and working with audio hashes.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update the tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

_*WIP - Working in process_
