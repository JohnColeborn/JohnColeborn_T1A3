import random
from file_ops import load_fruit

FILE_PATH = '../data/fruits.json'

def picker_random():
    fruits = load_fruit(FILE_PATH)    
# Random Fruit Picker
    picker = random.choice(fruits) 
    return picker
