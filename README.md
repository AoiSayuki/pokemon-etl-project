# Pokémon Data Analytics Pipeline (ETL)
## 📋 Project Overview
This project demonstrates a full ETL (Extract, Transform, Load) pipeline that processes data for all 1,025 Pokémon across 9 generations. The goal was to analyze Pokémon species as "assets," comparing performance metrics, type efficiencies, and generational trends.

## 🛠️ Tech Stack
- Language: Python 3.x
- Libraries: Pandas (Data Manipulation), SQLAlchemy (Database Connection)
- Database: SQLite
- Visualization: Power BI
- Data Source: PokeAPI (Raw CSV exports)

## ⚙️ The ETL Process
1. Extract
- Raw data was sourced in CSV format, containing detailed base stats, dimensions, and classifications for every Pokémon, along with a separate dataset for elemental type relations (Strengths/Weaknesses).

2. Transform
- Using Pandas, the data underwent rigorous cleaning to ensure it was "dashboard-ready":
  - Standardization: Converted height and weight to metric units (meters/kg).
  - Normalization: Lowercased all string values for consistency.
  - Feature Engineering: Calculated total_stats.
  - Mapped generation IDs to readable labels (e.g., "Gen 1").
  - Normalized capture_rate and gender_rate to decimal scales.
  - Data Integrity: Handled missing values (NaN) in dual-type Pokémon to ensure accurate SQL joins.
  
3. Load
- The cleaned data was programmatically loaded into a SQLite database (pokemon_db.db) using SQLAlchemy. This ensures the data is structured, indexed, and ready for relational queries or BI tool integration via ODBC.

## 📊 Dashboard Insights
- The final Power BI dashboard focuses on high-level distribution and comparative analysis rather than individual entries:
  - KPIs: Total Species, Average Base Stat Total (BST), Average Capture Rate.
  - Generational Analysis: A Line Chart comparing the number of Pokémon added Gen 1 to Gen 9.
  - Stat Distribution: Bar Chart showing the spread of Total Stats across different Primary Types.

## 📁 Project Structure
```
├── data/
│   ├── raw_pokemon_data.csv       # Original pokemon data
│   ├── raw_type_data.csv          # Original type data
│   ├── clean_pokemon_data.csv     # Transformed data
│   └── clean_type_data.csv        # Processed type relations
├── db/
│   └── pokemon_db.db              # Final SQLite Database
├── scripts/
│   ├── extract_pokemon.py         # Pokemon collection script
│   ├── extract_type_relations.py  # Type collection script
│   ├── transform_script.py        # Pandas cleaning logic
│   └── load_script.py             # SQLAlchemy loading logic
├── dashboard/
│   └── pokemon_analytics.pbix     # Power BI Dashboard file
└── README.md
```

## 🚀 How to Run
1. Clone the repository.
2. Install dependencies:
  - pip install pandas sqlalchemy.
3. Run the scripts:
  - Execute the transformation script to generate the clean CSVs.
  - Execute the load script to populate the SQLite database in the /db folder.
4. Connect to Power BI:
  - Open the .pbix file.
5. Update the ODBC DSN to point to your local pokemon_db.db file.


