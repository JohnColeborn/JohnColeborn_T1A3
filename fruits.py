import random
from file_ops import load_fruit

FILE_PATH = './data/fruits.json'

def fruit_picker():
    fruits = load_fruit(FILE_PATH)    
# Random Fruit Picker
    picker = random.choice(fruits)
    print(picker)
    


fruit_picker()