# Import required packages

import pymongo
import json
pymongo import MongoClient



#Connecting with MongoClient

client = MongoClient('localhost',27017)  


# Creating databases object

db = client["meals"]  


#Creating Collection

db.create_collection("Meal_Information")



#  Insert Many


db.info.insert_many(json_data)  # Insert json data to database


# # Find


doc = {"cuisine": input("enter cuisine ")}

# Find all documents from collection
for i in db.info.find(doc):
    print(i)


# # Find One


doc = {"meal_id": int(input("enter meal_id "))}

print(db.info.find_one(doc))


# # Limit


for i in db.info.find().limit(10):
    print(i)


# # Update One



doc = {"meal_id": int(input("enter meal_id "))}
update = {"$set": {"category": input("enter category to be changed ")}}

db.info.update_one(doc, update)

print(db.info.find_one(doc))


# # Update Many



doc = {"cuisine": input("enter cuisine ")}
update = {"$set": {"category": input("enter category to be changed ")}}

db.info.update_many(doc, update)

for i in db.info.find(doc):
    print(i)


# # Drop



db.info.drop()
for i in db.info.find({}):
    print(i)


# # Delete One



doc = {"meal_id": int(input("enter meal_id "))}

db.info.delete_one(doc)

for i in db.info.find({}):
    print(i)


# # Delete Many


doc = {"category": input("enter category ")}

db.info.delete_many(doc)

for i in db.info.find({}):
    print(i)


# # Insert One


meal_id = int(input("enter meal id "))
doc = {
    "meal_id": meal_id,
    "category": input("enter category"),
    "cuisine": input("enter cuisine")
}

db.info.insert_one(doc)
print(db.info.find_one({"meal_id": meal_id}))


# # Insert Many


docs = []
for i in range(int(input("number of meals "))):
    doc = {
        "meal_id": int(input("enter meal id ")),
        "category": input("enter category "),
        "cuisine": input("enter cuisine ")
    }
    docs.append(doc)

ids = db.info.insert_many(docs)
for i in db.info.find({}):
    print(i)


# # Inserted Id


print(ids.inserted_ids)




for i in db.info.find({}, {"_id": 1}):
    print(i["_id"])


# # Sort



for i in db.info.find().sort("meal_id", 1):
    print(i)
