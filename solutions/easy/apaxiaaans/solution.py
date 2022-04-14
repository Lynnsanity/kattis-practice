#https://open.kattis.com/problems/apaxiaaans
from typing import Dict, Set, List
from typing import Optional
import sys
from sys import stdin

#reading input import
lines: List[str] = list(stdin)

#the checker for whatever the last character was:
last_char: Optional[str] = None

#narrowing down to character
line: str = lines[0]
word: str = line.strip()

#characters accepted will get added to:
new_word: str = ''

for character in word:
    
    #do nothing if the character is same as last
    if character == last_char:
        pass
    else:
        #if character isn't the same as last, make sure the character goes into the new word
        #also make the last character the current in checker
        new_word += character
        last_char = character

print(new_word)

