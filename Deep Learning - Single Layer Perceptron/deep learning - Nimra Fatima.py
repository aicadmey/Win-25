# deep learning
#Example1:
qualification = int(input("Enter your qualification: "))
marks = int(input("Enter your marks: "))

w1 = 0.3
w2 = 0.7

result = (qualification*w1)+(marks*w2)


if result > 70:
    print("You got admission")
else:
    print("Oops! try next time")    

##Example2:
qualification = int(input("Enter your qualification: "))
marks = int(input("Enter your marks: "))
potential = int(input("Enter your potential: "))
attendence = int(input("Enter your attendence: "))

w1 = 0.1
w2 = 0.5
w3 = 0.3
w4 = 0.1

result = (qualification*w1)+(marks*w2)+(potential*w3)+(attendence*w4)

if result > 70:
    print("You got scholarship")
else:
    print("Oops! try next time")

##Example3:
Gender = int(input("Enter your gender: "))
age = int(input("Enter your age: "))
Bloodtype = int(input("Enter your blood type: "))
BP = int(input("Enter your BP: "))
weight = int(input("Enter your weight: "))
height = int(input("Enter your height: "))

w1 = 0.2
w2 = 0.1
w3 = 0.1
w4 = 0.2
w5 = 0.3
w6 = 0.1

result = (Gender*w1)+ (age*w2)+(Bloodtype*w3)+(BP*w4)+(weight*w5)+(height*w6)

if result > 70:
    print("You are healthy")
else:
    print("Oops! Please take care of yourself")

##Example4:
dectination = int(input("Enter your destination: "))
Departure_Date = int(input("Enter your Departure date: "))
Return_Date = int(input("Enter your Return date: "))
Flight_Number = int(input("Enter your Flight number: "))
Hostel_Name = int(input("Enter your Hostel name: "))
Rental_Car_Company = int(input("Enter your Rental car company: "))
Activity1 = int(input("Enter your Activity1: "))
Activity2 = int(input("Enter your Activity2: "))

w1 = 0.2
w2 = 0.1
w3 = 0.1
w4 = 0.2
w5 = 0.1
w6 = 0.1
w7 = 0.1
w8 = 0.1

result = (dectination*w1)+ (Departure_Date*w2)+(Return_Date*w3)+(Flight_Number*w4)+(Hostel_Name*w5)+(Rental_Car_Company*w6)+(Activity1*w7)+(Activity2*w8)

if result > 70:
    print("You are a travaler")
else:
    print("Oops! You are  not a travaler ")

##Example5
Make = int(input("Enter the making process: "))
Model = int(input("Enter the  car model: "))
Year = int(input("Enter the year: "))
Color = int(input("Enter the car color: "))
Mileage = int(input("Enter the mileage: "))
Engine_type = int(input("Enter the car engine type: "))
Transmission_type = int(input("Enter the car transmission type: "))
Fuel_type = int(input("Enter the fuel type: "))
Registration_number = int(input("Enter the registration number: "))
Insurance_Provider = int(input("Enter the insurance provider: "))

w1 = 0.1
w2 = 0.1
w3 = 0.1
w4 = 0.1
w5 = 0.1
w6 = 0.1
w7 = 0.1
w8 = 0.1
w9 = 0.1
w10 = 0.1

result = (Make*w1)+ (Model*w2)+(Year*w3)+(Color*w4)+(Mileage*w5)+(Engine_type*w6)+(Transmission_type*w7)+(Fuel_type*w8)+(Registration_number*w9)+(Insurance_Provider*w10)
if result > 70:
    print("You have a legal car")
else:
    print("Oops! You have ilegal car")

##Example6:
Math_Grade  = int(input("Enter your math grade: "))
Sciences_Grade  = int(input("Enter your sciences grade: "))
English_Grade  = int(input("Enter your english grade: "))
History_Grade  = int(input("Enter your history grade: "))
Foreign_Language_Grade  = int(input("Enter your foreign  language grade: "))
Art_Grade  = int(input("Enter your Art grade: "))
Music_Grade  = int(input("Enter your music grade: "))
Physical_Education_Grade  = int(input("Enter your physical education grade: "))
Computer_Science_Grade  = int(input("Enter your computer science grade: "))
Elective_Grade  = int(input("Enter your elective grade: "))
GPA  = int(input("Enter your GPA: "))
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

result = (Math_Grade*w1)+ (Sciences_Grade*w2)+(Elective_Grade*w3)+(History_Grade*w4)+(Foreign_Language_Grade*w5)+(Art_Grade*w6)+(Music_Grade*w7)+(Physical_Education_Grade*w8)+(Computer_Science_Grade*w9)+(Elective_Grade*w10)+(GPA*w11)+(Class_Rank*w12)

if result > 70:
    print("You are a good student")
else:
    print("Oops! please work hard")

