import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# Engineer is_resistance feature
troop_movements['is_resistance'] = troop_movements['empire_or_resistance'].str.lower() == 'resistance'

# Empire vs Resistance distribution using Seaborn
sns.countplot(data=troop_movements, x="empire_or_resistance", palette="dark")
plt.title("Character Count by Empire or Resistance")
plt.xlabel("Empire or Resistance")
plt.ylabel("Count")
plt.show()