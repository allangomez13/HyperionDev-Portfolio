names = []
birthdays = []

f = open("DOB.txt", "r") # Opens The file
data = f.readlines()

for line in data:
    parts = line.split()
    names.append(parts[:2])  # stores the names
    birthdays.append(parts[2:])  # stores the birthdays

f.close() # Closes the file

print("Name")
for i, name in enumerate(names, start=1):
    print("{}. {}".format(i, " ".join(name)))
                                                # Sections the information from the file to birthdays and Names.
print("Birthdays")
for i, birthdays in enumerate(birthdays, start=1):
    print("{}. {}".format(i, " ".join(birthdays)))