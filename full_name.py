user_input = input("Please enter your full name: ")
#Asking the user enter name

if len(user_input) == 0:
    print("You haven't entered any characters. Please enter your full name.")
#using the "==" equals to; to deny the users input

elif len(user_input) < 4:
    print ("You entered less than 4 characters. Please make sure you have entered your name and surname.")


elif len(user_input) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")


else:
    print("Thank you for entering your full name!")   



#I referred to SE T03 PDF slides to complete this task.