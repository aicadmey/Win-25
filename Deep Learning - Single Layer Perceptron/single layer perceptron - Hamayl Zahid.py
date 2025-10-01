x1 = int(input("enter quiz score: "))
x2 = int(input("enter exam score: "))

w1 = 0.3
w2 = 0.7

result = (x1*w1) + (x2*w2)
print(result)

# 2
x1 = int(input("Enter score(300-850) : "))
x2 = int(input("Enter Annual Income: "))
x3 = int(input("Enter Debt-to -income ratio: "))
x4 = int(input("enter amount of loan u want: "))


w1 = 0.3
w2 = 0.4
w3 = 0.2
w4 = 0.1


result = (x1*w1) + (x2*w2) + (x3*w3) + (x4*w4)
print(result)

# 3
x1 = int(input("Enter body temperature : "))
x2 = int(input("Enter heart rate: "))
x3 = int(input("Enter blood pressure: "))
x4 = int(input("enter BMI: "))
x5 = int(input("enter your age: "))
x6 = int(input("does your family has diabetes history (1 for yes ) (0 for no): "))


w1 = 0.1
w2 = 0.2
w3 = 0.1
w4 = 0.2
w5 = 0.1
w6 = 0.3

result = (x1*w1) + (x2*w2) + (x3*w3) +(x4*w4) + (x5*w5) + (x6*w6)
print(result)

# 4
x1 = int(input("Enter current humidity in integer : "))
x2 = int(input("Enter wind speed: "))
x3 = int(input("Enter barometer pressure: "))
x4 = int(input("enter Dew point in celcius: "))
x5 = int(input("did it rain yesterday (1 for yes ) (0 for no) : "))
x6 = int(input("enter current temperature: "))
x7 = int(input("are there clouds? (1 for yes ) (0 for no) : "))
x8 = int(input("enter current temperature: "))

w1 = 0.1
w2 = 0.2
w3 = 0.1
w4 = 0.2
w5 = 0.1
w6 = 0.1
w7 = 0.1
w8 = 0.1

result = (x1*w1) + (x2*w2) + (x3*w3) +(x4*w4) + (x5*w5) + (x6*w6) + (x7*w7) + (x8*w8)
print(result)
if result > 6:
    print("it will not rain today")
else:
    print("it will rain")

# 5
x1 = int(input("Enter no.bedrooms : "))
x2 = int(input("Enter no of bathrooms: "))
x3 = int(input("Enter square footage: "))
x4 = int(input("enter age of house in years: "))
x5 = int(input("distance to nearest school in miles : "))
x6 = int(input("distance to nearest grocery market in miles : "))
x7 = int(input("no of stories : "))
x8 = int(input("enter  size of garage "))
x9 = int(input("is it furnished? (1 for yes ) (0 for no): "))
x10 = int(input(" is its location is good? (1 for yes ) (0 for no): "))

w1 = 0.1
w2 = 0.1
w3 = 0.1
w4 = 0.2
w5 = 0.1
w6 = 0.1
w7 = 0.1
w8 = 0.1
w9 = 0.1
w10 = 0.1

result = (x1*w1) + (x2*w2) + (x3*w3) +(x4*w4) + (x5*w5) + (x6*w6) + (x7*w7) + (x8*w8) + (x9*w9) + (x10*w10)
print(result)
if result > 6:
    print("price will be high")
else:
    print("price will be low")

# 6
Math_Grade = int(input("Enter your math grade: "))
Sciences_Grade = int(input("Enter your sciences grade: "))
English_Grade = int(input("Enter your english grade: "))
History_Grade = int(input("Enter your history grade: "))
Foreign_Language_Grade = int(input("Enter your foreign  language grade: "))
Art_Grade = int(input("Enter your Art grade: "))
Music_Grade = int(input("Enter your music grade: "))
Physical_Education_Grade = int(input("Enter your physical education grade: "))
Computer_Science_Grade = int(input("Enter your computer science grade: "))
Elective_Grade = int(input("Enter your elective grade: "))
GPA = int(input("Enter your GPA: "))
Class_Rank = int(input("Enter your Class rank: "))

w1 = 0.1
w2 = 0.1
w3 = 0.1
w4 = 0.04
w5 = 0.1
w6 = 0.07
w7 = 0.1
w8 = 0.1
w9 = 0.1
w10 = 0.1
w11 = 0.06
w12 = 0.03

