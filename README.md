# MEAL_DELIVERY_COMAPNY

BY Ashish Kumar

# Service Function
1. SEARCH MEAL_ID INFORMATION BU MEAL_ID
2. DIFFERENT ORDERS AS PER _ID'S
3. FILETRING THE DATA AS PER THE MEAL_ID.

# PROBLEM DESCRIPTION

Meal delivery system filter the data by using the in built operation.

DATABASE

1.Mongodb Compass

2.MYSQL

# REQUIREMENT AND TECH STACK

1.Python

2.data in json file

3.MongoDB is implemented python libraries need for connecting are pymongo,json,pprint,json,warnings.

4.Jupyter



# PYMONGO QUERIES
. USE MONGODB FOR NO SQL DATABASE 

. USE PYMONGO FOR CONNECTING NOSQL WITH PYTHON

# RESTAPI design:
. IMPORTING THE PACKAGES BY USING PYMONGO 

. CONNECTING IT WITH PYTHON


# CONNECTING IT WITH CLIENT

1. Creating a Database

/DATABASE CREATED /

database=client["database_name"]

2. INSERTING THE MANY RECORDS

/ COLLECTION.INSERT()_MANY /


collection.insert_many()

3. inserting_one_data

/ COLLECTION.INSERT()_ONE /

result=collection.insert_one(insrt)

4. Finding the meal_id

/ FINDING THE MEAL_ID BY APROPRIATE ID /

collection.find_one({'meal_id':1010})


5. Deleting one record

/ DELETING ONE RECORD /

COLLECTION.DELETE_ONE()

6. Displaying limit of the database upto 3

/ DISPLAYING THE LIMITS UPTO DEFINED VALUE/

COLLECTION.FIND().LIMIT(6)

7. sorting in ascending order

/ SORTING THE DATA /

COLLECTION.FIND().SORT()

8. update_one

/UPDATING THE QUERY IN THE DATABASES/

COLLECTION.UPDATE_ONE({"ID":123},{"$SET":{"NAME":"Ashish"})

9. UPDATE MANY

/ UPDATE MANY UPADTE THE VALUES IN THA DATABASE /

COLLECTION.UPDATE_MANY({},{"$SET":{"NAME":"Ashish"})