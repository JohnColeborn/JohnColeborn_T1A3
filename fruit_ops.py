def fruit_picker(fruits):
    try:
        for fruit in fruits:
            print(f"{fruit}")
    except KeyError as e:
        print(f"{e}")
    except Exception as e:
        print(f"{e}")

