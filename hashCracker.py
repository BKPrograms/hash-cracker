# Created by: https://github.com/BKPrograms
try:
    import hashlib
    import argparse
    from termcolor import colored
    import os
    import time
    from art import *
    import random

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
    parser.add_argument("-c", "--hash", dest="hashToCrack", help="The hash or .txt file of list of hashes to crack")
    parser.add_argument("-a", "--algorithm", dest="algorithmToUse",
                        help=f"The hashing algorithm to use, including: {hashlib.algorithms_guaranteed}")

    options = parser.parse_args()

    if not options.wordlistToUse:
        parser.error("Specify a wordlist please, run python3 hashCracker.py --help for more info")
    elif not options.hashToCrack:
        parser.error("Specify a hash or list of hashes please, run python3 hashCracker.py --help for more info")
    elif not options.algorithmToUse:
        parser.error("Specify a hashing algorithm to use, run python3 hashCracker.py --help for more info")
    elif ".txt" not in options.wordlistToUse:
        parser.error("Select a valid wordlist")
    elif options.algorithmToUse not in hashlib.algorithms_guaranteed:
        parser.error("Select a valid algorithm to use please")

    return options


def singleHashcrack(wordList, hash, algorithm):
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
                print(
                    "\nSorry, hash couldn't be found! Please try another wordlist or select a different hashing algorithm\n")

    except FileNotFoundError:
        print("ERROR FILE NOT FOUND! Did you put the correct wordlist file path?")
    except KeyboardInterrupt:
        print("\nQuitting Program...Have a nice day!")


def hashListCrack(wordList, hashList, algorithm):
    try:
        print(f"\nSelect {colored('ATTACK MODE', 'red')}")
        print("1. Parallel attack, every hash gets compared to the word in the wordlist at it's corresponding position")
        print("2. Intense attack, every hash is compared to EVERY word in the wordlist in order")
        print("3. Random attack, every hash is compared to a random word in the wordlist only once")
        print("0. Exit Hash-Cracker")
        attackMode = input(f"{colored('Hash-Cracker > ', 'green')}")
        if attackMode == "0":
            print("Have a nice day!")
            time.sleep(2)
            clearTerminal()
            exit()

        while attackMode not in ["1", "2", "3"]:
            print("INVALID CHOICE!\n")
            attackMode = input(f"{colored('Hash-Cracker > ', 'green')}")

        with open(wordList, mode="r") as wordListFile:
            listOfWords = list(wordListFile.readlines())
            with open(hashList, mode="r") as hashListFile:
                listOfHashes = list(hashListFile.readlines())
                resultsString = ""
                hashListFile.seek(0, 0)
                if attackMode == "1":
                    for i, hash in enumerate(hashListFile.readlines()):
                        h = hashlib.new(algorithm)
                        h.update(listOfWords[i].strip().encode('utf-8'))
                        if hash.strip() == h.hexdigest():
                            resultsString = resultsString + f"{hash.strip()} was cracked to be {colored(listOfWords[i], 'green')}\n"
                            listOfHashes.remove(hash)

                elif attackMode == "2":
                    for hash in hashListFile.readlines():
                        for word in listOfWords:
                            h = hashlib.new(algorithm)
                            h.update(word.strip().encode('utf-8'))
                            if hash.strip() == h.hexdigest():
                                resultsString = resultsString + f"{hash.strip()} was cracked to be {colored(word, 'green')}\n"
                                listOfHashes.remove(hash)

                elif attackMode == "3":
                    for hash in hashListFile.readlines():
                        wordListCopy = listOfWords[:]
                        while len(wordListCopy) != 0:
                            randomIndex = random.randint(0, len(wordListCopy)-1)
                            randomWord = wordListCopy[randomIndex]
                            h = hashlib.new(algorithm)
                            h.update(randomWord.strip().encode('utf-8'))
                            if hash.strip() == h.hexdigest():
                                resultsString = resultsString + f"{hash.strip()} was cracked to be {colored(randomWord, 'green')}\n"
                                listOfHashes.remove(hash)
                                break
                            else:
                                wordListCopy.remove(randomWord)

                print("\n" + resultsString)
                if len(listOfHashes) > 0:
                    for uncrackedHash in listOfHashes:
                        print(
                            f"{uncrackedHash.strip()} could not be cracked! Try a different wordlist? Or a different algorithm")
    except FileNotFoundError:
        print("ERROR FILE NOT FOUND! Did you put the correct wordlist file path AND the correct hashlist path?")
    except KeyboardInterrupt:
        print("\nQuitting Program...Have a nice day!")


clearTerminal()

optionsToUse = getOptions()

tprint("    Hash \nCracker", font="sub-zero")

time.sleep(3)

createdBy = text2art("Created by: ", font="smallcaps3")

profile = colored("https://github.com/BKPrograms", "green")

print(createdBy + profile)

time.sleep(5)


if optionsToUse.hashToCrack[-4:] == ".txt":
    hashListCrack(wordList=optionsToUse.wordlistToUse, hashList=optionsToUse.hashToCrack,
                  algorithm=optionsToUse.algorithmToUse)
else:
    singleHashcrack(wordList=optionsToUse.wordlistToUse, hash=optionsToUse.hashToCrack,
                    algorithm=optionsToUse.algorithmToUse)
