from statistics import linear_regression
from sklearn.linear_model import LinearRegression
import numpy as np


regression = LinearRegression()

reg = linear_regression

house_size = [[1337671.8], [1359966.33], [1359966.33], [1404555.39], [1426849.92], [1426849.92], [1426849.92], [1449144.45], [1460291.715], [1471438.98], [1516028.04], [1516028.04], [1560617.0999999999], [1571764.365], [1582911.63], [1594058.895], [1605206.16], [1605206.16], [1605206.16], [1627500.69]]

cost = [3, 3.2, 3.4, 3.4, 3.5, 3.7, 3.4, 3.7, 3.8, 3.9, 4.0, 3.95, 4.0, 4.2, 4.4, 4.3, 4.2, 4.1, 4.4, 4.6]
#house_size = [[2],[4],[6],[8],[10]]
#cost = [3,6,9,12,15]

print(house_size)
print(cost)

print(np.count_nonzero(house_size))
print(np.count_nonzero(cost))
regression.fit(house_size, cost)
print(regression.predict([[1672089.75]]))