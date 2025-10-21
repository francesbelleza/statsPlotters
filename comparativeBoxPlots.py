import matplotlib.pyplot as plt
import numpy as np

data_formulation_1 = [1.70, 1.90, 2.65, 2.42, 3.10, 3.30, 2.62, 1.90]
data_formulation_2 = [1.80, 2.00, 3.10, 3.30, 2.75, 2.88, 3.40, 2.48, 1.80, 3.5]

data_to_plot = [data_formulation_1, data_formulation_2]

plt.boxplot(data_to_plot, labels=['Formula 1', 'Formula 2'])

plt.title('cold start ignition')
plt.ylabel('times in seconds')

plt.show()