##Example7:
Temperature = int(input("Enter the today temperature: "))
Humidity = int(input("Enter the humidity: "))
Wind_speed = int(input("Enter the wind speed: "))
Wind_Direction = int(input("Enter the wind direction: "))
Precipitation = int(input("Enter the precipitation: "))
Cloud_Cover = int(input("Enter the cloud cover: "))
UV_Index = int(input("Enter the ux index: "))
Air_Quality = int(input("Enter the air quality: "))
Atmospheric_pressure = int(input("Enter the atmospheric pressure: "))
Visibility = int(input("Enter the visibility: "))
Dew_Point = int(input("Enter the dew point: "))
Wind_Chill = int(input("Enter the wind chill: "))
Sunrise_Time = int(input("Enter the sunrise time: "))
Sunset_Time = int(input("Enter the sunset time: "))

w1 = 0.1
w2 = 0.04
w3 = 0.1
w4 = 0.04
w5 = 0.1
w6 = 0.07
w7 = 0.1
w8 = 0.05
w9 = 0.1
w10 = 0.1
w11 = 0.06
w12 = 0.03
w13 = 0.05
w14 = 0.06

result = (Temperature*w1)+ (Humidity*w2)+(Wind_speed*w3)+(Wind_Direction*w4)+(Precipitation*w5)+(Cloud_Cover*w6)+(UV_Index*w7)+(Air_Quality*w8)+(Atmospheric_pressure*w9)+(Visibility*w10)+(Dew_Point*w11)+(Wind_Chill*w12)+(Sunrise_Time*w13)+(Sunset_Time*w14)
print(result)

##Example8:
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

result = (Account_Number*w1)+ (Account_Type*w2)+(Account_Holder*w3)+(Address*w4)+(Phone_Number*w5)+(Email*w6)+(Account_Number*w7)+(Branch_Name*w8)+(IFSC_code*w9)+(MICR_code*w10)+(Account_Balance*w11)+(Account_Status*w12)+(Last_Transaction_Data*w13)+(Account_Opening_Date*w14)+(Account_Closing_Date*w15)+(Nominee_Details*w16)
print(result)

##Example9:
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
Family_member = int(input("Enter your family_member: "))
Profession= int(input("Enter your profession: "))
Language = int(input("Enter your language: "))
Hometown = int(input("Enter your hometown: "))

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
w15 = 0.02
w16 = 0.07
w17 = 0.08
w18 = 0.02

result = (Name*w1)+ (Age*w2)+(City*w3)+(Country*w4)+(Occupation*w5)+(Hobby*w6)+(Favourite_book*w7)+(Favourite_Movie*w8)+(Favourite_Music*w9)+(Favourite_sport*w10)+(Education*w11)+(Marital_status*w12)+(Income*w13)+(Favourite_book*w14)+(Family_member*w15)+(Profession*w16)+(Language*w17)+(Hometown*w18)
print(result)

##Example10:
Event_Name = int(input("Enter the event name: "))
Event_Date = int(input("Enter the event date: "))
Event_Time = int(input("Enter the event time: "))
Event_Location = int(input("Enter the event location: "))
Guest_list = int(input("Enter the Guest list: "))
Catering_option = int(input("Enter the catering option: "))
Entertainment = int(input("Enter the entertainment: "))
Decoration = int(input("Enter the decoration: "))
Audio_Visual_Equipment = int(input("Enter the audio visual equipment: "))
Budget = int(input("Enter the budget: "))
Transporation = int(input("Enter the transporation: "))
Accommodation = int(input("Enter the accommodation: "))
Event_Theme = int(input("Enter the event theme: "))
Event_Agenda = int(input("Enter the event agenda: "))
Sponsor_Details= int(input("Enter the sponsor details: "))
Vendor_Detail = int(input("Enter the vendor details: "))
Registration_Deadline = int(input("Enter the registration deadline: "))
Event_Hashtag = int(input("Enter the event hashtag: "))
Ticket_Price = int(input("Enter the ticket price: "))
Event_Schedule = int(input("Enter the event schedule: "))

w1 = 0.06
w2 = 0.04
w3 = 0.08
w4 = 0.04
w5 = 0.03
w6 = 0.07
w7 = 0.02
w8 = 0.05
w9 = 0.08
w10 = 0.03
w11 = 0.06
w12 = 0.03
w13 = 0.05
w14 = 0.06
w15 = 0.02
w16 = 0.07
w17 = 0.08
w18 = 0.02
w19 = 0.07
w20 = 0.04

result = (Event_Name*w1)+ (Event_Date*w2)+(Event_Time*w3)+(Event_Location*w4)+(Guest_list*w5)+(Catering_option*w6)+(Entertainment*w7)+(Decoration*w8)+(Audio_Visual_Equipment*w9)+(Budget*w10)+(Transporation*w11)+(Accommodation*w12)+(Event_Theme*w13)+(Event_Agenda*w14)+(Sponsor_Details*w15)+(Vendor_Detail*w16)+(Registration_Deadline*w17)+(Event_Hashtag*w18)+(Ticket_Price*w19)+(Event_Schedule*w20)
print(result)