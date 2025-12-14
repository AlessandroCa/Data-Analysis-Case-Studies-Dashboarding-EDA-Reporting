import helper as hp
print("Welcome to Serie A Match Analysis 2008-09")
print("In this project, you can find the standing of that season and two functions:" \
"(1) Show team points" \
"(2) Show team results")
while True:
    number_fuction = int(input("Enter number of the function that you want to use it, enter 0 for exit  "))
    if number_fuction == 1:
        hp.show_points
    elif number_fuction == 2:
        hp.show_results
    else:
        print("Just type the number of functions you see above")