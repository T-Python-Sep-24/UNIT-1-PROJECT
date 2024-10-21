from library_functions import like_book, list_books, comment_book, book_details, add_book, delete_book, rate_book


admin= {"username": "admin_user", "password": "admin123"},
viewer= {"username": "viewer_user", "password": "viewer123"}


def main():
    while True:
        print("Welcome to the Virtual Book Library!\n")
        username1 = input("Enter your username: ").strip().lower()
        password1 = input("Enter your password: ").strip().lower()
        
        if username1 == "admin_user" and password1 == "admin123":
            admin_view()
        elif username1 == "viewer_user" and password1 == "viewer123":    
            visitor_view()
        else:
            print("\nInvalid username or password! Please try again.")

def visitor_view():
    while True:
        print("Type 'list' to browse books, type 'view' for details, type 'comment' to add a comment, type 'like' to like the book, type 'rate' to rate the book, or 'exit' to quit..")

        user_type = input().strip().lower()
        if user_type == "list":
            list_books()
        elif user_type == "view":  
            book_id = input("Type the book ID: ")
            book_details(int(book_id))
        elif user_type == "comment":
            book_id = input("Type the book ID: ")
            type_comment = input("Type your comment: ")
            comment_book(int(book_id), type_comment)
        elif user_type == "like":
            book_id = input("Type the book ID: ")
            like_book(int(book_id))
        elif user_type == "rate":
            book_id = input("Type the book ID: ")
            rating = float(input("Enter your rating (1-5): "))
            if 1 <= rating <= 5:
                rate_book(int(book_id), rating)
            else:
                print("Invalid rating! Please enter a rating between 1 and 5.")    
        elif user_type == "exit":
            print("Thank you!")
            return  # return to the main
        else:
            print("Invalid. Try again!")

def admin_view():
    while True:
        print("\nAdmin Menu: Type 'add' to add a book, 'remove' to remove a book, or 'exit' to quit.")       
        admin_action = input().strip().lower()
        if admin_action == "add":
            add_book()
        elif admin_action == "remove":
            book_id = input("Type the book ID to remove: ")
            delete_book(book_id)
        elif admin_action == "list":
            list_books()   
        elif admin_action == "exit":
            print("Exiting admin mode.")
            return  # return to the main
        else:
            print("Invalid. Try again!")

main()