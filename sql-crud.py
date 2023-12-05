from sqlalchemy import (
    create_engine, Column, Float, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Executing the instructions from the "chinook" database
db = create_engine('postgresql://postgres:abdullah@localhost:5432/chinook')

# this new base class will essentially grab the metadata that is produced by our database table schema, and create a subclass to map everthing back to use here within the base variable
base = declarative_base()



# Create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)












# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)

# open an actual session by calling the Session() subclass defind above
session = Session()


# Creating the database using declarative_base subclass to generate all the metadata
base.metadata.create_all(db)




# Creating records on our Programmer table
ada_lovelace = Programmer(
        first_name = "Ada",
        last_name = "Lovelace",
        gender = "F",
        nationality = "British",
        famous_for = "First Programmer"
)



alan_turing = Programmer(
        first_name = "Alan",
        last_name = "Truing",
        gender = "M",
        nationality = "British",
        famous_for = "Modern Computing"
)




grace_hopper = Programmer(
        first_name = "Grace",
        last_name = "Hopper",
        gender = "F",
        nationality = "American",
        famous_for = "COBOL Language"
)


margaret_hamilton = Programmer(
        first_name = "Margaret",
        last_name = "Hamilton",
        gender = "F",
        nationality = "American",
        famous_for = "Apollo 11"
)


bill_gates = Programmer(
        first_name = "Bill",
        last_name = "Gates",
        gender = "M",
        nationality = "American",
        famous_for = "Microsoft"
)


tim_berners_lee = Programmer(
        first_name = "Tim",
        last_name = "Berners-Lee",
        gender = "M",
        nationality = "British",
        famous_for = "World Wide Web"
)


abdullah_alakel = Programmer(
        first_name = "Abdullah",
        last_name = "Alakel",
        gender = "M",
        nationality = "Syrian",
        famous_for = "IT Eng. and software Developer"
)




########################################################### 1
# Add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(abdullah_alakel)


# # Commit our session to the database 
# session.commit()



######################################################### 2 
# Updating single record
# programmer = session.query(Programmer).filter_by(id=7).first()    # if you don't use .first() method so must use for loop to iterate on the records
# ## Here define which column that we want to update
# programmer.famous_for = "World President"


# # # Commit our session to the database 
# session.commit()



# Updating Multiple records     ## I have issue it didn't update the multiple records must check it again later
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender == "Female"
#     elif person.gender == "M":
#         person.gender == "Male"
#     else:
#         print("Gender Not Defined")
#     session.commit()




# # Deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")

# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()

# # defensive programming
# if programmer is not None:
#     print("Progammer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are You Sure You want to Delete this Record? y/n")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted!")
#     else:
#         print("Pgrammer Not Deleted")
# else:
#     print("No records Found!!!")




# # delete Multiple recrods
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()



# Query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )