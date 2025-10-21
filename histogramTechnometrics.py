import matplotlib.pyplot as plt
import numpy as np

data = [88.5, 91.1, 88.2, 91.8, 89.8,
        94.7, 86.7, 88.5, 88.4, 92.7,
        84.3, 93.4, 93.3, 92.6, 93.3,
        90.1, 96.1, 87.4, 93.7, 86.7,
        89, 89.6, 91.1, 96.5, 91,
        89.8, 90.4, 90.5, 84.3, 90.9,
        91.6, 91.6, 100.3, 93.2, 89.9,
        90.3, 90.7, 87.6, 88.6, 91.8,
        90, 88.6, 92.7, 88.7, 89.7,
        91.5, 88.3, 87.9, 92.7, 92.2,
        89.9, 94.2, 93, 89.3,
        98.8, 85.3, 94.4, 91,
        88.3, 90.1, 90.4, 87.5,
        90.4, 89.3, 91.2, 87.8,
        91.2, 91.1, 86.7, 88.3,
        90.6, 92.2, 94.2, 89.2,
        92.2, 83.4, 90.8, 92.3,
        87.7, 91, 90.1, 88.9]

plt.figure(figsize=(12,5))

#histo with 8 bins
plt.subplot(1, 2, 1)
plt.hist(data, bins=8, color='skyblue', edgecolor='black')
plt.xlabel('octane rating')
plt.ylabel('frequencey')
plt.title('histogram with 8 bins')
plt.grid(axis='y', alpha=0.75)

#histo with 16 bins
plt.subplot(1, 2, 2)
plt.hist(data, bins=16, color='lightcoral', edgecolor='black')
plt.xlabel('octane rating')
plt.ylabel('frequencey')
plt.title('histogram with 16 bins')
plt.grid(axis='y', alpha=0.75)

plt.show()

