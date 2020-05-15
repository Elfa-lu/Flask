# Import: 
# Provided for you in this project is a file called books.csv, which is a spreadsheet in CSV format of 5000 different books.
# Each one has an ISBN number, a title, an author, and a publication year. 

# write a program that will take the books and import them into your PostgreSQL database. 
# You will first need to decide what table(s) to create, what columns those tables should have, 
# and how they should relate to one another. 

import os, csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

file = open("books.csv")
reader = csv.reader(file)

for isbn, title, author, year in reader:
	db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
				{"isbn":isbn, "title":title, "author":author, "year":year})
	db.commit()