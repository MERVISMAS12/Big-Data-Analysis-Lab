import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client['library']

books = db["books"]

title = "Java Programming"
price = 200
print(f"Updating the price of {title} to {price}")

books.update_one({"Title": title}, {"$set" : {"Price": price}})

print(f"Updated the price of {title} to {price}")

book = books.find_one({"Title": title})

print(book)