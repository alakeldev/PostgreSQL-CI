from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instrunctions from our localhost "chinook" database
# The reason of /// that signifies that our database is hosted locally within our workspace environment
# db = create_engine("postgresql:///chinook")   => this one from the CI video but it's not working 

#  create_engine('postgresql://yourusername:yourpassword@localhost:5432/chinook')
db = create_engine('postgresql://postgres:abdullah@localhost:5432/chinook')


# Metadata class will contain collection of our table objects, and the associated data within this objects => it's recursive data about data
# meaning the data about our tables and the data about the data in those tables ===>> META
meta = MetaData(db)

# Create Variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)


# Create Variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)


# Create Variable For "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("albumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)

)

# making the connection
with db.connect() as connection:
    # Query 1 - Select All records from the "Artist" Table
    # select_query = artist_table.select()

    # Query 2 - Select only the "name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])  ## here using with_only_columns method even if you want to grab results from a single column you need to wrap the column section inside of a list [] ----- .c meaning and identify a specific column header on the table
    
    # Query 3 - Select only "Queen" from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - Select only by "ArtistId" 51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - Select only the albums with "ArtistId" 51 on the "album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - Select all tracker where the composer is "Queen" from the "Track" table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")  ## here there is and error you mmust search about it to know why !!!!!!




    results = connection.execute(select_query)
    for result in results:
        print(result)

