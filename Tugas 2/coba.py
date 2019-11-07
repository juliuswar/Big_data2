import re

mystr = 'This is a string, with words!'
wordList = re.sub("[^\w]", " ",  mystr).split()