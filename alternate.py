myString = input("Enter a string: ")   #input for string

alternativeString = ""  #blank string that stores the string with alternate characters capital and small letters

#loop to convert the letters to upper case and lower case

for i in range(len(myString)):

    if i % 2 == 0:

        alternativeString = alternativeString + myString[i].upper()

    else:

        alternativeString = alternativeString + myString[i].lower()

        

print(alternativeString)

#New String

newString = input("Please enter a new string: ") #input for new string

new_alternateString = "" #blank string that stores the string with alternate characters capital and small letters
character = 1

for i in newString.split():
    if character != 1:
        new_alternateString += " " #space in between words
    if character % 2 == 0:
        new_alternateString += i.upper() 
    else:
        new_alternateString += i.lower()
    character += 1

# ^ alternates the words from lower case word to upper case words

print(new_alternateString)