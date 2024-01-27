import requests
import threading, os, json, time
from colorama import Fore

with open("config.json", "r") as file:
    config = json.load(file)

url = config["url"]
love = config["sleep"]
user = config["user"]

banner = Fore.GREEN + f'''
           _ __  __          __             _                       
    ____ _(_) /_/ /_  __  __/ /_     _   __(_)__ _      _____  _____
   / __ `/ / __/ __ \/ / / / __ \   | | / / / _ \ | /| / / _ \/ ___/
  / /_/ / / /_/ / / / /_/ / /_/ /   | |/ / /  __/ |/ |/ /  __/ /                Welcome, {user}
  \__, /_/\__/_/ /_/\__,_/_.___/    |___/_/\___/|__/|__/\___/_/     
 /____/         v1 - Made by @encq                                                                                                     
'''

def request():
    try:
        r = requests.get(url)
        print(f" {w}[{g}+{w}] Sent request: {r.status_code}")
    except KeyboardInterrupt:
        exit(f" {w}[{g}-{w}] Goodbye, {user}!")
    except:
        pass

try:
    os.system('title Github Viewer ︱ Made by t.me/aiosync')
except:
    pass
try:
    os.system('clear')
except:
    pass
try:
    os.system('cls')
except:
    pass
print(banner)

g = Fore.GREEN
w = Fore.WHITE
try:
    input(f' {w}[{g}!{w}] Press [{g}ENTER{w}] to start!')
except KeyboardInterrupt:
    exit(f"\n {w}[{g}-{w}] Goodbye, {user}!")
threads = config["threads"]

if threads == '0':
    while True:
        try:
            print(f" {w}[{g}-{w}] Starting thread...")
            t = threading.Thread(target=request).start()
            time.sleep(float(love))
        except KeyboardInterrupt:
            exit(f" {w}[{g}-{w}] Goodbye, {user}!")
else:
    for _ in range(int(threads)):
        try:
            print(f" {w}[{g}-{w}] Starting thread...")
            t = threading.Thread(target=request).start()
            time.sleep(float(love))
        except KeyboardInterrupt:
            exit(f" {w}[{g}-{w}] Goodbye, {user}!")