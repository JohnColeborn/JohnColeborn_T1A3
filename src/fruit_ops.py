def fruit_picker(fruits):
    try:
        for fruit in fruits:
            print(f"{fruits}")
    except KeyError as e:
        print(f"{e}")
    except Exception as e:
        print(f"{e}")

