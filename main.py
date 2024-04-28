def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = get_number_of_words(text)
    character_count_summary = get_character_count_summary(text)
    print(character_count_summary)

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

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
