# method/function that converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 

import re

def to_camel_case(text):
    # Split the text into words based on dashes and underscores
    words = re.split(r'[-_]', text)
    
    # Capitalize the first word if it was originally capitalized
    first_word = words[0]
    rest_words = words[1:]
    if len(first_word) > 0 and first_word[0].isupper():
        first_word = first_word[0] + first_word[1:].lower()
    else:
        first_word = first_word.lower()
    
    # Capitalize the rest of the words
    rest_words = [word.capitalize() for word in rest_words]
    
    # Join the words together into a single string
    return first_word + ''.join(rest_words)


