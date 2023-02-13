'''
Cory Thomaier
CYBR410-T301 Data/Database Security (2233-1)
2/11/2023
Assignment: PySports: Basic Table Joins

Create a new directory under csd-310 and name it module_9.
Create a new file under the module_9 directory and name it pysports_join_queries.py.
Add the appropriate Python code to connect to the pysports database.
Using the output I have provided and the sample queries, create an INNER JOIN query to connect the player and team tables by team_id and display the results.
Make sure your output matches the Expected Output.
'''
import mysql.connector
from mysql.connector import errorcode
#Connect to database
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\n   Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

#Create a cursor
cursor = db.cursor()

#create the query
query_innerJoin = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"

#perform query 
cursor.execute(query_innerJoin)

#for loop 
print("-- DISPLAYING PLAYER RECORDS --")
for team in cursor:
    print(team)

#close cursor 
cursor.close

#close the DB
db.close()