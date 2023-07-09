import sys

# sys.path.append(str(Path(__file__).parents[1].joinpath('modeling'))
sys.path.append('../modeling')

#from model import Model
from infrastructure.options import Options

#model = Model('Пороговый')
options = Options()
options.count = 5
#model.Go(options)

#print(f'Hi, {model.name}')

print(len(sys.path))