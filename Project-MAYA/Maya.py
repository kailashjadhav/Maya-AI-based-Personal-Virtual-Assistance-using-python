from google import google
import boto3
import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random

#Defining Speech Recognition.
speech = sr.Recognizer()

#Defining all the hot words to be compaired with the voice input.
greeting_dict = {'hello':'hello','hi':'hi','hey':'hey'}
open_launch_dict = {'open':'open','launch':'launch'}
social_media_dict = {'facebook':'https://www.facebook.com/','twitter':'https://twitter.com/?lang=en','google':'https://www.google.com/','youtube':'https://www.youtube.com/'}
google_search_dict = {'why':'why','what':'what','who':'who','when':'when','which':'which','how':'how','where':'where'}
shutdown_mode_dict = {'shutdown':'shutdown','switchoff':'switchoff','turnoff':'turnoff','poweroff':'poweroff'}
abort_shutdown_dict = {'abort':'abort','stop':'stop','cancel':'cancel'}
reboot_dict = {'reboot':'reboot','restart':'restart'}
goodbye_dict = {'buy':'buy','goodbye':'goodbye','bye':'bye'}
lock_windows_dict = {'lock':'lock'}
ms_word_dict = {'word':'winword'}
ms_excel_dict = {'excel':'excel'}
ms_powerpoint_dict = {'powerpoint':'powerpnt'}
ms_notepad_dict = {'notepad':'notepad'}
map_search_dict = {'locate':'locate',}
play_music_dict = {'play':'play'}
play_yutube_dict ={}

#Defining the audio response list, for predefined tasks.
mp3_greeting_list = ['Maya_Voice/yes-master.mp3','Maya_Voice/hi-there-what-can.mp3']
mp3_open_launch_list = ['Maya_Voice/here-it-is.mp3','Maya_Voice/launching-now.mp3']
mp3_goodbye_list = ['Maya_Voice/good-bye-sir-wish-you.mp3']
mp3_google_search = ['Maya_Voice/this-is-what-i-found.mp3']
mp3_shutdown_list = ['Maya_Voice/system-shutdown-initiated-20-seconds.mp3']
mp3_abort_shutdown_list = ['Maya_Voice/system-shutdown-aborted.mp3']
mp3_reboot_list = ['Maya_Voice/system-reboot-initiated.mp3']
mp3_ok_list = ['Maya_Voice/okay-sir.mp3']

error_occurence = 0
counter = 0

polly = boto3.client('polly', region_name='ap-south-1', aws_access_key_id='your AWS key', aws_secret_access_key='AWS Key')

def play_sound_from_polly(result):
    global counter
    mp3_name = "output.mp3".format(counter)
    obj = polly.synthesize_speech(Text=result, OutputFormat='mp3', VoiceId='Raveena')
    with open(mp3_name,'wb') as file:
        file.write(obj['AudioStream'].read())
        file.close()
        playsound(mp3_name)
        os.remove(mp3_name)
    counter+=1


def google_search_result(query):
    search_result=google.search(query)

    for result in search_result:
        print(result.description)
        play_sound_from_polly(result.description)
        break

#Defining function for google search.
def is_valid_google_search(phrase):
    if(google_search_dict).get(phrase.split(' ')[0])== phrase.split(' ')[0]:
        return True

#Defined to play the sounds randomly.
def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)

def cls():
    os.system("CLS")

#Defining Function to Input the voice from microphone and convert into text.
def read_voice_cmd():
    voice_text = ''
    cls()
    print('[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]')
    print('')
    print('  @@@@        @@@@       @@@@   @@@     @@@    @@@@				         ')
    print('  @@ @@@     @@ @@      @@  @@    @@    @@    @@  @@				         ')
    print('  @@   @@   @@  @@     @@    @@    @@  @@    @@    @@             @         @@@@@@@   ')
    print('  @@     @@@    @@    @@@@@@@@@@    @@@@    @@@@@@@@@@           @  @          @      ')
    print('  @@            @@   @@        @@    @@    @@        @@         @@@@@@         @      ')
    print('  @@            @@  @@          @@   @@   @@          @@       @      @  @  @@@@@@@   ')
    print('')
    print('[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]')
    print('\n')
    print('Listening...')
    global error_occurence

    try:
        with sr.Microphone() as source:
            audio = speech.listen(source=source,phrase_time_limit=10)
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print('Network Unreachable')
    except sr.WaitTimeoutError:
        pass
    return voice_text

