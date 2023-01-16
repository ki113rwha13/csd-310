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

# create 3 students, first name, last name, and student id

cory = {
        "student_id": "1007",
        "first_name": "Cory",
        "last_name": "Thomaier"
    }
rachel = {
        "student_id": "1008",
        "first_name": "Rachel",
        "last_name": "Thomaier"
    }
duchess = {
        "student_id": "1009",
        "first_name": "Duchess",
        "last_name": "Lady"
    }


#insert each record into the collection

cory_student_Id = students.insert_one(cory).inserted_id
rachel_student_Id = students.insert_one(rachel).inserted_id
duchess_student_Id = students.insert_one(duchess).inserted_id

print(cory_student_Id)
print(rachel_student_Id)
print(duchess_student_Id)