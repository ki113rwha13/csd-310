'''
Cory Thomaier
CYBR410-T301 Data/Database Security (2233-1)
2/5/2023
Assignment: PySports: Table Queries

Create a new file under the module_8 directory and name it pysports_queries.py.
Write the code to connect to your MySQL pysports database.
Refer to the previous assignment for code structure.
You can basically copy/paste the code we used in the previous assignment, assuming you were able to get it to work.
Write two select queries, one for the team table and one for the player table.
SELECT team_id, team_name, mascot FROM team.
Using a for loop, iterate over the cursor and display the results.
Make sure your output matches the expected output below (this is gradable).
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
query_team = "SELECT team_id, team_name, mascot FROM team"
query_player = "SELECT player_id, first_name, last_name FROM player"

#perform query team
cursor.execute(query_team)

#for loop team
print("-- DISPLAYING TEAM RECORDS --")
for team in cursor:
    print(team)

#close the cursor team
cursor.close

#perform query player
cursor.execute(query_player)

#for loop player
print("-- DISPLAYING PLAYER RECORDS --")
for player in cursor:
    print(player)    

#close cursor player
cursor.close

#close the DB
db.close()

