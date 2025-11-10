# libraries used
import requests as r
import pandas as pd

# base url
base_url_pokemon = "https://pokeapi.co/api/v2/pokemon/"

# range for loop
# no_of_pokemon = r.get(base_url_pokemon).json()['count'] #number of pokemon
no_of_pokemon = 1025

# list for the data
all_pokemon_data = []

for i in range(1, no_of_pokemon + 1):
  # complete pokemon url
  pokemon_url = f"{base_url_pokemon}{i}"

  try:
    # API calls
    pokemon_data = r.get(pokemon_url)
    pokemon_data.raise_for_status()
    pokemon_json = pokemon_data.json()

    pokemon_species_url = 'No species for this pokemon'
    pokemon_species_url = pokemon_json.get('species').get('url')
    pokemon_species_data = r.get(pokemon_species_url)
    pokemon_species_data.raise_for_status()
    pokemon_species_json = pokemon_species_data.json()

    pokemon_info = {
      'pokemon_id' : pokemon_json['id'],
      'pokemon_name' : pokemon_json['name'],
      'pokemon_base_exp' : pokemon_json['base_experience'],
      'pokemon_height' : pokemon_json['height'],
      'pokemon_weight' : pokemon_json['weight'],
      'pokemon_hp' : pokemon_json['stats'][0]['base_stat'],
      'pokemon_atk' : pokemon_json['stats'][1]['base_stat'],
      'pokemon_def' : pokemon_json['stats'][2]['base_stat'],
      'pokemon_sp_atk' : pokemon_json['stats'][3]['base_stat'],
      'pokemon_sp_def' : pokemon_json['stats'][4]['base_stat'],
      'pokemon_speed' : pokemon_json['stats'][5]['base_stat'],
      'pokemon_type_1' : pokemon_json['types'][0]['type']['name'],
      'pokemon_type_2' : pokemon_json['types'][1]['type']['name'] if len(pokemon_json['types']) > 1 else None,

      # selected data from pokemon species
      'p_species_gender_rate' : pokemon_species_json['gender_rate'],
      'p_species_capture_rate' : pokemon_species_json['capture_rate'],
      'p_species_base_happiness' : pokemon_species_json['base_happiness'],
      'p_species_is_baby' : pokemon_species_json['is_baby'],
      'p_species_is_legendary' : pokemon_species_json['is_legendary'],
      'p_species_is_mythical' : pokemon_species_json['is_mythical'],
      'p_species_color' : pokemon_species_json['color']['name'],
      'p_species_shape' : pokemon_species_json['shape']['name'],
      'p_species_gen' : pokemon_species_json['generation']['name'],
    }

    # add data to list
    all_pokemon_data.append(pokemon_info)

  except r.exceptions.RequestException as e:
        print(f"Could not fetch data for Pokemon ID {i}: {e}")

# pokemon dataframe
pokemon_df = pd.DataFrame(all_pokemon_data)
pokemon_df.to_csv('data/raw_pokemon_data.csv', index=False)
print('Raw Pokemon data saved!')
