from model import Model
from options import Options

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Lets start....')

model = Model('Пороговый')
options = Options()
options.count = 5
model.Go(options)

print(f'Hi, {model.name}')