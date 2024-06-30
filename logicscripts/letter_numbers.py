# Count the letters in each word
def count_char(text):
    return len(text)

# In case I want to add hints, eg : "this word has 2 letters the same"
def count_unique_char(text):
    return len(set(text.lower()))

