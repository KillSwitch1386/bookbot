def count_words(text):
    words = text.split()
    return len(words)

def character_stats(text):
    new_text = text.lower()
    char_dict = dict()
    
    for char in new_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def main():
    #Read content of frankenstein.txt file
    book = "books/frankenstein.txt"
    
    with open(book) as f:
        file_contents = f.read()

    print(f"--- Begin report of {book} ---")
    print(f"{count_words(file_contents)} words found in the document")
    print("")

    letters = character_stats(file_contents)
    letter_list = []
    for letter in letters:
        if letter.isalpha():
            letter_list.append({"letter": letter, "count": letters[letter]})
    
    letter_list.sort(reverse=True, key=sort_on)
    for record in letter_list:
        print(f"The '{record['letter']}' character was found {record['count']} times")

    print("--- End report ---")
main()