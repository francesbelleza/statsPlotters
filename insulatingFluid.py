from statistics import median

import pandas
import matplotlib.pyplot as plt

data = {'value': [0.19, 0.70, 0.95, 1.30, 2.75, 3.10, 4.20, 4.70, 4.80, 6.48,
        7.32, 8.00, 8.28, 12.08, 31.80, 32.40, 34.00, 36.60]}
df = plt.DataFrame(data, columns=['breakdown_time'])

print(" ----------basic statistics panel--------- ")
stats = df.describe()
print(stats)


print(" -------- From Problem 1 ---------")
mean = df['breakdown_time'].mean()
std = df['breakdown_time'].std()
min = df['breakdown_time'].min()
max = df['breakdown_time'].max()
range = max-min
median = df['breakdown_time'].median()
q1 = df['breakdown_time'].quantile(0.25)
q3 = df['breakdown_time'].quantile(0.75)
inter_q = q3-q1

print(f"Mean: {mean:.3f} mins")
print(f"Standard Dev.: {std:.3f} mins")
print(f"Range: {range:.3f} mins")
print(f"Median (q2): {median:.3f} mins")
print(f"Q1: {q1:.3f} mins")
print(f"Interquartile: {inter_q:.3f} mins")


# Simple dot plot
plt.figure(figsize=(10, 4))
plt.scatter(df['breakdown_time'], [1]*len(df), s=100, alpha=0.7, color='blue')
plt.xlabel('Breakdown Time (minutes)')
plt.title('Dot Plot of Breakdown Times')
plt.ylim(0.5, 1.5)
plt.yticks([])
plt.grid(True, alpha=0.3)
plt.show()