# transform phase
import pandas as pd

# pokemon dataframe
pokemon_df = pd.read_csv('data/raw_pokemon_data.csv')

# type dataframe
type_df = pd.read_csv('data/raw_type_data.csv')

# check the data types
#print(pokemon_df.info())

# rename columns
pokemon_df.rename(columns={"pokemon_name": "name",
                           "pokemon_base_exp": "base_experience",
                           "pokemon_height": "height_in_meters",
                           "pokemon_weight": "weight_in_kg",
                           "pokemon_hp": "hp",
                           "pokemon_atk": "attack",
                           "pokemon_def": "defense",
                           "pokemon_sp_atk": "special_attack",
                           "pokemon_sp_def": "special_defense",
                           "pokemon_speed": "speed",
                           "pokemon_type_1": "primary_type",
                           "pokemon_type_2": "secondary_type",
                           "p_species_gender_rate": "gender_rate",
                           "p_species_capture_rate": "capture_rate",
                           "p_species_base_happiness": "base_happiness",
                           "p_species_is_baby": "is_baby",
                           "p_species_is_legendary": "is_legendary",
                           "p_species_is_mythical": "is_mythical",
                           "p_species_color": "color",
                           "p_species_shape": "shape",
                           "p_species_gen": "generation"
                          },
                          inplace=True)
# total stats column
stats_columns = ["hp", "attack", "defense", "special_attack", "special_defense", "speed"]

# convert to float
pokemon_df[stats_columns] = pokemon_df[stats_columns].astype(float)

# sum across the columns
pokemon_df["total_stats"] = pokemon_df[stats_columns].sum(axis=1)


# normalize data
num_cols = ["pokemon_id", "base_experience", "height_in_meters", "weight_in_kg", "gender_rate", "capture_rate", "base_happiness"]
pokemon_df[num_cols] = pokemon_df[num_cols].astype(float)

str_cols = ["name", "primary_type", "secondary_type", "color", "shape", "generation"]
pokemon_df[str_cols] = pokemon_df[str_cols].astype(str)

type_cols = ["type_name", "relation", "target_type"]
type_df[type_cols] = type_df[type_cols].astype(str)

for col in str_cols:
  pokemon_df[col] = pokemon_df[col].str.lower()

for col in type_cols:
  type_df[col] = type_df[col].str.lower()


# additional cleaning
# height
pokemon_df["height_in_meters"] = pokemon_df["height_in_meters"] / 10

# weight
pokemon_df["weight_in_kg"] = pokemon_df["weight_in_kg"] / 10

# type 2
pokemon_df["secondary_type"] = pokemon_df["secondary_type"].replace('nan', None)

# gender rate
pokemon_df["gender_rate"] = round(pokemon_df["gender_rate"] / 8, 2)
pokemon_df["gender_rate"] = pokemon_df["gender_rate"].replace(-0.12, -1)

# capture rate
pokemon_df["capture_rate"] = round(pokemon_df["capture_rate"] / 255, 2)

# generation
pokemon_df["generation"] = pokemon_df["generation"].map({"generation-i" : "Gen 1",
                                                         "generation-ii" : "Gen 2",
                                                         "generation-iii" : "Gen 3",
                                                         "generation-iv" : "Gen 4",
                                                         "generation-v" : "Gen 5",
                                                         "generation-vi" : "Gen 6",
                                                         "generation-vii" : "Gen 7",
                                                         "generation-viii" : "Gen 8",
                                                         "generation-ix" : "Gen 9"})


# save cleaned pokemon data
pokemon_df.to_csv("data/clean_pokemon_data.csv", index=False)
print("Cleaned Pokémon data saved!")

# save cleaned type data
type_df.to_csv("data/clean_type_data.csv", index=False)
print("Cleaned Type data saved!")

# pokemon_df.head()
# print(pokemon_df.info())
# pokemon_df.describe()