import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["library"]

books = db["books"]

title = "Java Programming"
books.delete_one({"Title": title})
print(f"Deleted book: {title}")

print(f"\n All Books")
for book in books.find():
    print(book)