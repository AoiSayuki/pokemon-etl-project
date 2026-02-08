Pokémon Data Analytics Pipeline (ETL)
📋 Project Overview
This project demonstrates a full ETL (Extract, Transform, Load) pipeline that processes data for all 1,025 Pokémon across 9 generations. The goal was to move beyond a simple "Pokedex" and create a Business Intelligence Dashboard that analyzes Pokémon species as "assets," comparing performance metrics, type efficiencies, and generational trends.

🛠️ Tech Stack
Language: Python 3.x

Libraries: Pandas (Data Manipulation), SQLAlchemy (Database Connection)

Database: SQLite

Visualization: Power BI

Data Source: PokeAPI (Raw CSV exports)

⚙️ The ETL Process
1. Extract
Raw data was sourced in CSV format, containing detailed base stats, dimensions, and taxonomic classifications for every Pokémon, along with a separate dataset for elemental type relations (Strengths/Weaknesses).

2. Transform
Using Pandas, the data underwent rigorous cleaning to ensure it was "dashboard-ready":

Standardization: Converted height and weight to metric units (meters/kg).

Normalization: Lowercased all string values for consistency.

Feature Engineering: * Calculated total_stats (BST).

Mapped generation IDs to readable labels (e.g., "Gen 1").

Normalized capture_rate and gender_rate to decimal scales.

Data Integrity: Handled missing values (NaN) in dual-type Pokémon to ensure accurate SQL joins.

3. Load
The cleaned data was programmatically loaded into a SQLite database (pokemon_db.db) using SQLAlchemy. This ensures the data is structured, indexed, and ready for relational queries or BI tool integration via ODBC.

📊 Dashboard Insights
The final Power BI dashboard focuses on high-level distribution and comparative analysis rather than individual entries:

KPIs: Total Species, Average Base Stat Total (BST), Type Diversity.

Generational Analysis: A Bar Chart comparing how average power levels have shifted from Gen 1 to Gen 9.

Stat Distribution: Box Plots showing the spread of Total Stats across different Primary Types.

Correlation: A Scatter Plot exploring the relationship between Weight and Physical Stats (Attack/Defense).

Type Strategy: A condensed Heatmap identifying the most (and least) effective type matchups.

📁 Project Structure
├── data/
│   ├── raw_pokemon_data.csv       # Original data
│   ├── clean_pokemon_data.csv     # Transformed data
│   └── clean_type_data.csv        # Processed type relations
├── db/
│   └── pokemon_db.db              # Final SQLite Database
├── scripts/
│   ├── transform_script.py        # Pandas cleaning logic
│   └── load_script.py             # SQLAlchemy loading logic
├── dashboard/
│   └── pokemon_analytics.pbix     # Power BI Dashboard file
└── README.md
🚀 How to Run
Clone the repository.

Install dependencies: pip install pandas sqlalchemy.

Run the scripts:

Execute the transformation script to generate the clean CSVs.

Execute the load script to populate the SQLite database in the /db folder.

Connect to Power BI: * Open the .pbix file.

Update the ODBC DSN to point to your local pokemon_db.db file.
