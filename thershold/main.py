import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1].joinpath('modeling')))

from model import Model
from options import Options

model = Model('Пороговый')
options = Options()
options.count = 5
model.Go(options)

print(f'Hi, {model.name}')

print(len(sys.path))