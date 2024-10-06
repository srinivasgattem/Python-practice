def abbreviate_word(word):
    if len(word)<=2:
        return word
    first_letter=word[0]
    last_letter=word[-1]
    middle_count= len(word)-2
    return f"{first_letter}{middle_count}{last_letter}"
word="examination"
abbreviated_word=abbreviate_word(word)
print(abbreviated_word) 