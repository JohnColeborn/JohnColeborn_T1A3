import json

def load_fruit(file_path):

    """
    load fruits from a JSON
    paramaters: file_path: path to the json
    return: list of fruits or empty list if error occurs
    """
    try: 
        with open(file_path, 'r') as file:
            fruits = json.load(file)
            return fruits
    except FileNotFoundError:
        print(f"Error: The file {file_path} doesn't exist")
        return[]
    except Exception as e:
        print(f"all the other errors unexpected {e}")
        return[]
