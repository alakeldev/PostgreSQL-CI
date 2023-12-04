import psycopg2


# Connect to Chinook Database
connection = psycopg2.connect(
    host="localhost",
    database="chinook",
    user="postgres",
    password="abdullah"
)

# Build Cursor Object of the Database Important to loop on the database
cursor = connection.cursor()

# Query 1 ==> Select All records from the "Artist" Table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 ==> Select only the "Name column from the "Artist" table 
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 ==> Select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])   # here you can use single result below it'S better

# Query 4 ==> Select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])    # here you can use single result below it'S better

# Query 5 ==> Select only the albums with "ArtistId" 51 on the album table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])   # Here use fetch all because multiple results you want

# Query 6 => Select all tracks where the composer is "Queen" from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])


#Query 7 => Select all tracks where the composer is "no" from the track table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["YOYOYO"])

# Fetch the results (Multiple)
results = cursor.fetchall()

# Fetch The result (Single)   if you want only a single result 
# results = cursor.fetchone()

# Close the Connection
connection.close()

# using for loop to loop and iterate on the results
for result in results:
    print(result)