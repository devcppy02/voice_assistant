# -*- coding: utf-8 -*-

import subprocess
import os.path
from playsound import playsound
import speech_recognition as sr
import gtts
import keyboard
import wikipedia
import webbrowser
from pathlib import Path
from colorama import init
from colorama import Fore
import re
import requests
from bs4 import BeautifulSoup


init()

#save list
caa = []


wikipedia.set_lang('ru')

listening = gtts.gTTS('слушаю', lang='ru')
listening.save('listening.mp3')

not_understand_for_test = gtts.gTTS('команда не опознана, пожалуйста повторите', lang='ru')
not_understand_for_test.save('not_understand_for_test.mp3')

not_understand = gtts.gTTS('команда не опознана, пожалуйста повторите или добавте ее', lang='ru')
not_understand.save('not_understand.mp3')

start = gtts.gTTS('запускаю', lang='ru')
start.save('start.mp3')

openn = gtts.gTTS('открываю', lang='ru')
openn.save('open.mp3')

on = gtts.gTTS('включаю', lang='ru')
on.save('on.mp3')

start_clicker = gtts.gTTS('кликер включится через 5 секунд', lang='ru')
start_clicker.save('start_clicker.mp3')

stop_clicker = gtts.gTTS('кликер остановлен', lang='ru')
stop_clicker.save('stop_clicker.mp3')



def test_audio_recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source)
        playsound('listening.mp3')
        print('слушаю...')
        audio = r.listen(source)
    try:
        print("распознавание...")
        global test_text
        test_text = r.recognize_google(audio, language='ru-RU')
    except:
        print('ошибка')
        playsound('not_understand_for_test.mp3')
        test_audio_recognize()
    return test_text.lower()

print(Fore.CYAN + 'Добро пожаловать в VoiceAssistant',Fore.RESET + '\n=================================',Fore.MAGENTA + '\nосновные команды:\n"открой ..." - открывает сайт\nнайди (что такое/кто такой/кто такая/кто такие) ..." - находит вопрос в википедии\n',Fore.GREEN + '\nесли вы запустили VoiceAssistant первый раз вам нужно добавить команды чтобы он работал')
print(Fore.RESET + '=======================================================================================================\n/ для того чтобы сказать команду нажмите ctrl+o \    / для того чтобы добавить команду нажмите ctrl+i \\\n=======================================================================================================')

def all_program():
    if 'voice_assist_caa.txt' in os.listdir(os.getcwd()):
        path = Path('voice_assist_caa.txt')
        caas = path.read_text()
        new_caas = re.sub(',{2,}', ',', caas)
        new_caas = new_caas.lstrip(',').rstrip(',')
        caa = new_caas.split(',')
    else:
        my_file = open("voice_assist_caa.txt", "w", encoding='utf-8')
        my_file.close()

    if keyboard.is_pressed('ctrl+i'):
        print('Введите что нужно добавить:\nсайт - с\nприложение - п')
        what_add = input()
        def add():
            if 'с' in what_add:
                print('произнесите название сайта')
                name = test_audio_recognize()
                print(name)
                print('Введите "д" - если название записалось верно, "н" - если неверно')
                yn = input()
                if yn == 'д':
                    name = 'открой '+name
                    caa.append(name)
                    caaf = open('voice_assist_caa.txt', 'w')
                    for element in caa:
                        caaf.write(element)
                        caaf.write(',')
                    caaf.close()
                    print('отлично! теперь введите ссылку на этот сайт\n')
                    link = input()
                    caa.append(link)
                    caaf = open('voice_assist_caa.txt', 'w')
                    for element in caa:
                        caaf.write(element)
                        caaf.write(',')
                    caaf.close()
                    print('команда открытия этого сайта успешно добавлена\nтеперь вы можете открывать его используя VoiceAssistant')
                    print(Fore.RESET + '=======================================================================================================\n/ для того чтобы сказать команду нажмите ctrl+o \    / для того чтобы добавить команду нажмите ctrl+i \\\n=======================================================================================================')
                    all_program()
                elif yn == 'н':
                    add()

            elif 'п' in what_add:
                print('произнесите название приложения')
                name = test_audio_recognize()
                print(name)
                print('Введите "д" - если название записалось верно, "н" - если неверно')
                yn = input()
                if yn == 'д':
                    name = 'запусти '+name
                    caa.append(name)
                    caaf = open('voice_assist_caa.txt', 'w')
                    for element in caa:
                        caaf.write(element)
                        caaf.write(',')
                    caaf.close()
                    print('отлично! теперь введите расположение этого приложения на вашем комрьютере\n')
                    link = input()
                    caa.append(link)
                    caaf = open('voice_assist_caa.txt', 'w')
                    for element in caa:
                        caaf.write(element)
                        caaf.write(',')
                    caaf.close()
                    print('команда запуска этого приложения успешно добавлена\nтеперь вы можете запускать его используя VoiceAssistant')
                    print(Fore.RESET + '=======================================================================================================\n/ для того чтобы сказать команду нажмите ctrl+o \    / для того чтобы добавить команду нажмите ctrl+i \\\n=======================================================================================================')
                    all_program()
                elif yn == 'н':
                    add()

            else:
                print(Fore.RED + 'ошибка',Fore.RESET)
                print(Fore.RESET + '=======================================================================================================\n/ для того чтобы сказать команду нажмите ctrl+o \    / для того чтобы добавить команду нажмите ctrl+i \\\n=======================================================================================================')
                all_program()
        add()
    if keyboard.is_pressed('ctrl+o'):
        def get_audio():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                playsound('listening.mp3')
                print('слушаю...')
                audio = r.listen(source)
            try:
                print("распознавание...")
                global text
                text = r.recognize_google(audio, language='ru-RU')
            except:
                print('ошибка')
                playsound('not_understand.mp3')
                print(Fore.RESET + '=======================================================================================================\n/ для того чтобы сказать команду нажмите ctrl+o \    / для того чтобы добавить команду нажмите ctrl+i \\\n=======================================================================================================')
                all_program()
            return text.lower()

        text = get_audio()
        print(text)
        caa.append('stop')

        for i in range(len(caa)):
