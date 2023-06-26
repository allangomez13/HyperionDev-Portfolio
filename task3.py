swimming = int(input("Enter the time taken to complete swimming in minutes: "))
print("Swimming time: ",swimming)


cycling = int(input("Enter the time taken to complete cycling in minutes: "))
print("Cycling time: ",cycling)

running = int(input("Enter the time taken to complete running in minutes: "))
print("Running time: ",running)

#Qualifying time 100 

total = swimming + cycling + running
print("Total time taken to complete the triathlon: ",total)

if (total < 100):
    print("Award: Provincial Colours")

elif (total > 100 and total <= 105):
    print("Award: Provincial Half Colours")

elif (total > 105 and total <= 110):
    print("Award: Provincial Scroll")

else:
    print("No award")

#In reference to SE T04 PDF Slides & SE T03, used to complete task.