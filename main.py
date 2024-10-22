from library_functions import like_book, list_books, comment_book, book_details, add_book, delete_book, rate_book
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import print

admin = {"username": "admin_user", "password": "admin123"}  
viewer = {"username": "viewer_user", "password": "viewer123"}
console = Console()

def main():
    try:
        while True:
            console.print("\n[bold blue] Welcome to Abjad Library!\n[/bold blue]")
            username1 = input("Enter your username: ").strip().lower()
            password1 = input("Enter your password: ").strip().lower()
            
            # Check is it the admin
            if username1 == admin["username"] and password1 == admin["password"]:
                admin_view()
            # Check is it the viewer
            elif username1 == viewer["username"] and password1 == viewer["password"]:    
                visitor_view()
            else:
                print("\nInvalid username or password! Please try again.")
    except KeyboardInterrupt:
        # Handle Ctrl+C 
        print("\nExiting the program. Thank you!")
        return
    except EOFError:
        print("Invalid input!")
        return

def visitor_view():
    while True:
        print("Type 'list' to browse books, type 'view' for details, type 'comment' to add a comment, type 'like' to like the book, type 'rate' to rate the book, or 'logout' to log out.")

        user_type = input().strip().lower()
        try:
            if user_type == "list":
                list_books()
            elif user_type == "view":  
                book_id = input("Type the book ID: ")
                book_details(int(book_id))
            elif user_type == "comment":
                while True: 
                    try:
                        book_id = input("Type the book ID: ")
                        type_comment = input("Type your comment: ")
                        comment_book(int(book_id), type_comment)
                        break  
                    except ValueError:
                        print("Invalid input! Please enter a numeric book ID.")
            elif user_type == "like":
                while True:  # Loop until valid input is received
                    try:
                        book_id = input("Type the book ID: ")
                        like_book(int(book_id))
                        break  # Exit the loop if the input is valid
                    except ValueError:
                        print("Invalid input! Please enter a numeric book ID.")
            elif user_type == "rate":
                while True:  # Loop until valid input is received
                    book_id = input("Type the book ID: ")
                    try:
                        rating = float(input("Enter your rating (1-5): "))
                        if 1 <= rating <= 5:
                            rate_book(int(book_id), rating)
                            break  # Exit the loop if the rating is valid
                        else:
                            print("Invalid rating! Please enter a rating between 1 and 5.")
                    except ValueError:
                        print("Invalid input! Please enter a numeric rating between 1 and 5.")    
            elif user_type == "logout":
                print("Thank you!")
                return  # return to the main
            else:
                print("Invalid option. Try again!")
        except ValueError:
            print("Invalid input!")
        except Exception as e:
            print(f"An error occurred. {str(e)}")

def admin_view():
    while True:
        print("\nAdmin Menu: Type 'add' to add a book, 'list' to list all the books, 'remove' to remove a book, or 'logout' to log out.")       
        admin_action = input().strip().lower()
        try:
            if admin_action == "add":
                add_book()
            elif admin_action == "remove":
                book_id = input("Type the book ID to remove: ")
                delete_book(book_id)
            elif admin_action == "list":
                list_books()   
            elif admin_action == "logout":
                print("Exiting admin mode.")
                return  # return to the main
            else:
                print("Invalid option. Try again!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

main()