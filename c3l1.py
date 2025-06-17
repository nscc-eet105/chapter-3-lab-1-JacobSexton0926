print('Numeric Workday Translator')

workday = int(input("\nEnter in the numeric value of the workday you wish to translate: "))

if workday == 1:
    print("The workday is Monday")

elif workday == 2:
    print("The workday is Tuesday")

elif workday == 3:
    print("The workday is Wednesday")

elif workday == 4:
    print("The workday is Thursday")

elif workday == 5:
    print("The workday is Friday")

elif workday == 6 or workday == 7:
    print("The workday is a weekend")

else:
    print("The workday is Invalid")


              
