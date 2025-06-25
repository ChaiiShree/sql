# main.py

import os
from dotenv import load_dotenv
from scripts.clean_transform import clean_accident_data
from sqlalchemy import create_engine

load_dotenv()

def main():
    print("🚀 Starting ETL process...")

    df = clean_accident_data("data/US_Accidents_Dataset.csv")
    print(f"✅ Cleaned dataset with {len(df)} rows.")

    db_url = os.getenv("DATABASE_URL")
    engine = create_engine(db_url)
    df.to_sql("accidents", con=engine, if_exists="replace", index=False)

    print("✅ Data successfully inserted into the database!")

if __name__ == "__main__":
    main()
