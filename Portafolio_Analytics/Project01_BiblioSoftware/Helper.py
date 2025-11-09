#In this file, you can find useful functions for managing a library system.
books_list = {}
def add_book(title, copies):     
    if title in books_list:
        books_list[title] += copies
    else:
        books_list[title] = copies

def remove_book(title):
    if title in books_list:
        books_list.pop(title)
    else:
        print("Error: The book doesn't exsist")

def peek_book(title):
    if title in books_list:
        if books_list[title] >= 1:
            return True
        else:
            return False
    else:
        return False
    
def borrow_book(title):
    if title in books_list:
        if books_list[title] >= 1:
            books_list[title] -= 1
        else:
            print("Error: The book isn't available")
    else:
        print("Error: The book doesn't exsist")

def library_statistics():
    statistics_dizionary = {}
    total_books = len(books_list)
    for i in books_list:
        s = sum(books_list[i])
    total_copies = s
    copies_avarage = total_copies / total_books
    statistics_dizionary["Total books"] = total_books
    statistics_dizionary["Total copies"] = total_copies
    statistics_dizionary["Copies avarage"] = copies_avarage
    return statistics_dizionary

def view_books():
    if len(books_list) == 0:
        print("Error: There aren't books")
    else:
        return books_list

def restore_book(title, copies):
    if title in books_list:
        if books_list[title] <= 5:
            books_list[title] += copies
        else:
            print("The selected book already has many copies")
    else:
        print("Error: The book doesn't exsist")