import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({'x': [1, 2, 3, 4, 5.3,],
                     'y': [2, 4, 6, 8, 10.2]})

x_train, x_test, y_train, y_test = train_test_split(data[['x']],data[['y']],test_size=0.2)

reg= LinearRegression().fit(x_train,y_train)

y_pred = reg.predict(x_test)
mse = np.mean((y_pred - y_test)**2, axis = 0)
print("Mean Squared Error: ",mse[0])