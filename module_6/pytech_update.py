"""
Cory Thomaier
1/22/2023
CYBR410-T301 Data/Database Security (2233-1)
Assignment: PyTech: Updating Documents
"""
import certifi
from pymongo import MongoClient
#I had a ssl error, this takes care of that error
ca = certifi.where()

# assign a pymongo client
client = MongoClient("mongodb+srv://admin:admin@cluster0.uizza3d.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)

# call the database
db = client["pytech"]

# assign the collection
students = db["students"]

# display all documents in the collection
docs = students.find()

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
    print(doc)

#update the name for student id 1007
result = db.students.update_one({"student_id":"1007"}, {"$set": {"last_name":"Smith"}})

# display a single document by student_id
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
print(students.find_one({"student_id": "1007"}))