from pathlib import Path

import requests

URL = 'https://adventofcode.com/2019/day/{day_number}/input'
COOKIE = dict(
    session='53616c7465645f5f405c809e0f85ce95631c200e0fe9b1651e31982e553be0d2d03af5a96bd8625b5cd8c11167112e9e')
HTTP_OK_CODE = 200

INPUT_DIRECTORY = Path('inputs')
TXT_SUFFIX = '.txt'


def get_input(day_number: str) -> str:
    url = URL.format(day_number=day_number)
    r = requests.get(url, cookies=COOKIE)
    if r.status_code != 200:
        raise ConnectionError(f'Something went wrong. Response: {r.text}')
    return r.text


if __name__ == '__main__':
    day_number_input = input('Enter day number: ')
    input_text = get_input(day_number_input)

    input_file = (INPUT_DIRECTORY / day_number_input).with_suffix(TXT_SUFFIX)
    input_file.write_text(input_text)