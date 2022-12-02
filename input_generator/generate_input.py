import os

import requests
from dotenv import load_dotenv

load_dotenv("./.env")
COOKIE = os.getenv("cookie")


def main():
    cookies = {'session': COOKIE}
    day = get_day()
    url = f"https://adventofcode.com/2022/day/{day}/input"

    text = requests.get(url, cookies=cookies).text

    f = open("input.txt", "w")
    f.write(text)


def get_day():
    valid = False
    while not valid:
        try:
            day = int(input("Which day would you like to solve (1 to 24)? "))
            if (day >= 1 and day <= 24):
                valid = True
            else:
                print("Sorry, please only enter an integer from 1 to 24.")
        except (ValueError, TypeError):
            print("Sorry, please only enter an integer from 1 to 24.")
    return day


if __name__ == "__main__":
    main()
