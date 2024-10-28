import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")


db = client['library']

books = db['books']

book1 = {
    "Title":"C++ Programming",
    "Price": 1500.00
    }

book2 = {
    "Title":"Java Programming",
    "Price": 100.00
    }

books.insert_many([book1, book2])

print("Books Inserted...")