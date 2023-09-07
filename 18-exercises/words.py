# def print_upper_words(words):
#     """for each word in list, print word in uppercase"""

#     for word in words:
#         print(word.upper())

# def print_upper_words(words):
#     """for each word in list, print word in uppercase"""

#     for word in words:
#         if word[0] == 'e' or word[0] == 'E':
#             print(word.upper())

def print_upper_words(words, must_start_with):
    """for each word in list, print word in uppercase"""
    for word in words:
        for letter in must_start_with:
            if word[0] == letter:
                print(word.upper())
                break


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  must_start_with={"h", "y"})
