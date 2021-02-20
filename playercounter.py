#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import sys

def get_count(game) -> int:
    r=requests.get('https://playercounter.com/%s/' % game)
    soup = BeautifulSoup(r.content, features="html.parser")
    return int(soup.find(class_='entry-content').h2.get_text().split()[0].replace(',',''))

try:
    print(get_count(sys.argv[1]))
except IndexError:
    print("supply a game name (i.e. overwatch)")
    exit(1)