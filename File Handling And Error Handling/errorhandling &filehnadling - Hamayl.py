# Error Handling
# Example no.1
a = input("a= ")
b = input("b= ")
try:
    sum = a + b
except:
    print("Type Error")
else:
    print(sum)

# Example no.2

x = input("x= ")
y = input("y= ")
try:
    c = x / y
except:
    print("error 400")

# Example no.3

n1 = "hi"
n2 = 10
try:
    mult = n1 + n2
except:
    print("Type Error")
else:
    print(mult)

# FILE HANDLING
# Example no.1
my_File = "example.txt"

with open(my_File, "w") as file:
    file.write("\n hi ! everyone ,how r u doing?")

with open(my_File, "a") as file:
    file.write("\n I am Hamayl,nice to meet u")

with open(my_File, "r") as file:
    data = file.read()
    print(f"data of file {my_File} is {data}")

# Example no.2
my_File = "demofile.txt"

with open(my_File, "w") as file:
    file.write("\n hamayl, asma")

with open(my_File, "a") as file:
    file.write("\nAppended data")

with open(my_File, "r") as file:
    data = file.read()
    print(f"data of file {my_File} is {data}")

# Example no.3
files = "pdf.txt"

with open(files, "w") as file:
    file.write("\n marks of students are: \n 89\n 50\n 100")

with open(files, "a") as file:
    file.write("\n 45\n 39")

with open(files, "r") as file:
    data = file.read()
    print(f"data of file {my_File} is {data}")
