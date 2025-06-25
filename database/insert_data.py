import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from scripts.clean_transform import clean_accident_data

load_dotenv()

def insert_to_db():
    df = clean_accident_data('data/US_Accidents_Dataset.csv')

    db_url = os.getenv("DATABASE_URL")  # Example: postgresql://user:pass@localhost:5432/accidents
    engine = create_engine(db_url)

    df.to_sql('accidents', con=engine, if_exists='replace', index=False)
    print("Data successfully inserted into PostgreSQL database.")

if __name__ == '__main__':
    insert_to_db()