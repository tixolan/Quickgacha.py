# QuickGacha.py
I was bored in a discord call while some people played Genshin Impact and I felt like pulling
some gacha. Decided I could code a simple enough gacha myself and ended up with this.

It's amazing how entertained I got.

## How to use
Simply run
```
py Quickgacha.py <amount>
```

The `amount` is any integer above 0 (if you put 0 or negative numbers it simply won't do anything).
There are also some options which can be checked with the `--help` option.
```
$ py QuickGacha.py --help
usage: QuickGacha.py [-h] [-s] [-i] amount

positional arguments:
  amount         The amount of pulls you wish to do

options:
  -h, --help     show this help message and exit
  -s, --summary  Toggle to show whether you want the summary or not
  -i, --instant  Don't show each pull and just jump to the end
```

## Rarities
To customize the rarities simply edit the `rarity.json`. This file's structure is as follows:
```json
{
    "Rarity Name": {
        "weight": 1.0,
        "color": 30
    }
} 
```
The `weight` can be any positive decimal value, it determines the likelihood of pulling this rarity. The `color` is
a number which represents the [ANSI Escape Code](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors).

## Notes
Because the script only pulls 2000 rarities at a time, you can put whatever number of pulls you desire. While this will make the script take longer to execute it shouldn't affect the amount of memory it consumes.