#site
            if 'открой' in text and text == caa[i]:
                playsound('open.mp3')
                webbrowser.open(caa[i+1])
                print(Fore.RESET + '=======================================================================================================\n/ для того чтобы сказать команду нажмите ctrl+o \    / для того чтобы добавить команду нажмите ctrl+i \\\n=======================================================================================================')
                all_program()
                break
#app
            elif 'запусти' in text and text == caa[i]:
                playsound('start.mp3')
                subprocess.call(caa[i+1])
                print(Fore.RESET + '=======================================================================================================\n/ для того чтобы сказать команду нажмите ctrl+o \    / для того чтобы добавить команду нажмите ctrl+i \\\n=======================================================================================================')
                all_program()
                break
#wiki
            elif text.count('найди что такое') > 0:
                wikires = wikipedia.summary(text.replace('найди что такое', ''))
                inf = gtts.gTTS(wikires, lang='ru')
                inf.save('inf.mp3')
                print(wikires)
                playsound('inf.mp3')
                print(Fore.RESET + '=======================================================================================================\n/ для того чтобы сказать команду нажмите ctrl+o \    / для того чтобы добавить команду нажмите ctrl+i \\\n=======================================================================================================')
                all_program()
                break
            elif text.count('найди кто такой') > 0:
                wikires = wikipedia.summary(text.replace('найди кто такой', ''))
                inf = gtts.gTTS(wikires, lang='ru')
                inf.save('inf.mp3')
                print(wikires)
                playsound('inf.mp3')
                print(Fore.RESET + '=======================================================================================================\n/ для того чтобы сказать команду нажмите ctrl+o \    / для того чтобы добавить команду нажмите ctrl+i \\\n=======================================================================================================')
                all_program()
                break
            elif text.count('найди кто такая') > 0:
                wikires = wikipedia.summary(text.replace('найди кто такая', ''))
                inf = gtts.gTTS(wikires, lang='ru')
                inf.save('inf.mp3')
                print(wikires)
                playsound('inf.mp3')
                print(Fore.RESET + '=======================================================================================================\n/ для того чтобы сказать команду нажмите ctrl+o \    / для того чтобы добавить команду нажмите ctrl+i \\\n=======================================================================================================')
                all_program()
                break
            elif text.count('найди кто такие') > 0:
                wikires = wikipedia.summary(text.replace('найди кто такие', ''))
                inf = gtts.gTTS(wikires, lang='ru')
                inf.save('inf.mp3')
                print(wikires)
                playsound('inf.mp3')
                print(Fore.RESET + '=======================================================================================================\n/ для того чтобы сказать команду нажмите ctrl+o \    / для того чтобы добавить команду нажмите ctrl+i \\\n=======================================================================================================')
                all_program()
                break
                
#weather
            elif text.count('сколько градусов') > 0:
                url = 'https://yandex.ru/'
                response = requests.get(url)
                bs = BeautifulSoup(response.text, 'html.parser')
                temp = bs.find('div', class_ = 'weather__temp')
                temp = str(temp)
                temp = temp[27:-7]
                inf = gtts.gTTS(temp, lang='ru')
                inf.save('inf.mp3')
                print(temp)
                playsound('inf.mp3')
                print(Fore.RESET + '=======================================================================================================\n/ для того чтобы сказать команду нажмите ctrl+o \    / для того чтобы добавить команду нажмите ctrl+i \\\n=======================================================================================================')
                all_program()
                break
            
            elif caa[i] == 'stop':
                caa.remove('stop')
                playsound('not_understand.mp3')
                print(Fore.RESET + '=======================================================================================================\n/ для того чтобы сказать команду нажмите ctrl+o \    / для того чтобы добавить команду нажмите ctrl+i \\\n=======================================================================================================')
                all_program()
                break
            else:
                continue

while True:
    all_program()
