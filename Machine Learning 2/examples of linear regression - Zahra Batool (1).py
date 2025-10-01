# example 1
from sklearn.linear_model import LinearRegression
import nump

# Example data
square_footage = np.array([800, 1000, 1200, 1500, 1800]).reshape(-1, 1)
prices = np.array([200000, 250000, 300000, 350000, 400000])

# Linear regression model
model = LinearRegression()
model.fit(square_footage, prices)

# Prediction
predicted_price = model.predict([[1300]])
print(f"Predicted price for 1300 sq. ft.: {predicted_price[0]:.2f}")

# example 2
advertising_spend = np.array([1000, 1500, 2000, 2500, 3000]).reshape(-1, 1)
sales = np.array([10000, 15000, 20000, 25000, 30000])
model = LinearRegression()
model.fit(advertising_spend, sales)
predicted_sales = model.predict([[4000]])
print(f"Predicted sales for $4000 advertising spend: {predicted_sales[0]:.2f}")

# example 3

# Example data
experience = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
salaries = np.array([40000, 45000, 50000, 55000, 60000])

# Linear regression model
model = LinearRegression()
model.fit(experience, salaries)

# Prediction
predicted_salary = model.predict([[6]])
print(f"Predicted salary for 6 years of experience: {predicted_salary[0]:.2f}")

# example 4

# Example data
study_hours = np.array([5, 10, 15, 20, 25]).reshape(-1, 1)
scores = np.array([50, 60, 70, 80, 90])

# Linear regression model
model = LinearRegression()
model.fit(study_hours, scores)

# Prediction
predicted_score = model.predict([[12]])
print(f"Predicted score for 12 hours of study: {predicted_score[0]:.2f}")

# example 5

# Example data
temperature = np.array([30, 40, 50, 60, 70]).reshape(-1, 1)
energy_consumption = np.array([300, 400, 500, 600, 700])

# Linear regression model
model = LinearRegression()
model.fit(temperature, energy_consumption)

# Prediction
predicted_energy = model.predict([[55]])
print(f"Predicted energy consumption at 55°F: {predicted_energy[0]:.2f}")
