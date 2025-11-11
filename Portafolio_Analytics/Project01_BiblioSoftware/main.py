import Helper as h
print("Hi, welcome to the library management system")
print("In this software you can do these functions: Add books, Remove books, " \
    "Peek books, Borrow books, View statistics library, View books and Restore books")
while True:
    try:
        user_fuction = input("What you want do?, digit Exit for quit.  ")
    except KeyboardInterrupt:
        print("Input cancelled. Exiting.")
 
    if user_fuction == "Exit":
        print(f"The following books are now in the library: {h.books_list}")
        break

    elif user_fuction == "Add books":
        try:
            user_title = input("Digit the title of book  ")
            user_copies = int(input("Digit the copies of book  "))
            h.add_book(user_title, user_copies)
            print("Perfect, the book has been added")
        except ValueError:
            print("ValueError: you must enter an integer")

    elif user_fuction == "Remove books":
            user_title = input("Digit the title of book that you want delete  ")
            h.remove_book(user_title)
            print("Perfect, the book has been deleted")

    elif user_fuction == "Peek books":
        user_title = input("Digit the title of book that you want peek  ")
        if h.peek_book(user_title) == True:
            print("The selected book is available, for borrow enter - Borrow books")
        else:
            print("The selected book isn't available or doesn't exsist")
        
    elif user_fuction == "Borrow books":
        user_title = input("Digit the title of book that you want borrow  ")
        h.borrow_book(user_title)
        print("Perfect, your loan has been processed.")

    elif user_fuction == "View statistics library":
        print(f"The statistics libray are as follows: {h.library_statistics()}")

    elif user_fuction == "View books":
        print(f"The books available in the library are: {h.view_books()}")

    elif user_fuction == "Restore books":
        try:
            user_title = input("Digit the title of book that you want restore  ")
            user_copies = int(input("Digit the copies of book  "))
            h.restore_book(user_title, user_copies)
        except ValueError:
            print("ValueError: you must enter an integer")
    
    else:
        print("Error: you already must enter only these functions: Add books, Remove books, " \
    "Peek books, Borrow books, View statistics library, View books and Restore books, try again")



