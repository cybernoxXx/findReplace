def findAndReplace(text, oldText, newtext):
    i = 0
    textReplaced = ""

    while(i < len(text)):
        # I have to check all the possible ordered sequence to find a match
        if text[i:i+len(oldText)] == oldText:
            textReplaced = textReplaced + newtext
            # If i find a match i add the substitution and the counter start at the end of the substitution, I don't want to add the same to i and replaced text
            i = i + len(oldText)
        else:
            textReplaced += text[i]
            i = i + 1
    return textReplaced

assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
assert findAndReplace('fox', 'fox', 'dog') == 'dog'
assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'
assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
