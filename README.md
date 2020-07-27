# hash-cracker
## Description:
Hash cracker is a simple script written in python3 that can be used to identify the original value of a hash. The script takes in a wordlist, the actual hash to crack, and the algorithm which the hash has been produced from. 
**Disclaimer:** This will not work with python2 so please run this script with python3.

### Hashing Algorithms Supported:
* SHA-1
* SHA-256
* SHA-512
* SHA-224
* SHA-384

* SHA3-256
* SHA3-512
* SHA3-224
* SHA3-384

* BLAKE2S
* SHAKE-128
* BLAKE2B
* SHAKE-256
* MD5

### Supported Platforms:
* Linux
* Windows

### Installation:
1. Open terminal or cmd and run the following: `git clone https://github.com/BKPrograms/hash-cracker.git`

2. Next, navigate into the newly cloned directory and run `pip install -r requirements.txt`

3. Finally, to run the script `python3 hashCracker.py -w wordlistYouWantToUse.txt -a algorithmToUse -h hashToCrack` or run `python3 hashCracker.py --help` for more info

### Usage:

`python3 hashCracker.py -w wordlistYouWantToUse.txt -a algorithmToUse -h hashToCrack`. Note: make sure to include the full filepath to the wordlistYouWantToUse.txt

## Issues and Errors:

If any issues are present and persist, please report to https://github.com/BKPrograms/hash-cracker/issues
