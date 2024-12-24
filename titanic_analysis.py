import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
url = https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
dataset = pd.read_csv(url)

# Explore the data
print(dataset.head())  # Display the first 5 rows of the dataset
print(dataset.info())  # Get a summary of the dataset

# Calculate the death count
death_count = dataset[dataset['Survived'] == 0].shape[0]
print(f'Total number of deaths: {death_count}')

# Visualize survival vs death
sns.countplot(data=dataset, x='Survived', palette='coolwarm')
plt.title('Survival Counts (0 = Died, 1 = Survived)')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()


