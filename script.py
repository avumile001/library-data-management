import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine(
    "mysql+pymysql://root:Avumile%40123@localhost:3306/librarydb"
)

# Read CSV files
books = pd.read_csv("books.csv")
members = pd.read_csv("members.csv")
loans = pd.read_csv("loans.csv")

# Load into database
books.to_sql("books", engine, if_exists="append", index=False)
members.to_sql("members", engine, if_exists="append", index=False)
loans.to_sql("loans", engine, if_exists="append", index=False)

print("Data loaded successfully!")