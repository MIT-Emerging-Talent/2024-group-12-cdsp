
import pandas as pd

# Creating a DataFrame from the provided data
data = {
    'Indicator': ['Household Size', 'Female Employment Rate', 'Income-Earning Members', 
                  'Household Income', 'Child Marriages', 'Child Labor', 
                  'Immigration and Displacement', 'Poverty Level'],
    'Pre-restriction': [6.1, 22.6, 2.2, 2500, 35, 25, 2.5, 54],
    'Post-restriction': [6.3, 10.3, 1.8, 1800, 45, 30, 3.5, 65]
}

df = pd.DataFrame(data)

# Calculating the change for each indicator
df['Change'] = df['Post-restriction'] - df['Pre-restriction']

# Displaying the DataFrame
print(df)
