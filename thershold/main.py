from model import Model
from options import Options
import sys
import os

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    # sys.path.append(os.path.join(sys.path[0], '../../modules'))
    print_hi(len(sys.path))

model = Model('Пороговый')
options = Options()
options.count = 5
model.Go(options)

print(f'Hi, {model.name}')