result = (Math_Grade*w1)+ (Sciences_Grade*w2)+(Elective_Grade*w3)+(History_Grade*w4)+(Foreign_Language_Grade*w5)(Art_Grade*w6)+(Music_Grade*w7)+(Physical_Education_Grade*w8)+(Computer_Science_Grade*w9)+(Elective_Grade*w10)+(GPA*w11)+(Class_Rank*w12)

if result > 70:
    print("you are going well..good work")
else:
    print("Oops! please work hard")

# 7
Name = int(input("Enter your name: "))
Age = int(input("Enter your age: "))
City = int(input("Enter your city: "))
Country = int(input("Enter your country: "))
Occupation = int(input("Enter your occupation: "))
Hobby = int(input("Enter your hobby: "))
Favourite_book = int(input("Enter your favourite book: "))
Favourite_Movie = int(input("Enter your favourite movie: "))
Favourite_Music= int(input("Enter your favourite music: "))
Favourite_sport = int(input("Enter your favourite sport: "))
Education = int(input("Enter your Education: "))
Marital_status = int(input("Enter your marital status: "))
Income = int(input("Enter your Income: "))
Favourite_book = int(input("Enter your favourite_book: "))


w1 = 0.1
w2 = 0.04
w3 = 0.08
w4 = 0.04
w5 = 0.03
w6 = 0.07
w7 = 0.02
w8 = 0.05
w9 = 0.08
w10 = 0.1
w11 = 0.06
w12 = 0.03
w13 = 0.05
w14 = 0.06


result = ((Name*w1)+ (Age*w2)+(City*w3)+(Country*w4)+(Occupation*w5)+(Hobby*w6)+(Favourite_book*w7)+(Favourite_Movie*w8)
          +(Favourite_Music*w9)+(Favourite_sport*w10)+(Education*w11)+(Marital_status*w12)+(Income*w13))
print(result)

# 8
Account_Number = int(input("Enter the account number: "))
Account_Type = int(input("Enter the account type: "))
Account_Holder = int(input("Enter the account holder: "))
Address = int(input("Enter the address: "))
Phone_Number = int(input("Enter the phone number: "))
Email = int(input("Enter the email: "))
Account_Number = int(input("Enter the account number: "))
Branch_Name = int(input("Enter the branch name: "))
IFSC_code = int(input("Enter the IFSC code: "))
MICR_code = int(input("Enter the MICR code: "))
Account_Balance = int(input("Enter the account balance: "))
Account_Status = int(input("Enter the account status: "))
Last_Transaction_Data = int(input("Enter the last transaction data: "))
Account_Opening_Date = int(input("Enter the account operating data: "))
Account_Closing_Date = int(input("Enter the account closing date: "))
Nominee_Details = int(input("Enter the nominee details: "))

w1 = 0.1
w2 = 0.04
w3 = 0.1
w4 = 0.04
w5 = 0.03
w6 = 0.07
w7 = 0.1
w8 = 0.05
w9 = 0.08
w10 = 0.1
w11 = 0.06
w12 = 0.03
w13 = 0.05
w14 = 0.06
w15 = 0.02
w16 = 0.07

result = ((((Account_Number*w1)+ (Account_Type*w2)+(Account_Holder*w3)+(Address*w4)+(Phone_Number*w5) +
          (Email*w6)+(Account_Number*w7)+(Branch_Name*w8)+(IFSC_code*w9)+(MICR_code*w10)+(Account_Balance*w11)) +
          (Account_Status*w12)+(Last_Transaction_Data*w13)+(Account_Opening_Date*w14)+(Account_Closing_Date*w15)) +
          (Nominee_Details*w16))
print(result)

# 9

High_School_GPA = float(input("Enter your High School GPA (on a 4.0 scale,: "))
SAT_Score = int(input("Enter your SAT Score: "))
Extracurricular_Activities = int(input("Rate your Extracurricular Activities : "))
Essay_Quality = int(input("Rate the Quality of your Essay : "))
Recommendation_Letters = int(input("Rate the strength of your Recommendation Letters: "))
Community_Service = int(input("Rate your Community Service involvement: "))
Leadership_Experience = int(input("Rate your Leadership Experience: "))
Awards_and_Honors = int(input("Rate your Awards and Honors: "))
Work_Experience = int(input("Rate your Work Experience: "))
Volunteer_Experience = int(input("Rate your Volunteer Experience: "))
Personal_Statement_Strength = int(input("Rate the strength of your Personal Statement: "))
Interview_Score = int(input("Rate your Interview Score : "))
Diversity_Factor = int(input("Rate the Diversity Factor you bring: "))
First_Generation_Student = int(input("Are you a First-Generation Student? (Yes=10, No=1): "))
Legacy_Status = int(input("Do you have Legacy Status? (Yes=10, No=1): "))
Financial_Need = int(input("Rate your Financial Need : "))
Geographic_Location = int(input("Rate the desirability of your Geographic Location: "))
Program_Demand = int(input("Rate the demand for the Program you're applying to: "))

