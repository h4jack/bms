import json
import os
import sys
import requests

def readisdc():
    try:
        with open("isdcodes.json") as file:
            isdcodes = json.load(file)
        return isdcodes
    except FileNotFoundError:
        print("Error: 'isdcodes.json' file not found.")
    except json.JSONDecodeError:
        print("Error: Unable to parse 'isdcodes.json'. Check if it's valid JSON.")
    sys.exit(2)

def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def check_intr():
    try:
        requests.get("https://motherfuckingwebsite.com")
    except Exception:
        bann_text()
        mesgdcrt.FailureMessage("Poor internet connection detected")
        sys.exit(2)

def format_phone(num):
    num = [n for n in num if n in ['1','2','3','4','5','6','7','8','9','0']]
    return ''.join(num).strip()