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



presents = ["a Partridge in a Pear Tree",
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

and_partridge = "and a Partridge in a Pear Tree"

# enumerate gives an index and element reference
for i, day in enumerate(days):
    print first_line %(day)

    # Print list in reverse range([start], stop[, step])
    for a in range(i, 0, -1):
        print presents[a]

    # Need an 'and' on subsequent verses
    if (i == 0):
        print presents[0]
    else:
        print and_partridge
    print "\n"



