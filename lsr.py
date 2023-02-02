import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading the phishing data
data = pd.read_csv('phishing_dataset_full.csv')

# Choosing one attribute to see its correlation with phishing
X = data['qty_dot_url'].values
Y = data['phishing'].values

mean_x = np.mean(X)
mean_y = np.mean(Y)

numerator, denominator = 0, 0

for i in range(len(X)):
    numerator += (X[i] - mean_x) * (Y[i] - mean_y)
    denominator += (X[i] - mean_x) ** 2
m = numerator/denominator
c = mean_y - (m* mean_x)

max_x = np.max(X) + 100
min_x = np.min(X) - 100

x = np.linspace(min_x, max_x, 1000)
y = c + m * x

plt.plot(x, y, color='#58b970', label='Phishing Dataset Regression Line')

plt.scatter(X, Y, c="#ef5423", label='Scatter Plot')

plt.xlabel('qty_dot_url')
plt.ylabel('Phishing')
plt.legend()
plt.show()
# linear model between x_attribute and phishing

