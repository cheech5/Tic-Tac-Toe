# WELCOME TO TIC-TAC-TOE
Written in Python
Used PyCharm

# How to play...

'1' --> bottom row, left corner of board
'2' --> bottom row, middle square of board
'3' --> bottom row, right corner of board
'4' --> middle row, left square of board
'5' --> middle row, middle square of board
'6' --> middle row, right square of board
'7' --> top row, left corner of board
'8' --> top row, middle sqaure of board
'9' --> top row, right corner of board


'7' | '8' | '9'
____|_____|_____
'4' | '5' | '6'
____|_____|_____
'1' | '2' | '3'

# Idea behind board numbering

The board is setup like your standard keyboard number pad

# CPU AI Logic
Check 1: check if CPU can win in next turn
Check 2: check if player/user can win in next turn, and block user winning selection
Check 3: try taking one of the 4 corners, if available ('1', '3', '7', '9')
Check 4: try to take the center, if available ('5')
Check 5: try taking one of the sides, if available ('2', '4', '6', '8')
