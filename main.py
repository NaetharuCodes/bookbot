
def count_words(text):
    word_list = text.split()
    return len(word_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    character_dict = {}
    for char in text:
        testChar = char.lower()
        if testChar in character_dict:
            character_dict[testChar] += 1
        else:
            character_dict[testChar] = 1
    return character_dict



def sort_on(d):
    return d["num"]
    
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char" : char, "num" : num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def character_report(character_dict_list):

    for char in character_dict_list:
        if char["char"].islower():
            print(f"The '{char['char']}' character was found {char['num']} times")


def main():
    book = get_book_text("books/frankenstein.txt")

    char_frequency = count_characters(book)

    sorted_report = chars_dict_to_sorted_list(char_frequency)

    character_report(sorted_report)

main()