# # Input that asks the user to enter the amount of students are registered.
students = int(input("Please enter the amount of students registered: "))

# Handles the opening and closing of the file as well as saving the data.
with open('reg_form.txt', 'w') as file:
    for a in range(students):
        id_number = int(input("Please enter the student ID number: "))
        file.write(str(id_number) + '\n')

# Opens a Text file that stores the student information for the register.
print("Thank you, ID numbers saved to txt file reg_form")