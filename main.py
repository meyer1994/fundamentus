import json
from pathlib import Path
from datetime import date
from argparse import ArgumentParser

import fundamentus

parser = ArgumentParser()
parser.add_argument('date', type=date.fromisoformat)
parser.add_argument('output', type=Path)
args = parser.parse_args()

args.output.mkdir(parents=True, exist_ok=True)

data = fundamentus.load()

for key, val in data.items():
    ticker = args.output / key
    ticker.mkdir(parents=True, exist_ok=True)

    filename = args.date.isoformat() + '.json'
    filename = ticker / filename

    with open(filename, 'wt') as file:
        json.dump(val, file, indent=2, sort_keys=True)
