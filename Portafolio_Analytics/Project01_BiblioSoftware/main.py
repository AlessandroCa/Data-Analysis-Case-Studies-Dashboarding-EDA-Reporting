import Helper as h
print("Hi, welcome to the library management system")
print("In this software you can do these functions: ")
print("(1) Add a book")
print("(2) Remove a book")
print("(3) Check availability")
print("(4) Borrow a book")
print("(5) View statistics")
print("(6) View books")
print("(7) Restore a book")
print("(0) Exit")

while True:
    try:
        user_fuction = input("What you want do?, digit the number of fuction.  ")
    except KeyboardInterrupt:
        print("Input cancelled. Exiting.")
 
    if user_fuction == "0":
        print(f"The following books are now in the library: {h.books_list}")
        break

    elif user_fuction == "1":
        try:
            user_title = input("Digit the title of book  ").strip().lower()
            while True:
                user_copies = int(input("Digit the copies of book  "))
                if user_copies <= 0:
                    print("Error: you can't enter negative numbers, try again")
                    continue
                else: 
                    break
            h.add_book(user_title, user_copies)
            print("Perfect, the book has been added")
        except ValueError:
            print("ValueError: you must enter an integer")

    elif user_fuction == "2":
            user_title = input("Digit the title of book that you want delete  ").strip().lower()
            h.remove_book(user_title)
            print("Perfect, the book has been deleted")

    elif user_fuction == "3":
        user_title = input("Digit the title of book that you want peek  ").strip().lower()
        if h.peek_book(user_title) == True:
            print("The selected book is available, for borrow enter - 4")
        else:
            print("The selected book isn't available or doesn't exsist")
        
    elif user_fuction == "4":
        user_title = input("Digit the title of book that you want borrow  ").strip().lower()
        h.borrow_book(user_title)
        print("Perfect, your loan has been processed.")

    elif user_fuction == "5":
        print(f"The statistics libray are as follows: {h.library_statistics()}")

    elif user_fuction == "6":
        print(f"The books available in the library are: {h.view_books()}")

    elif user_fuction == "7":
        try:
            user_title = input("Digit the title of book that you want restore  ").strip().lower()
            while True:
                user_copies = int(input("Digit the copies of book  "))
                if user_copies <= 0:
                    print("Error: you can't enter negative numbers, try again")
                    continue
                else: 
                    break
            h.restore_book(user_title, user_copies)
        except ValueError:
            print("ValueError: you must enter an integer")
    
    else:
<<<<<<< HEAD
        print("Error: you already must enter only these functions:")
        print("(1) Add a book")
        print("(2) Remove a book")
        print("(3) Check availability")
        print("(4) Borrow a book")
        print("(5) View statistics")
        print("(6) View books")
        print("(7) Restore a book")
        print("(0) Exit")

=======
        print("Error: you already must enter only these functions: Add books, Remove books, " \
    "Peek books, Borrow books, View statistics library, View books and Restore books, try again")
>>>>>>> fb1bc4def9e48b8e39085f555fe29af1d0874be8



