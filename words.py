def print_upper_words(list, must_start_with):
    """list: contains a list of words and print out each word on a separate line, but in all uppercase.
    must_start_with: allows you to pass in a set of letters where it only prints out words that start with those letters.
    """

    filteredList = []

    for word in list:
        for char in must_start_with:
            if word[0].lower == char.lower:
                filteredList.append(word)

    for word in filteredList:
        print(word.upper(), '\n')

# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
