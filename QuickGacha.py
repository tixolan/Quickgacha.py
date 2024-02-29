#!/usr/bin/python

import json
import random
import sys
import argparse

THRESHOLD = 2000
RESET_STYLE = '\x1b[0m'
BOLD_STYLE = '\x1b[1m'

class QuickGacha:
    rarities = {}
    pulled = {}

    def __init__(self, rarities: dict[str, dict[str, float | int]]):
        self.rarities = rarities
        self.pulled = {k: 0 for k, _ in rarities.items()}

    def pull(self, amount: int) -> list[str]:
        pulls = random.choices(
            list(self.rarities.keys()),
            list(map(lambda x: x["weight"], self.rarities.values())),
            k=amount
        )

        for item in pulls:
            self.pulled[item] = self.pulled.get(item, 0) + 1

        return pulls


def convertToDict(file: str) -> dict[str, dict[str, float | int]]:
    data = {}
    with open(file) as open_file:
        data = json.load(open_file)

    return data

def printPulls(counted, pulls, rarities):
    for c in pulls:
        print(f'{counted["i"]}:', f'\x1b[{rarities[c]["color"]}m' + c, RESET_STYLE)
        counted["i"]+=1

def main() -> int:
    rarities = convertToDict('rarity.json')
    gacha = QuickGacha(rarities)
    parser = argparse.ArgumentParser()

    parser.add_argument("amount", type=int, help="The amount of pulls you wish to do")
    parser.add_argument("-s", "--summary", action="store_true", help="Toggle to show whether you want the summary or not")
    parser.add_argument("-i", "--instant", action="store_true", help="Don't show each pull and just jump to the end")

    args = parser.parse_args()

    if not args.summary and args.instant:
        print("You selected no summary and an instant pull, I have nothing to show.")
        return 0

    amount = args.amount
    
    if not args.instant:
        print(f'Pulling {amount}...')

    counted = {"i": 1}

    while amount > THRESHOLD:
        pull = gacha.pull(THRESHOLD)
        amount -= THRESHOLD
        if not args.instant:
            printPulls(counted, pull, rarities)

    pull = gacha.pull(amount)
    
    if not args.instant:
        printPulls(counted, pull, rarities)

    if args.summary:
        print(BOLD_STYLE, 'Summary:', RESET_STYLE, sep='')
        for k, v in gacha.pulled.items():
            print(f'\x1b[{rarities[k]["color"]}m{k}: ', RESET_STYLE, v, sep='')
    return 0

if __name__ == "__main__": main()
