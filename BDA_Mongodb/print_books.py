import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["library"]

books = db["books"]

print("All Books")

for book in books.find():
    print(book)

title = "C++ Programming"
print(f"\n Book titled {title}")
for book in books.find({"Title": title}):
    print(book)