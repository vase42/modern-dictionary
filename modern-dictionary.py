#!/usr/bin/env python3
import sys
import requests
import argparse
from numpy import random
def clean_string(text):
    text = text.replace('[', '').replace(']', '')
    text = text.replace('"', '')
    return text

def filter_words(data, target_word):
    filtered_data = []
    target_word = target_word.strip().lower()
    for item in data:
        item_word = item["word"].strip().lower()
        if item_word == target_word:
            filtered_data.append(item)

    if not filtered_data and data:
        return data
    return filtered_data

def getWord(word):
    if word == "yyy":
        url = f"https://api.urbandictionary.com/v0/random"
    else:
        url = f"https://api.urbandictionary.com/v0/define?term={word}"
    response = requests.get(url)
    data = response.json()
    data = data["list"]
    if word != "yyy":
        data = filter_words(data, word)
    if data:
        word = data[0]
        RED = '\033[0;31m'
        GREEN = '\033[0;32m'
        NC = '\033[0m'
        print()
        print(f"{RED}{word['word']}{NC}")
        print()
        print(f"{GREEN}Definition:{NC}")
        print(clean_string(word["definition"]))
        print()
        print(f"{GREEN}Example:{NC}")
        print(clean_string(word["example"]))
        print()
        print(f"{GREEN}By:{NC} {word['author']}")
    else:
        print(f"No definitions found for '{word}'.")

def warningWord():
    print("I will skin you alive.")


def print_help():
    RED = '\033[0;31m'
    WHITE = '\033[1;37m'
    NC = '\033[0m'  # Reset color

    print(f"""
{RED}///////////////////////{NC}
{RED}// {WHITE}Modern Dictionary{RED} //{NC}
{RED}///////////////////////{NC}

Usage:
  modern-dictionary [WORD] [-r | --random]

Description:
  Fetches the definition of a word from Modern Dictionary.

Options:
  WORD         The word to define.
  -r, --random Get a random word definition.
  -h, --help   Show this help message.

Examples:
  modern-dictionary zeko      # Get definition of "zeko"
  modern-dictionary -r        # Get a random word definition
""")
    sys.exit(0)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get definitions from Urban Dictionary.",add_help=False)  # Disable default help
    parser.add_argument("-r", "--random", action="store_true", help="Return a random word definition")
    parser.add_argument("-h", "--help", action="store_true", help="Show help message")  # Custom help flag
    parser.add_argument("word", nargs="?", default=None, help="The word to define")
    args = parser.parse_args()

    if random.randint(1, 100) > 3:
        if args.random:
            getWord("yyy")
        elif args.word:
            getWord(args.word)
        elif args.help:
            print_help()
        else:
            print_help()
    else:
        warningWord()