first_line = "On the %s day of Christmas my true love sent to me:"

days = ["first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth"]



presents = ["and a Partridge in a Pear Tree",
            "Two Turtle Doves",
            "Three French Hens",
            "Four Calling Birds",
            "Five Golden Rings",
            "Six Geese a Laying",
            "Seven Swans a Swimming",
            "Eight Maids a Milking",
            "Nine Ladies Dancing",
            "Ten Lords a Leaping",
            "Eleven Pipers Piping",
            "12 Drummers Drumming"]

a_partridge = "a Partridge in a Pear Tree"

# enumerate gives an index and element reference
for i, day in enumerate(days):
    print first_line %(day)

    # Needed only for the first verse
    if (i == 0):
        print a_partridge
    else:
        # Print list in reverse range([start], stop[, step])
        for a in range(i, -1, -1):
            print presents[a]

    print "\n"



