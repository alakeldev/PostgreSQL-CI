- POSTGRES

- PSYCOPG2 python (library to connect python with postgres)

- PYTHONIC method when working with postgres using something called ORM

ORM = Object Relational Mapping => Method to query and manupulate data from data base using Objects

Object => the object that you use from the programming language => python
Relational => the relational database that is being used => PostgreSQL
Mapping => the bridge between Python object and the tables within the databas, mapping the two together

** The most Popular ORM libraries when working with Python are the Django ORM and SQLAlchemy connecting with PostgreSQL

- Django includes its own ORM which is extremely popular but cannot be decoupled from the Django framework to be used on its own
- SQLAlchemy is build to be framework agnostic, and so can therefore be used on its own

Some of the best reasons to use SQLAlchemy isclude having cleaner code, the logic is simple and your code is more secure than using raw SQL commands.
SQLAlchemy library comes with three different layers of abstraction mean you can choose the level of support necessary for your application:

- 1 The lowest Layer of abstraction is simply use SQLAlchemy's engine component in order to execute raw SQL 
- 2 The middle Layer of abstraction uses SQLAlchemy's Expression language to build SQL statements in more PYthonic way instead of relying purely on thos raw strings 
- 3 The highest Layer of abstraction uses SQLAlchemy's full ORM capabilites, allowing us to make use of python classes and objects, instead of using database tables and connections


The summary of above is:
(1) Raw SQL commands => (2) Basic Python Syntax => (3) Python Classes and Objects



Class Based Models:
Class is a collection of methods that serve a common purpose with each method having its own purpose.
Mthods themselves should only do one thing, having only one purpose, if its starts to do too much, them you should ideally split it into different methods

Examples for methods that we already used:

- with db.connect() as connection:  ===>>>> connect() to connect to database
- select_query = artist_table.select() ====>>>> select() to make a selection from the database
- results = connection.execute(select_query) ====>>> execute() to perform  the execution of the query


Class-Based models has many benefits such as it helps to keep your code clean and modular and you can use methods throughout an application without repeating your self   (SQLAlchemy ORM)



Important to know inside SQlAlchemy the difference between 
Expression Language: SQLAlchemy's core component Focus on tables (sql-expression.py)
ORM: SQLAlchemy's full ORM class based models (sql-orm.py)




CRUD Functionality: Using ORM
CREATE
READ
UPDATE
DELETE






to update the pip on my machine:
open the CLI and write below:
python -m pip install --upgrade pip

Important note to understand:
    
        the difference between {%%} and {{}} 
        {{}} contain an expression which is outputting something either onto the screen or in this case in to our href
        {%%} for statments that control the flow of our template such as a for loopm if statement of this block element
   