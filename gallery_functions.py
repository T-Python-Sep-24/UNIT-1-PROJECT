import json

ARTWORK_FILE = 'data/artworks.json'

def load_artworks():
    with open(ARTWORK_FILE, 'r') as f:
        return json.load(f)

def save_artworks(artworks):
    with open(ARTWORK_FILE, 'w') as f:
        json.dump(artworks, f, indent = 4)

def list_artworks():
    artworks = load_artworks()
    for artwork in artworks:
        print(f"ID: {artwork['id']}")
        print(f"Title: {artwork['title']}")
        print(f"Artist: {artwork['artist']}")
        print(f"Year: {artwork['year']}")
        print()  

def artwork_details(art_id):
    artworks = load_artworks()
    art_id = int(art_id)
    for artwork in artworks:
        if artwork['id'] == art_id: 
            print(f"Title: {artwork['title']}")
            print(f"Artist: {artwork['artist']} ({artwork['year']})")
            print(f"Description: {artwork['description']}")
            print(f"Likes: {artwork['likes']}")
            print(f"comment: {artwork['comments']}")
            break
    else:
        print("Art not found!") 
        
def like_artwork(art_id):
    art_id = int(art_id)
    artworks = load_artworks()
    for artwork in artworks:
        if artwork['id'] == art_id: 
            artwork['likes'] += 1
            save_artworks(artworks)
            print(f"You liked '{artwork['title']}'. Total Likes: {artwork['likes']}")
            break
        else:
            print("Art not found!") 

def comment_artwork(art_id, type_comment):
    art_id = int(art_id)
    artworks = load_artworks()
    for artwork in artworks:
        if artwork['id'] == art_id: 
            artwork['comments'].append(type_comment)
            save_artworks(artworks)
            print(f"Comment added to '{artwork['title']}'.")
            break
        else:
            print("Art not found!")    