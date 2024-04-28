import sys

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    number_of_words = get_number_of_words(text)
    character_count_summary = get_character_count_summary(text)
    character_list = get_character_list(character_count_summary)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the document")
    print("")
    for char in character_list:
        print(f"The '{char["name"]}' character was found {char["num"]} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_character_count_summary(text):
    lowered_text = text.lower()
    character_count_summary = {}
    for char in lowered_text:
        if char in character_count_summary:
            character_count_summary[char] += 1
        else:
            character_count_summary[char] = 1  
    return character_count_summary

def get_character_list(character_count_summary):
    character_list = []
    for char in character_count_summary:
        if char.isalpha():
            character_list.append({"name": char, "num": character_count_summary[char]})
    character_list.sort(reverse=True, key=sort_on)
    return character_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
