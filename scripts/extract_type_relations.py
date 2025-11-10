# libraries used
import requests as r
import pandas as pd

# base url type
base_url = "https://pokeapi.co/api/v2/type"

# number of types
no_of_types = r.get(base_url).json()['count']

# container for data
all_relations_type_data = []

# get all types
try:
  type_data = r.get(base_url)
  type_data.raise_for_status()
  all_types = type_data.json().get('results', [])

  # initial loop
  for type_info in all_types:
    type_name = type_info.get('name')
    type_url = type_info.get('url')

    # check if type_name is not null
    if type_name:
      type_details_info = r.get(type_url)
      type_details_info.raise_for_status()
      type_data = type_details_info.json()

      dmg_relations = type_data.get('damage_relations', {})

      # keys under damage_relations
      dmg_relation_keys = ['double_damage_from', 'double_damage_to', 'half_damage_from', 'half_damage_to', 'no_damage_from', 'no_damage_to']

      # loops for retrieving affected types
      for relation_name in dmg_relation_keys:
        target_types_list = dmg_relations.get(relation_name, [])

        for target_type_dict in target_types_list:
          target_type_name = target_type_dict.get('name')

          # mapping of data
          if target_type_name:
            row = {
                'type_name': type_name,
                'relation': relation_name,
                'target_type': target_type_name
            }

            # add data to container
            all_relations_type_data.append(row)

except r.exceptions.RequestException as e:
        print(f"Could not fetch data for Type Name {type_name}: {e}")

# type dataframe
type_df = pd.DataFrame(all_relations_type_data)
type_df.to_csv('data/raw_type_data.csv', index=False)
print('Raw Type data saved!')