w1 = 0.15
w2 = 0.10
w3 = 0.08
w4 = 0.12
w5 = 0.08
w6 = 0.05
w7 = 0.06
w8 = 0.05
w9 = 0.04
w10 = 0.04
w11 = 0.10
w12 = 0.05
w13 = 0.03
w14 = 0.02
w15 = 0.01
w16 = 0.01
w17 = 0.01
w18 = 0.01

# Calculate the admission score
result = ((High_School_GPA * w1) + (SAT_Score * w2) + (Extracurricular_Activities * w3) + (Essay_Quality * w4)
    + (Recommendation_Letters * w5) + (Community_Service * w6) + (Leadership_Experience * w7) +
    (Awards_and_Honors * w8) + (Work_Experience * w9)
    + (Volunteer_Experience * w10) + (Personal_Statement_Strength * w11) + (Interview_Score * w12)
    + (Diversity_Factor * w13) + (First_Generation_Student * w14) + (Legacy_Status * w15) + (Financial_Need * w16)
    + (Geographic_Location * w17) + (Program_Demand * w18))

# Print the admission score
print("Admission Score:", result)


# 10
Name_Length = int(input("Enter the length of your Name : "))
Age = int(input("Enter your Age : "))
City_Population = int(input("Enter your City Population : "))
Country_Area = int(input("Enter your Country Area  "))
Occupation_Stress_Level = int(input("Enter your Occupation Stress Level: "))
Hobby_Cost = int(input("Enter cost of your hobby (1-1000): "))
Favourite_Book_Pages = int(input("Enter number of pages in your favourite book (1-1000): "))
Favourite_Movie_Duration = int(input("Enter duration of your favourite movie: "))
Favourite_Music_Tempo = int(input("Enter average tempo of your favourite music : "))
Favourite_Sport_Intensity = int(input("Enter intensity level of your favourite sport : "))
Education_Level = int(input("Enter your highest education level: "))
Marital_Status_Satisfaction = int(input("Enter your marital status satisfaction level : "))
Income_Level = int(input("Enter your income level : "))
Favourite_Food_Spice_Level = int(input("Enter spice level of your favourite food : "))
Family_Member_Count = int(input("Enter number of family members : "))
Profession_Prestige = int(input("Enter perceived prestige of your profession : "))
Language_Complexity = int(input("Enter complexity of your native language : "))
Hometown_Elevation = int(input("Enter elevation of your hometown : "))
Favourite_Color_Wavelength = int(input("Enter approximate wavelength of your favourite color: "))
Daily_Steps = int(input("Enter your average daily step count (1-30000): "))

w1 = 0.05
w2 = 0.04
w3 = 0.08
w4 = 0.03
w5 = 0.03
w6 = 0.07
w7 = 0.02
w8 = 0.05
w9 = 0.08
w10 = 0.1
w11 = 0.06
w12 = 0.03
w13 = 0.05
w14 = 0.06
w15 = 0.02
w16 = 0.07
w17 = 0.08
w18 = 0.02
w19 = 0.04
w20 = 0.01

result = (Name_Length*w1) + (Age*w2) + (City_Population*w3) + (Country_Area*w4) + (Occupation_Stress_Level*w5) + (Hobby_Cost*w6) + (Favourite_Book_Pages*w7) + (Favourite_Movie_Duration*w8) + (Favourite_Music_Tempo*w9) + (Favourite_Sport_Intensity*w10) + (Education_Level*w11) + (Marital_Status_Satisfaction*w12) + (Income_Level*w13) + (Favourite_Food_Spice_Level*w14) + (Family_Member_Count*w15) + (Profession_Prestige*w16) + (Language_Complexity*w17) + (Hometown_Elevation*w18) + (Favourite_Color_Wavelength*w19) + (Daily_Steps*w20)

print("Unique Score:", result)