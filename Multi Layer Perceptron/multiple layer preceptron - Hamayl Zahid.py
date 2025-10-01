
fever = int(input("Enter body temperature: "))
tachycardia = int(input("Enter heart rate: "))
hypertension = int(input("Enter blood pressure: "))
obesity = int(input("Enter BMI: "))
age = int(input("Enter your age: "))
family_diabetes_history = int(input("Does your family have diabetes history (1 for yes, 0 for no): "))

# First Hidden Layer
h1 = (fever * 0.1 + tachycardia * 0.2 + hypertension * 0.1 + obesity * 0.2 + age * 0.1 +
      family_diabetes_history * 0.3)
h2 = (fever * 0.15 + tachycardia * 0.25 + hypertension * 0.05 + obesity * 0.3 + age * 0.1 +
      family_diabetes_history * 0.2)
h3 = (fever * 0.05 + tachycardia * 0.15 + hypertension * 0.1 + obesity * 0.1 + age * 0.2 +
      family_diabetes_history * 0.4)
h4 = (fever * 0.3 + tachycardia * 0.05 + hypertension * 0.25 + obesity * 0.15 + age * 0.2 +
      family_diabetes_history * 0.25)
h5 = (fever * 0.2 + tachycardia * 0.3 + hypertension * 0.2 + obesity * 0.25 + age * 0.15 +
      family_diabetes_history * 0.05)

# Second Hidden Layer
heart_attack = (h1 * 0.4 + h2 * 0.5 + h3 * 0.3 + h4 * 0.2 + h5 * 0.1)
stroke = (h1 * 0.6 + h2 * 0.4 + h3 * 0.2 + h4 * 0.3 + h5 * 0.4)
kidney_failure = (h1 * 0.3 + h2 * 0.5 + h3 * 0.2 + h4 * 0.1 + h5 * 0.6)
lung_cancer = (h1 * 0.7 + h2 * 0.3 + h3 * 0.4 + h4 * 0.5 + h5 * 0.3)
sepsis = (h1 * 0.2 + h2 * 0.6 + h3 * 0.4 + h4 * 0.3 + h5 * 0.7)

# Output Layer
output = (heart_attack * 0.3 + stroke * 0.2 + kidney_failure * 0.5 + lung_cancer * 0.4 + sepsis * 0.6)

print(f"Predicted result: {output}")


# example no.02
# Get user inputs
x = int(input("Enter input x: "))
y = int(input("Enter input y: "))
z = int(input("Enter input z: "))
a = int(input("Enter input a: "))
b = int(input("Enter input b: "))
c = int(input("Enter input c: "))
d = int(input("Enter input d: "))

# First Hidden Layer
h1 = (x * 0.1 + y * 0.2 + z * 0.3 + a * 0.4 + b * 0.5 + c * 0.6 + d * 0.7)
h2 = (x * 0.15 + y * 0.25 + z * 0.35 + a * 0.45 + b * 0.55 + c * 0.65 + d * 0.75)
h3 = (x * 0.2 + y * 0.3 + z * 0.4 + a * 0.5 + b * 0.6 + c * 0.7 + d * 0.8)
h4 = (x * 0.3 + y * 0.4 + z * 0.5 + a * 0.6 + b * 0.7 + c * 0.8 + d * 0.9)
h5 = (x * 0.35 + y * 0.45 + z * 0.55 + a * 0.65 + b * 0.75 + c * 0.85 + d * 0.95)
h6 = (x * 0.4 + y * 0.5 + z * 0.6 + a * 0.7 + b * 0.8 + c * 0.9 + d * 1.0)
h7 = (x * 0.45 + y * 0.55 + z * 0.65 + a * 0.75 + b * 0.85 + c * 0.95 + d * 1.1)

# Second Hidden Layer
h1_out = (h1 * 0.5 + h2 * 0.6 + h3 * 0.7 + h4 * 0.8 + h5 * 0.9 + h6 * 1.0 + h7 * 1.1)
h2_out = (h1 * 0.55 + h2 * 0.65 + h3 * 0.75 + h4 * 0.85 + h5 * 0.95 + h6 * 1.05 + h7 * 1.15)
h3_out = (h1 * 0.6 + h2 * 0.7 + h3 * 0.8 + h4 * 0.9 + h5 * 1.0 + h6 * 1.1 + h7 * 1.2)
h4_out = (h1 * 0.65 + h2 * 0.75 + h3 * 0.85 + h4 * 0.95 + h5 * 1.05 + h6 * 1.15 + h7 * 1.25)
h5_out = (h1 * 0.7 + h2 * 0.8 + h3 * 0.9 + h4 * 1.0 + h5 * 1.1 + h6 * 1.2 + h7 * 1.3)
h6_out = (h1 * 0.75 + h2 * 0.85 + h3 * 0.95 + h4 * 1.05 + h5 * 1.15 + h6 * 1.25 + h7 * 1.35)
h7_out = (h1 * 0.8 + h2 * 0.9 + h3 * 1.0 + h4 * 1.1 + h5 * 1.2 + h6 * 1.3 + h7 * 1.4)

# Third Hidden Layer
h1_out2 = (h1_out * 0.2 + h2_out * 0.3 + h3_out * 0.4 + h4_out * 0.5 + h5_out * 0.6 + h6_out * 0.7 + h7_out * 0.8)
h2_out2 = (h1_out * 0.25 + h2_out * 0.35 + h3_out * 0.45 + h4_out * 0.55 + h5_out * 0.65 + h6_out * 0.75 + h7_out * 0.85)
h3_out2 = (h1_out * 0.3 + h2_out * 0.4 + h3_out * 0.5 + h4_out * 0.6 + h5_out * 0.7 + h6_out * 0.8 + h7_out * 0.9)
h4_out2 = (h1_out * 0.35 + h2_out * 0.45 + h3_out * 0.55 + h4_out * 0.65 + h5_out * 0.75 + h6_out * 0.85 + h7_out * 0.95)
h5_out2 = (h1_out * 0.4 + h2_out * 0.5 + h3_out * 0.6 + h4_out * 0.7 + h5_out * 0.8 + h6_out * 0.9 + h7_out * 1.0)
h6_out2 = (h1_out * 0.45 + h2_out * 0.55 + h3_out * 0.65 + h4_out * 0.75 + h5_out * 0.85 + h6_out * 0.95 + h7_out * 1.1)
h7_out2 = (h1_out * 0.5 + h2_out * 0.6 + h3_out * 0.7 + h4_out * 0.8 + h5_out * 0.9 + h6_out * 1.0 + h7_out * 1.2)

# Output Layer Calculation
output = (h1_out2 * 0.6 + h2_out2 * 0.7 + h3_out2 * 0.8 + h4_out2 * 0.9 + h5_out2 * 1.0 + h6_out2 * 1.1 + h7_out2 * 1.2)

print(f"Predicted result: {output}")

