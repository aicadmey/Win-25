import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
    """Calculates the coefficients (slope and intercept) of the regression line."""
    n = np.size(x)
    
    # Mean of x and y
    m_x, m_y = np.mean(x), np.mean(y)
    
    # Cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
    
    # Calculate regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
    
    return(b_0, b_1)

def plot_regression_line(x, y, b):
    """Plots the regression line."""
    plt.scatter(x, y, color="m", marker="o", s=30) # Plot the actual data points
    
    y_pred = b[0] + b[1]*x # Predicted response vector
    
    plt.plot(x, y_pred, color="g") # Plot the regression line
    
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.show()

# Sample data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

# Estimate coefficients
b = estimate_coef(x, y)
print("Estimated coefficients:\nb_0 = {} \nb_1 = {}".format(b[0], b[1]))

# Plot the regression line
plot_regression_line(x, y, b)

#Example1:
import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
    """Calculates the coefficients (slope and intercept) of the regression line."""
    n = np.size(x)
    
    # Mean of x and y
    m_x, m_y = np.mean(x)*2, np.mean(y)*2
    
    # Cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
    
    # Calculate regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
    
    return(b_0, b_1)

def plot_regression_line(x, y, b):
    """Plots the regression line."""
    plt.scatter(x, y, color="m", marker="o", s=30) # Plot the actual data points
    
    y_pred = b[0] + b[1]*x # Predicted response vector
    
    plt.plot(x, y_pred, color="g") # Plot the regression line
    
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.show()

# Sample data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

# Estimate coefficients
b = estimate_coef(x, y)
print("Estimated coefficients:\nb_0 = {} \nb_1 = {}".format(b[0], b[1]))

# Plot the regression line
plot_regression_line(x, y, b)

##Example2:

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
    """Calculates the coefficients (slope and intercept) of the regression line."""
    n = np.size(x)
    
    # Mean of x and y
    m_x, m_y = np.mean(x), np.mean(y)**2
    
    # Cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
    
    # Calculate regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
    
    return(b_0, b_1)

def plot_regression_line(x, y, b):
    """Plots the regression line."""
    plt.scatter(x, y, color="m", marker="o", s=30) # Plot the actual data points
    
    y_pred = b[0] + b[1]*x # Predicted response vector
    
    plt.plot(x, y_pred, color="g") # Plot the regression line
    
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.show()

# Sample data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

# Estimate coefficients
b = estimate_coef(x, y)
print("Estimated coefficients:\nb_0 = {} \nb_1 = {}".format(b[0], b[1]))

# Plot the regression line
plot_regression_line(x, y, b)



##Example3:

import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
    """Calculates the coefficients (slope and intercept) of the regression line."""
    n = np.size(x)
    
    # Mean of x and y
    m_x, m_y = np.mean(x)**2, np.mean(y)
    
    # Cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
    
    # Calculate regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
    
    return(b_0, b_1)

def plot_regression_line(x, y, b):
    """Plots the regression line."""
    plt.scatter(x, y, color="m", marker="o", s=30) # Plot the actual data points
    
    y_pred = b[0] + b[1]*x # Predicted response vector
    
    plt.plot(x, y_pred, color="g") # Plot the regression line
    
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.show()

# Sample data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

# Estimate coefficients
b = estimate_coef(x, y)
print("Estimated coefficients:\nb_0 = {} \nb_1 = {}".format(b[0], b[1]))

# Plot the regression line
plot_regression_line(x, y, b)


##Example4:

import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
    """Calculates the coefficients (slope and intercept) of the regression line."""
    n = np.size(x)
    
    # Mean of x and y
    m_x, m_y = np.mean(x)**2, np.mean(y)**2
    
    # Cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
    
    # Calculate regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
    
    return(b_0, b_1)

def plot_regression_line(x, y, b):
    """Plots the regression line."""
    plt.scatter(x, y, color="m", marker="o", s=30) # Plot the actual data points
    
    y_pred = b[0] + b[1]*x # Predicted response vector
    
    plt.plot(x, y_pred, color="g") # Plot the regression line
    
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.show()

# Sample data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

# Estimate coefficients
b = estimate_coef(x, y)
print("Estimated coefficients:\nb_0 = {} \nb_1 = {}".format(b[0], b[1]))

# Plot the regression line
plot_regression_line(x, y, b)


##Eample5:

import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
    """Calculates the coefficients (slope and intercept) of the regression line."""
    n = np.size(x)
    
    # Mean of x and y
    m_x, m_y = np.mean(x), np.mean(y)*2
    
    # Cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
    
    # Calculate regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
    
    return(b_0, b_1)

def plot_regression_line(x, y, b):
    """Plots the regression line."""
    plt.scatter(x, y, color="m", marker="o", s=30) # Plot the actual data points
    
    y_pred = b[0] + b[1]*x # Predicted response vector
    
    plt.plot(x, y_pred, color="g") # Plot the regression line
    
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.show()

# Sample data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

# Estimate coefficients
b = estimate_coef(x, y)
print("Estimated coefficients:\nb_0 = {} \nb_1 = {}".format(b[0], b[1]))

# Plot the regression line
plot_regression_line(x, y, b)