#Defining a common function for all tasks like, greeting, opening file explorer,etc.
def is_valid_note(greeting_dict,voice_note):
    for key, value in greeting_dict.iteritems():
        try:
            if value== voice_note.split(' ')[0]:
                    return True
                    break
            elif key == voice_note.split(' ')[1]:
                    return True
                    break
        except IndexError:
            pass

    return False

if __name__ == '__main__':

    playsound('Maya_Voice/hello-sir-i.mp3')

    while True:

        voice_note = read_voice_cmd().lower()
        print('User Command : {}'.format(voice_note))

        if is_valid_note(greeting_dict,voice_note):
            play_sound(mp3_greeting_list)
            continue
        elif is_valid_note(open_launch_dict,voice_note):
            play_sound(mp3_open_launch_list)
            if(is_valid_note(social_media_dict,voice_note)):
                key = voice_note.split(' ')[1]
                webbrowser.open(social_media_dict.get(key))
                continue
            elif(is_valid_note(ms_word_dict,voice_note)):
                key = voice_note.split(' ')[1]
                playsound('Maya_Voice/opening-now.mp3')
                os.system('start winword')
                continue
            elif (is_valid_note(ms_notepad_dict, voice_note)):
                key = voice_note.split(' ')[1]
                playsound('Maya_Voice/opening-now.mp3')
                os.system('start notepad')
                continue
            elif (is_valid_note(ms_excel_dict,voice_note)):
                key = voice_note.split(' ')[1]
                playsound('Maya_Voice/opening-now.mp3')
                os.system('start excel')
                continue
            elif (is_valid_note(ms_powerpoint_dict,voice_note)):
                key = voice_note.split(' ')[1]
                playsound('Maya_Voice/opening-now.mp3')
                os.system('start powerpnt')
                continue
            else:
                os.system('explorer C:\\{}'.format(voice_note.replace('open ', '').replace('launch','')))
                continue
        elif is_valid_google_search(voice_note):
            play_sound(mp3_google_search)
            webbrowser.open('https://www.google.com/search?q={}'.format(voice_note))
            google_search_result(voice_note)

            continue
        elif is_valid_note(map_search_dict,voice_note):
            play_sound(mp3_google_search)
            webbrowser.open('https://www.google.com/maps/place/{}'.format(voice_note.replace('locate','').replace('search','')))
            continue
        elif 'search video' in voice_note:
             playsound('Maya_Voice/youtube video.mp3')
            webbrowser.open('https://www.youtube.com/results?search_query={}'.format(voice_note.replace('search','')))
            continue
        elif is_valid_note(shutdown_mode_dict,voice_note):
            print('Shutdown Initiated')
            play_sound(mp3_shutdown_list)
            os.system('shutdown /s /t 20')
            continue
        elif is_valid_note(abort_shutdown_dict,voice_note):
            print('Shutdown Aborted')
            play_sound(mp3_abort_shutdown_list)
            os.system('shutdown /a')
            continue
        elif is_valid_note(reboot_dict,voice_note):
            print('Rebooting System')
            play_sound(mp3_reboot_list)
            os.system('shutdown /r /t 20')
            continue
        elif is_valid_note(lock_windows_dict,voice_note):
            print('System Locked')
            play_sound(mp3_ok_list)
            os.system('rundll32.exe user32.dll,LockWorkStation')
            continue
        elif is_valid_note(play_music_dict,voice_note):
            print('Playing Music...')
            playsound('Maya_Voice/playing-now.mp3')
            os.system('start vlc Maya_Voice/songs/playlist.xspf')
            continue
        elif 'thank you' in voice_note:
            playsound('Maya_Voice/you-are-welcome-sir.mp3')
            continue
        elif 'tell me' in voice_note:
            playsound('Maya_Voice/tell me about myself.mp3')
            continue
        elif is_valid_note(goodbye_dict,voice_note):
            play_sound(mp3_goodbye_list)
            exit()
