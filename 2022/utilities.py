from datetime import datetime
from pathlib import Path
import requests


project_root = Path('/home/carlo/AdventOfCode')
YEAR = datetime.today().year
DAY = datetime.today().day
midnight = datetime(YEAR, 12, DAY, 0, 0, 0, 0)


def load_data(year=YEAR, day=DAY):
    input_file = Path(f'{project_root}/{year}/input_data/day_{day}.txt')
    if input_file.exists():
        print('Cached input file found.  Loading...')
    else:
        print('No local input file. Downloading...')
        with open(f'{project_root}/.aoc_cookie', 'r') as f:
            aoc_cookie = f.read().strip()
        url = f'https://adventofcode.com/{year}/day/{day}/input'
        response = requests.get(url, cookies={'session': aoc_cookie})
        with open(input_file, 'w') as f:
            f.write(response.text)
    with open(input_file, 'r') as f:
        input_data = f.read().strip()
    print('\t...done.')
    return input_data


def submit(answer, part, year=YEAR, day=DAY):
    url = f'https://adventofcode.com/{year}/day/{day}/answer'
    payload = {'level': part, 'answer': answer}
    with open('.aoc_cookie', 'r') as f:
        aoc_cookie = f.read().strip()
    response = requests.post(url, payload, cookies={'session': aoc_cookie})
    if 'That\'s the right answer!' in response.text:
        dt = datetime.now() - midnight
        print(f'Fucken sick bro you got part {part}!')
        print(f'Time taken: {dt}')
    elif 'You don\'t seem to be solving the right level.' in response.text:
        print(f'Ya already solved part {part} knucklehead.')
    else:
        print('Incorrect!  Keep trying!')
    return response
