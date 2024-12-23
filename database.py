from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:root%40123@localhost:5432/pizza_delivery"

# Create the engine
engine = create_engine(DATABASE_URL)

# Test the connection
try:
    with engine.connect() as connection:
        print("Database connected successfully!")
except Exception as e:
    print(f"Error connecting to the database: {e}")


# Provides the schema for your database by defining models (tables).
# Used to map Python classes to database tables.
# Define a base class for models
Base = declarative_base()


# Facilitates database operations (queries, transactions) by managing sessions.
# Ensures safe and efficient communication with the database.
# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)