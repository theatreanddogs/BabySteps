#Shakespeare's life span becomes a very small dictionary
dates = {'birth' : 1564 , 'death': 1616}

#print the info
print("Shakespeare was born during", dates['birth'])
print("Shakespeare died in the year", dates['death'])
print('')

#playing with the first line of sonnet 18
firstline = "Shall I compare thee to a summer's day"
print("The first word of Sonnet 18 is", firstline[0:5])
print("The first line of Sonnet 18 is", len(firstline), "characters long.")
print('')

#history plays as the king's number
#set will reorder and eliminate redundancies (wishful thinking for some?)
histories = {6, 6, 6, 3, 2, 4, 4, 5, 1, 8}
print("The kings in the histories had the following numbers:", histories)
print('')

#names of those kings as a tuple (in order of the plays' writing)
kingnames = ("Henry VI", "Richard III", "Richard II", "Henry IV", "Henry V", "King John", "Henry VIII")

#print the full name of each play in that order on separate lines
print(kingnames[0], "Part 1")
print(kingnames[0], "Part 2")
print(kingnames[0], "Part 3")
print(kingnames[1])
print(kingnames[2])
print(kingnames[3], "Part 1")
print(kingnames[3], "Part 2")
print(kingnames[4])
print(kingnames[5])
print(kingnames[6])
print('')

#make the big four tragedies a list
bigtragedies = ['Hamlet', 'Othello', 'Macbeth', 'Lear']

#print the tragedies Marc Pouhe has starred in on the same line
print(bigtragedies[1:3])
print(" ")

#print the tragedies RS has done on separate lines
print("Rosedale Shakespeare has done:")
print(bigtragedies[0])
print(bigtragedies[2])