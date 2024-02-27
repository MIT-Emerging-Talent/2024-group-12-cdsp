import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creating a DataFrame from the provided data
data = {
    'Indicator': ['Household Size', 'Female Employment Rate', 'Income-Earning Members', 
                  'Household Income', 'Child Marriages', 'Child Labor', 
                  'Immigration and Displacement', 'Poverty Level'],
    'Pre-restriction': [6.1, 22.6, 2.2, 2500, 35, 25, 2.5, 54],
    'Post-restriction': [6.3, 10.3, 1.8, 1800, 45, 30, 3.5, 65],
    'Unit': ['people', '%', 'members', '$', '%', '%', 'M', '%']
}

df = pd.DataFrame(data)

# Create a bar plot for each indicator using Seaborn
for index, row in df.iterrows():
    plt.figure(figsize=(8, 5))
    sns.barplot(x=['Pre-restriction', 'Post-restriction'], y=[row['Pre-restriction'], row['Post-restriction']], palette=['lightblue', 'orange'])
    plt.title(f"{row['Indicator']} ({row['Unit']})")
    plt.ylabel('Values')
    plt.show()
