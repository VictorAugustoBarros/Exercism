verse = {
    1: "a Partridge in a Pear Tree.",
    2: "two Turtle Doves",
    3: "three French Hens",
    4: "four Calling Birds",
    5: "five Gold Rings",
    6: "six Geese-a-Laying",
    7: "seven Swans-a-Swimming",
    8: "eight Maids-a-Milking",
    9: "nine Ladies Dancing",
    10: "ten Lords-a-Leaping",
    11: "eleven Pipers Piping",
    12: "twelve Drummers Drumming"
}

suffix = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"
}


def recite(start_verse, end_verse):
    song = []
    for i in range(start_verse, end_verse + 1):
        frase = []
        msg = "On the %s day of Christmas my true love gave to me: " % suffix[i]
        for j in range(i, 0, -1):
            if i == 1:
                frase.append(verse[j])
            elif j == 1:
                frase.append("and " + verse[j])
            else:
                frase.append(verse[j])
        msg += ", ".join(frase)
        song.append(msg)

    return song
