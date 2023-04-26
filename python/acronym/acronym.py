import re


def abbreviate(words):
    words = re.split('[-+#,_ ]', words)
    acronym = ''

    for letter in words:
        if letter:
            acronym += letter[0]

    return acronym.upper()
