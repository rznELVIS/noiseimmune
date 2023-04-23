# from model import Model
import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).parents[1].joinpath('modeling')))

from model import Model
from options import Options

if __name__ == '__main__':
    # sys.path.append(os.path.join(sys.path[0], '../../modules'))
    print(len(sys.path))

model = Model('Пороговый')
options = Options()
options.count = 5
model.Go(options)

print(f'Hi, {model.name}')

print(len(sys.path))