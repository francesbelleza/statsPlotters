from statistics import median

import matplotlib.pyplot as plt
import pandas as pd

data = {'value': [0.19, 0.70, 0.95, 1.30, 2.75, 3.10, 4.20, 4.70, 4.80, 6.48,
        7.32, 8.00, 8.28, 12.08, 31.80, 32.40, 34.00, 36.60]}
df = pd.DataFrame(data, columns=['value'])

print(" ----------basic statistics panel--------- ")
stats = df.describe()
print(stats)


print(" -------- From Problem 1 ---------")
mean = df['value'].mean()
std = df['value'].std()
min = df['value'].min()
max = df['value'].max()
range = max-min
median = df['value'].median()
q1 = df['value'].quantile(0.25)
q3 = df['value'].quantile(0.75)
inter_q = q3-q1

print(f"Mean: {mean:.3f} mins")
print(f"Standard Dev.: {std:.3f} mins")
print(f"Range: {range:.3f} mins")
print(f"Median (q2): {median:.3f} mins")
print(f"Q1: {q1:.3f} mins")
print(f"Interquartile: {inter_q:.3f} mins")


# Simple dot plot
plt.figure(figsize=(10, 4))
plt.scatter(df['value'], [1]*len(df), s=100, alpha=0.7, color='blue')
plt.xlabel('Breakdown Time (minutes)')
plt.title('Dot Plot of Breakdown Times')
plt.ylim(0.5, 1.5)
plt.yticks([])
plt.grid(True, alpha=0.3)
plt.show()