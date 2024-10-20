from gallery_functions import like_artwork, list_artworks, comment_artwork, artwork_details

def main():
    print("Welcome to the Virtual Art Gallery!")
    while True:
        print("Type 'list' to browse artworks, type 'view' for the details, type 'comment' to add a comment or 'like' to like the artwork")

        user_type = input().strip().lower()
        if user_type == "list":
            list_artworks()
        elif user_type == "view":  
            art_id = input("type the art id: ")
            artwork_details(int(art_id))
        elif user_type == "comment":
            art_id = input("type the art id: ")
            type_comment = input("type your comment: ")
            comment_artwork(int(art_id),type_comment)
        elif  user_type == "like":
            art_id = input("type the art id: ")
            like_artwork(int(art_id))
        elif user_type == "exit":
            print("Thank you!")
            break
        else:
            print("Invalid. Try again!")    
main()               
