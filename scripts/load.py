import pandas as pd
from sqlalchemy import create_engine

# load dataframes
df_pokemon = pd.read_csv('data/clean_pokemon_data.csv')
df_type = pd.read_csv('data/clean_type_data.csv')

# create engine
engine = create_engine("sqlite:///pokemon_db.db")

# load data into sqlite database
df_pokemon.to_sql("pokemon", con=engine, if_exists="replace", index=False)
df_type.to_sql("type_relations", con=engine, if_exists="replace", index=False)

# disconnect engine
engine.dispose()

print("Successfully loaded data into the database!")