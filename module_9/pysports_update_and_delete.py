'''
Cory Thomaier
CYBR410-T301 Data/Database Security (2233-1)
2/11/2023
Assignment: PySports: Update & Deletes

Create a new file under the module_9 directory and name it pysports_update_and_delete.py.
Using the example code I provided, connect to the pysports database.
Using the example code I have provided, insert a new record into the player table for Team Gandalf.
team_id = 1
Using the example code I provided, execute a select query to display the player records (I want to verify the record was inserted successfully).
This query should include the INNER JOIN; I want to see the team_name field and not the team_id in the output window.
Using the example code I provided, update the newly inserted record by changing the player's team to Team Sauron.
team_id = 2
Using the example code I provided, execute a select query to display the updated record.
This query should include the INNER JOIN; I want to see the team_name field and not the team_id in the output window.
Using the example code I provided, execute a delete query to remove the updated record.
Using the example code I provided, execute a select query to display all the records in the player table.
This query should include the INNER JOIN; I want to see the team_name field and not the team_id in the output window.
Make sure your output matches the expected output (this is gradable.)
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

#create the querys
query_insert = "INSERT INTO player (first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1)"
query_innerJoin = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"
query_update = "UPDATE player SET team_id = 2 WHERE first_name = 'Smeagol'"
query_delete = "DELETE FROM player WHERE first_name = 'Smeagol'"
#perform insert query 
cursor.execute(query_insert)
#close cursor
cursor.close

cursor.execute(query_innerJoin)
#for loop showing records after insert
print("-- DISPLAYING RECORDS AFTER INSERT --")
for player in cursor:
    print(player)

#close cursor 
cursor.close
#update query
cursor.execute(query_update)
#close query
cursor.close

cursor.execute(query_innerJoin)
#for loop showing records after update
print("-- DISPLAYING RECORDS AFTER UPDATE --")
for player in cursor:
    print(player)

#close cursor 
cursor.close
#delete query
cursor.execute(query_delete)
#close cursor
cursor.close

cursor.execute(query_innerJoin)
#for loop showing records after delete
print("-- DISPLAYING RECORDS AFTER DELETE --")
for player in cursor:
    print(player)

#close cursor 
cursor.close

#close the DB
db.close()