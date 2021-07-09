# Import required packages

import pymongo
import json
import dateutil.parser

#Connecting with MongoClient
client=pymongo.MongoClient('localhost',27017)

# Creating databases object
db = client["meals"]  

#Creating Collection
#db.create_collection("Meal_Information")

#  Insert Many
db.Meal_Information.insert_many(json_data)  # Insert json data to database


# Find
doc = {"cuisine": input("enter cuisine ")}

# Find all documents from collection
for i in db.Meal_Information.find(doc):
    print(i)


# Find One
doc = {"meal_id": int(input("enter meal_id "))}

print(db.Meal_Information.find_one(doc))


# Limit
for i in db.info.find().limit(10):
    print(i)


# Update One
doc = {"meal_id": int(input("enter meal_id "))}
update = {"$set": {"category": input("enter category to be changed ")}}

db.Meal_Information.update_one(doc, update)

print(db.Meal_Information.find_one(doc))


# Update Many
doc = {"cuisine": input("enter cuisine ")}
update = {"$set": {"category": input("enter category to be changed ")}}

db.Meal_Information.update_many(doc, update)

for i in db.Meal_Information.find(doc):
    print(i)


# Drop
db.Meal_Information.drop()
for i in db.Meal_Information.find({}):
    print(i)


# Delete One
doc = {"meal_id": int(input("enter meal_id "))}

db.Meal_Information.delete_one(doc)

for i in db.Meal_Information.find({}):
    print(i)


# Delete Many
doc = {"category": input("enter category ")}

db.Meal_Information.delete_many(doc)

for i in db.Meal_Information.find({}):
    print(i)


# Insert One
meal_id = int(input("enter meal id "))
doc = {
    "meal_id": meal_id,
    "category": input("enter category"),
    "cuisine": input("enter cuisine")
}

db.Meal_Information.insert_one(doc)
print(db.Meal_Information.find_one({"meal_id": meal_id}))


# Insert Many
docs = []
for i in range(int(input("number of meals "))):
    doc = {
        "meal_id": int(input("enter meal id ")),
        "category": input("enter category "),
        "cuisine": input("enter cuisine ")
    }
    docs.append(doc)

ids = db.Meal_Information.insert_many(docs)
for i in db.Meal_Information.find({}):
    print(i)


# Inserted Id
print(ids.inserted_ids)




for i in db.Meal_Information.find({}, {"_id": 1}):
    print(i["_id"])


# Sort
for i in db.Meal_Information.find().sort("meal_id", 1):
    print(i)
