def main():
    bookpath = "books/frankenstein.txt"
    text = get_book_text(bookpath)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print_report(bookpath, num_words, num_chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split(" ")
    return len(words)

def get_num_chars(text):

    character_dictionary = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0,
        "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
        "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
    }

    character_list = list(text.lower())

    print(f"the length of your character list is {len(character_list)}")

    for char in character_list:

        if char in character_dictionary:
            character_dictionary[char] += 1

    return character_dictionary


def print_report(path, words, char_dict):
    print(f"---Begin report of {path} ---")
    print(f"{words} found in the document")
    for entry in char_dict:
        print(f"The '{entry}' character was found {char_dict[entry]} times in the document.")
    print("--- End Report ---")

main()
