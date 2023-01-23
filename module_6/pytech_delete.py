"""
Cory Thomaier
1/22/2023
CYBR410-T301 Data/Database Security (2233-1)
Assignment: PyTech: Deleting Documents
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

# create new student for id 1010, first name, last name, and student id
james = {
        "student_id": "1010",
        "first_name": "James",
        "last_name": "Dory"
    }
#insert student into students
james_student_Id = students.insert_one(james).inserted_id

# display a single document by student_id
print("-- DISPLAYING STUDENT DOCUMENT 1010 --")
print(students.find_one({"student_id": "1010"}))

#delete student 1010
result = db.students.delete_one({"student_id":"1010"})

# display all documents in the collection
docs = students.find()
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print(doc)