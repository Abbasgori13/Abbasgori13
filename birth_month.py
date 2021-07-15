birthday = input("Enter your birthday in this format DD-MM-YYYY :")
months = ( "jan", "feb", "march", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nau", "dec" )

check = int(birthday[3:5]) - 1
bd_month = months[check]
print("You were born in ", bd_month)