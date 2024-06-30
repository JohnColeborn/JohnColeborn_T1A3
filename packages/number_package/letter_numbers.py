# Count the letters in each word
def count_char(text):
    return len(text)

def count_unique_char(text):
    return len(set(text.lower()))

# Check output
print(count_char("This is a test"))
print(count_unique_char("This is a test"))