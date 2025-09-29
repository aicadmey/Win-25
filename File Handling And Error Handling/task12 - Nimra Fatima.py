#Error Handling
#Example1:
a = int(input("Enter the number: "))


try:
    result = 1/a
    print(result) 
except ZeroDivisionError:
    print("Please! Don't enter zero.") 
except TypeError:
    print("Only enter integers.")
except Exception:
    print("An unexcepted error occur: ")    

#Example2:
def calculate_square_root(number):
        try:
           result = number ** 0.5
           print("Square root :" , result)
        except TypeError:
           print("Please enter number. ")
        except Exception as e:
           print("An unexpected error occur: " ,str(e)) 

calculate_square_root(16)
calculate_square_root("a")       

#Example3:
def calculate_area(lenght , width):
    try:
        result = lenght * width
        print("Area :" , result)
    except TypeError:
        print("Please enter integer! ")    
    
              
calculate_area(7, 3)
calculate_area("pak"," pizza")

#File Handling
# For write
#Example1:

file =open("example.txt", "w")
file.write("Hello, World! \n")
file.write("This is a test file. \n")

file.close()
print("File written successfully. ")

#Example2:
file = open("Hey.txt", "w")
file.write("Hey, Guys")

file.close()
print("File written successfully. ")

#Example3:
file = open("Marks.txt", "w")
file.write("I have scored good marks.\n")

file.close()
print("File written successfully. ")


#File Handling For read
#Example1:
with open("example.txt","r") as file:
    content = file.read()
    print(content)
#Example2:
file = open("example.txt", "r")
for line in file:
    print(line) 
file.close() 
#Example3:
with open("Marks.txt","r") as file:
    content = file.read()
    print(content)

#File Handling For append
##Example1:
my_file = "example.txt"
file = open("example.txt", "a")
file.write("I have written appended text.\n")
print(f"Data successfully appended to {my_file}.")
file.close()
#Example2:
my_file = "Hey.txt"
with open(my_file, "a") as file:
    file.write("Nimra,Fatima,Ayesha.\n")
print(f"Data successfully appended to {my_file}.")
##Example3:
my_file = "Marks.txt"
with open(my_file, "a") as file:
    file.write("I'm very happy for this achievement.")
print(f"Data successfully appended to {my_file}.")