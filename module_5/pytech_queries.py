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

for doc in docs:
    print(doc)
    
# display a single document by student_id
print(students.find_one({"student_id": "1007"}))