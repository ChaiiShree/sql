# 🚦 US Traffic Accidents: ETL & PostgreSQL Analysis Pipeline

A complete data engineering and analytics project using the **US Accidents dataset**, covering extraction, transformation, and loading into a PostgreSQL database, followed by SQL-based analysis and Python-powered visualizations.

---

## 📁 Project Structure

```
TrafficAccidents-ETL-Analysis/
├── data/                      # Raw dataset (ignored in Git)
├── database/
│   ├── create_schema.sql      # Table schema for PostgreSQL
│   └── insert_data.py         # CSV-to-Postgres script
├── scripts/
│   └── clean_transform.py     # ETL transformation script
├── notebooks/
│   ├── exploratory_analysis.ipynb  # All 10 visual plots
│   └── advanced_queries.ipynb     # Raw SQL insights
├── visualizations/            # Saved plots
├── main.py                    # Runs the full ETL pipeline
├── requirements.txt           # Python dependencies
├── .env                       # DB credentials (excluded from Git)
└── README.md                  # Project overview
```

---

## 🗃️ Dataset

* **Source:** [Kaggle: US Accidents (2016–2023)](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)
* **Size:** 7+ million rows
* **Fields include:**

  * Start/End Time
  * Severity
  * City, State
  * Weather Condition
  * Visibility, Temperature, Wind Speed
  * Accident Duration (calculated)

---

## 🧪 ETL Pipeline

* 📥 **Extract:** CSV loaded using Pandas
* 🧹 **Transform:** Cleaned nulls, calculated accident duration, converted timestamps
* 🏗️ **Load:** Inserted into PostgreSQL using SQLAlchemy

Run the full pipeline:

```bash
python main.py
```

---

## 📊 Exploratory Visualizations

Stored in the `notebooks/visualizations/` folder and generated via Jupyter:

1. **Accidents by State**

   ![Accidents by State](notebooks/visualizations/accidents_by_state.png)

2. **Severity Distribution**

   ![Severity Distribution](notebooks/visualizations/severity_distribution.png)

3. **Accident Duration Histogram**

   ![Accident Duration Histogram](notebooks/visualizations/accident_duration_hist.png)

4. **Top Cities by Accidents**

   ![Top Cities by Accidents](notebooks/visualizations/top_cities.png)

5. **Weather Conditions by State**

   ![Weather Conditions by State](notebooks/visualizations/weather_by_state.png)

6. **Hourly Accident Distribution**

   ![Hourly Accident Distribution](notebooks/visualizations/hourly_distribution.png)

7. **Weekday vs Weekend Accidents**

   ![Weekday vs Weekend Accidents](notebooks/visualizations/weekday_vs_weekend.png)

8. **Monthly Average Duration**

   ![Monthly Average Duration](notebooks/visualizations/avg_duration_by_month.png)

9. **Severity by Weather Condition**

   ![Severity by Weather Condition](notebooks/visualizations/severity_by_weather.png)

10. **Wind Speed vs Severity**

    ![Wind Speed vs Severity](notebooks/visualizations/wind_speed_vs_severity.png)


---

## 🧠 Deeper SQL Queries

Found in `notebooks/advanced_queries.ipynb`:

* Top cities with most accidents
* Average duration per state
* Severity × Weather correlation
* Time-based aggregations (hour, weekday, month)
* Weather/visibility/wind effect on severity

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Database:** PostgreSQL
* **Libraries:** Pandas, SQLAlchemy, Matplotlib, Seaborn, Dotenv
* **Notebook:** Jupyter

---

## 📦 Setup Instructions

1. Clone repo:

   ```bash
   git clone https://github.com/ChaiiShree/sql.git
   cd TrafficAccidents-ETL-Analysis
   ```

2. Create `.env` file:

   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/dbname
   ```

3. Set up environment:

   ```bash
   python -m venv venv
   venv/Scripts/activate  # On Windows
   pip install -r requirements.txt
   ```

4. Download dataset from Kaggle into `data/`

5. Run ETL:

   ```bash
   python main.py
   ```

6. Launch notebooks:

   ```bash
   jupyter notebook
   ```

## 📄 License

This project is licensed under the MIT License.
Dataset credit: © [Kaggle – US Accidents](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)
