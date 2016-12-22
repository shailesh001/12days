def censor(org_text, match_word):
    censor_str = "*" * len(match_word)

    # Split string into a list of strings
    text_list = org_text.split(" ")

    # Iterate text_list with index
    for index, word in enumerate(text_list):
            # if word in list matches match_word then replace with ****...
            if word == match_word:
                text_list[index] = censor_str

    # Turn list into string of words separated with space
    return " ".join(text_list)


print(censor("this hack is wack hack", "hack"))

