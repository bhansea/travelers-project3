import pandas as pd

troop_movements = pd.read_csv('troop_movements.csv')
# troop_movements.head()

empire_resistance_counts = troop_movements.groupby('empire_or_resistance').agg({
    'empire_or_resistance': 'count'
})

print(empire_resistance_counts)

character_by_homeworld_counts = troop_movements.groupby('homeworld').agg({
    'homeworld': 'count'
})

print(character_by_homeworld_counts)

character_by_unit_type_counts = troop_movements.groupby('unit_type').agg({
    'unit_type': 'count'
})

print(character_by_unit_type_counts)

# def isResistance(e_or_r):
#     for type in e_or_r:
#         if type == 'empire':
#             print(False)
#         else:
#             print(True)

# troop_movements['is_resistance'] = troop_movements.apply(isResistance(troop_movements['empire_or_resistance']))
# print(troop_movements.head())