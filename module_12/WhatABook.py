'''
Cory Thomaier
WhatABook Application
2/21/2023
'''
#import
import sys
import mysql.connector
from mysql.connector import errorcode
'''FUNCTIONS'''
#Connect to DB
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#main menu function
def menu():
    print("\n**Main Menu**")

    print("1. View Books\n2. View Store Locations\n3. My Account\n4. Exit Program")

    try:
        choice = int(input('Select a number 1-4: '))

        return choice
    except ValueError:
        print("\nInvalid number, good bye...\n")

        sys.exit(0)

#store locations function
def locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n**DISPLAYING STORE LOCATIONS**")

    for location in locations:
        print("Locale: {}\n".format(location[1]))

#display book function
def display_books(_cursor):
    # inner join 
    _cursor.execute("SELECT book_id, book_name, author, details FROM book")

    # results 
    books = _cursor.fetchall()

    print("\n**DISPLAYING BOOK LISTINGS**")
    
    # display the results 
    for book in books:
        print("Book Name: {}\nAuthor: {}\nDetails: {}\n".format(book[0], book[1], book[2]))

#account menu function
def account_menu():
    #display the users account menu
    try:
        print("\n**Customer Menu**")
        print("1. Wishlist\n2. Add Book\n3. Main Menu")
        account_option = int(input('<Example enter: 1 for wishlist>: '))

        return account_option
    except ValueError:
        print("\n  Invalid number, goodbye...\n")

        sys.exit(0)

#userid function
def validate_user():
    # validate the users ID

    try:
        user_id = int(input('\nCustomer id: '))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer id, goodbye...\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid id, goodbye...\n")

        sys.exit(0)

#whishlist function
def show_wishlist(_cursor, _user_id):
    #query the database for a list of books added to the users wishlist

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n**DISPLAYING WISHLIST ITEMS**")

    for book in wishlist:
        print("Book Name: {}\nAuthor: {}\n".format(book[4], book[5]))

#books to add function (not in whishlist)
def show_books_to_add(_cursor, _user_id):
    #query the database for a list of books not in the users wishlist

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n** DISPLAYING AVAILABLE BOOKS**")

    for book in books_to_add:
        print("Book Id: {}\nBook Name: {}\n".format(book[0], book[1]))

#insert into whishlist funtion
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))


'''MEAT AND POTATOES OF THE PROGRAM'''

try:
    #try/catch for errors

    db = mysql.connector.connect(**config) # connect to the WhatABook database 

    cursor = db.cursor() # cursor for queries

    print("\nWelcome to the WhatABook Webstore!")

    user_selection = menu() # show the main menu 

    # while the user's selection is not 4
    while user_selection != 4:

        # this will display the books if the user selects option 1
        if user_selection == 1:
            display_books(cursor)

        # this will display the locations if the user selects option 2
        if user_selection == 2:
            locations(cursor)

        # if the user selects option 3, the validate method is called followed by the account menu
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = account_menu()

            # while account option does not equal 3
            while account_option != 3:

                # if the user selects option 1, show the whishlist
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # if the user selects option 2, show the books available to add to the users wish list
                if account_option == 2:

                    # show the books not currently configured in the users wishlist
                    show_books_to_add(cursor, my_user_id)

                    # get the entered book_id 
                    book_id = int(input("\nEnter the id of the book you want to add: "))
                    
                    # add the selected book the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() # commit the changes to the database 

                    print("\nBook id: {} was added to your wishlist!".format(book_id))

                # if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\nInvalid option, please retry...")

                # show the account menu 
                account_option = account_menu()
        
        # if the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\nInvalid option, please retry...")
            
        # show the main menu
        user_selection = menu()

    print("\n\nGoodbye...")

except mysql.connector.Error as err:
    #handle errors

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")

    else:
        print(err)

finally:
    #exit

    db.close()