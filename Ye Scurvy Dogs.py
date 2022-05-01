#asking the hard questions
cutestdog = input("Who's the cutest dog?")

#all dogs are the cutest dog
print("Correct. The cutest dog is", cutestdog)
print('')

#inspired by WeRateDogs on Twitter
rating = int(input("Rate their cuteness out of 10"))
print("The cuteness of", cutestdog, "is rated at", rating, "out of 10")
print("Just kidding. It's infinite!")
print('')

#time to segue so I can practice with floats
wantingpie = input("Do they want pie?")
print("The correct answer is", wantingpie)

print('')
print("Speaking of pie...")

#this one goes out to the nerds
knowledge = int(input("How many digits of pi do you know?"))

if knowledge >= 16:
    pi = (input("What are the first 16 digits of pi?"))
    knownlength =(len(pi)-1)
    print('')
    print("Congrats! You know pi to at least", knownlength, "digits.")
    floatingpi= float(pi)
    
else:
    print ("What are the first", knowledge, "digits of pi?")
    pi=input()
    knownlength =(len(pi)-1)
    print('')
    print("Congrats! You know pi to at least", knownlength, "digits.")
    floatingpi=float(pi)

#did they tell the truth?
if knowledge == knownlength:
    print("And you are honest!")

if knowledge > knownlength:
    print("Hmm, something doesn't add up...")
    
if knowledge < knownlength:
    print("Modest, I see!")

print('')

#practicing explicit type conversion
rating_int = int(rating)

#now for some implicit type conversion
#let Python do the hard work
pirating = rating + floatingpi

#here's where it really gets goofy
print('')
fakechoice = input('Do you like puns?')
print('')
print("You said", fakechoice)
print('')
print("Either way, you're a captive audience...")
print('')
print("Now we're going to add your rating and your pi...")
print("Your pie rating =", pirating)
print('')
print("Arrr!")
print("Pie rating...get it?")
print('')

#is the user staying afloat?
print("The type of your pie rating is in the <> brackets below.")
print(type(pirating))
shipshape = int(input("Type 1(Yes) or 2(No): does it say 'float' in the line above?"))
print('')
if shipshape == 1:
    print("Thar she blows!")
else:
    print("Avast, matey! Yer a lyin' knave!")

