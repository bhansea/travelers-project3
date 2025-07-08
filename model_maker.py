import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

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
print(troop_movements)

# Empire vs Resistance distribution using Seaborn
sns.countplot(data=troop_movements, x="empire_or_resistance", palette="dark")
plt.title("Character Count by Empire or Resistance")
plt.xlabel("Empire or Resistance")
plt.ylabel("Count")
plt.show()

X, y = troop_movements[['homeworld', 'unit_type']], troop_movements['is_resistance']

X_encoded = pd.get_dummies(X, columns=['homeworld', 'unit_type'])

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(predictions, y_test)
print(accuracy)

with open('trained_model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Get feature importances
importances = model.feature_importances_

# Create a DataFrame to hold the feature importances
feature_importances = pd.DataFrame({'Feature': X_encoded.columns, 'Importance': importances}).sort_values('Importance', ascending=False)
print(feature_importances.head())

plt.figure(figsize=(10,10))
sns.barplot(x=feature_importances['Feature'], y=feature_importances['Importance'])
plt.xticks(rotation='vertical')
plt.xlabel('Feature')
plt.ylabel('Importance')
plt.title('Feature Importances')
plt.savefig('feature_importances.png')
plt.show()

print(f'Most Influential Unit Type: {feature_importances['Feature'][0]}')