# Created by: https://github.com/BKPrograms
try:
    import hashlib
    import argparse
    from termcolor import colored
    import os
    import time
    from art import *

except ImportError:
    print("You seem to be missing some necessary libraries, please run pip install -r requirements.txt")

def clearTerminal():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nts":
        os.system("cls")

def getOptions():
    parser = argparse.ArgumentParser()

    parser.add_argument("-w", "--wordlist", dest="wordlistToUse",
                        help="The path to the wordlist to use during the attack")
    parser.add_argument("-c", "--hash", dest="hashToCrack", help="The hash to crack")
    parser.add_argument("-a", "--algorithm", dest="algorithmToUse",
                        help=f"The hashing algorithm to use, including: {hashlib.algorithms_guaranteed}")

    options = parser.parse_args()

    if not options.wordlistToUse:
        parser.error("Specify a wordlist please, run python3 hashCracker.py --help for more info")
    elif not options.hashToCrack:
        parser.error("Specify a hash please, run python3 hashCracker.py --help for more info")
    elif not options.algorithmToUse:
        parser.error("Specify a hashing algorithm to use, run python3 hashCracker.py --help for more info")
    elif ".txt" not in options.wordlistToUse:
        parser.error("Select a valid wordlist")
    elif options.algorithmToUse not in hashlib.algorithms_guaranteed:
        parser.error("Select a valid algorithm to use please")

    return options


def crack(wordList, hash, algorithm):
    found = False
    try:
        with open(wordList, mode="r") as wordlistFile:
            for word in wordlistFile.readlines():
                h = hashlib.new(algorithm)
                h.update(word.strip().encode("utf-8"))
                if h.hexdigest() == hash:
                    found = True
                    print(f"\n[{colored('+', 'green')}] Hash Cracked! Original word was: " + colored(word.strip(),
                                                                                                     color="green") + "\n")
                    break
                else:
                    print(f"[{colored('-', 'red')}] {word.strip()} did not match! Moving onto next guess....")

            if found == False:
                print("\nSorry, hash couldn't be found! Please try another wordlist or select a different hashing algorithm\n")

    except FileNotFoundError:
        print("ERROR FILE NOT FOUND! Did you put the correct wordlist file path?")

    except:
        print("Something went wrong! Either run the script again or create")

clearTerminal()

optionsToUse = getOptions()

tprint("    Hash \nCracker", font="sub-zero")

time.sleep(3)

createdBy = text2art("Created by: ", font="smallcaps3")

profile = colored("https://github.com/BKPrograms", "green")

print(createdBy + profile)

time.sleep(5)

crack(wordList=optionsToUse.wordlistToUse, hash=optionsToUse.hashToCrack, algorithm=optionsToUse.algorithmToUse)
