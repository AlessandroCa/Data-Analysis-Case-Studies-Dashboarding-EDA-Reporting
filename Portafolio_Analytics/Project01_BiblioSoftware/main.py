#L'obiettivo del progetto è creare un software per la gestione dei libri di una biblioteca. 
# Il software deve consentire all'utente di interagire continuamente tramite un ciclo infinito, 
# offrendo diverse opzioni per gestire i libri. Il programma terminerà solo quando l'utente inserirà il comando "esci".

import Helper as h
print("Hi, welcome to the library management system")
print("In this software you can do these functions: Add books, Remove books, " \
    "Peek books, Borrow books, View the statistics library, View books and Restore books")
while True:
    try:
        user_fuction = input("What you want do?, digit Exit for quit.")
    except AttributeError:
        print("AttributeError: you aready must enter only these functions: Add books, Remove books, " \
    "Peek books, Borrow books, View the statistics library, View books and Restore books")
    except: #modificare
        print("Error: you haven't entered the functions in correct method, try again")

    if user_fuction == "Exit":
        print(f"The following books are now in the library: {h.books_list}")
        break

    elif user_fuction == "Add books":
        try:
            user_title = input("Digit the title of book")
            user_copies = int(input("Digit the copies of book"))
            h.add_book(user_title, user_copies)
            print("Perfect, the book has been added")
        except ValueError:
            print("ValueError: you must enter an integer")

    elif user_fuction == "Remove books":
        try:
            user_title = input("Digit the title of book that you want delete")
            h.remove_book(user_title)
            print("Perfect, the book has been deleted")
        except: #modificare
            print(".")

    elif user_fuction == "Peek books": #modificare da qui in fondo
        user_title = input("Digit the title of book that you want peek")
        if h.peek_book(user_title) == True:
            print("The selected book is available")
        else:
            print("The selected book isn't available or doesn't exsist")
        
    elif user_fuction == "Borrow books":
        user_title = input("Digit the title of book that you want borrow")
        h.borrow_book(user_title)

    elif user_fuction == "View the statistics library":
        print(f"The statistics libray are as follows: {h.library_statistics}")

    elif user_fuction == "View books":
        print(f"The books available in the library are: {h.view_books()}")

    elif user_fuction == "Restore books":
        try:
            user_title = input("Digit the title of book that you want restore")
            user_copies = int(input("Digit the copies of book"))
            h.restore_book(user_title, user_copies)
        except ValueError:
            print("ValueError: you must enter an integer")



