from dataset import li
import helper as hp

print("Welcome to Serie A Match Analysis 2008-09")
print("(1) Show team points")
print("(2) Show team results")
print("(0) Exit")

while True:
    number_function = int(input("\nEnter the function number: "))
    if number_function == 1:
        name_team = input("Enter team name: ")
        hp.show_points(name_team)
    elif number_function == 2:
        name_team = input("Enter team name: ")
        hp.show_results(name_team)
    elif number_function == 0:
        print("Goodbye!")
        break
    else:
        print("Please enter a valid number\n")