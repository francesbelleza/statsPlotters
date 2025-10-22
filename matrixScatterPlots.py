import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('HW5_Computer_Data.xlsx', header=0)
#petroleum_data = data[['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3']]

#debug lines
#print("Column Names:")
#print(data.columns.tolist())

petroleum_data = data.iloc[1:, 1:4].astype(float)

pd.plotting.scatter_matrix(petroleum_data, figsize=(10, 10))
plt.show()


print("----correlation matrix----")
correlation_matrix = petroleum_data.corr()
print(correlation_matrix)