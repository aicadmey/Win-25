#multiple_neural_programs
# #Example!:
Grand_grant_parent = int(input("Enter the inheretance you got from Grant grant parent: "))
Grant_Parent = int(input("Enter the inheretance you got from your grant parent: "))
Parent = int(input("Enter the inheretance you  got from your parent: "))

hair_color = (Grand_grant_parent*0.1)+(Grant_Parent*0.4)+(Parent*0.5)
height = (Grand_grant_parent*0.3)+(Grant_Parent*0.3)+(Parent*0.4)
eye_color = (Grand_grant_parent*0.2)+(Grant_Parent*0.3)+(Parent*0.5)
Dimples = (Grand_grant_parent*0.3)+(Grant_Parent*0.5)+(Parent*0.2)
Mental_disorder = (Grand_grant_parent*0.2)+(Grant_Parent*0.3)+(Parent*0.5)

#Inherentance passed to next generation
hair_color = (hair_color*0.3)+(height*0.2)+(eye_color*0.5)+(Dimples*0.2)+(Mental_disorder*0.4)
height = (hair_color*0.4)+(height*0.2)+(eye_color*0.4)+(Dimples*0.2)+(Mental_disorder*0.4)
eye_color = (hair_color*0.3)+(height*0.4)+(eye_color*0.3)+(Dimples*0.2)+(Mental_disorder*0.4)
Dimples = (hair_color*0.2)+(height*0.6)+(eye_color*0.2)+(Dimples*0.2)+(Mental_disorder*0.4)
Mental_disorder = (hair_color*0.1)+(height*0.3)+(eye_color*0.6)+(Dimples*0.2)+(Mental_disorder*0.4)

print("hair_color " , hair_color)
print("height " , height)
print("eye_color " , eye_color)
print("Dimples " , Dimples)
print("Mental_disorder " , Mental_disorder)


#Example2:
x1 = int(input("Enter the x1: "))
x2 = int(input("Enter the x2:  "))
x3 = int(input("Enter the x3:  "))
 
inputx1 = (x1*0.3) + (x2*0.5) + (x3*0.2) 
inputx2 = (x1*0.2) + (x2*0.6) + (x3*0.2)
inputx3 = (x1*0.1) + (x2*0.5) + (x3*0.4)
inputx4 = (x1*0.2) + (x2*0.4) + (x3*0.4)
inputx5 = (x1*0.5) + (x2*0.2) + (x3*0.3)
inputx6 = (x1*0.4) + (x2*0.1) + (x3*0.5)
inputx7 = (x1*0.3) + (x2*0.4) + (x3*0.3)

subinputx1 = (inputx1 * 0.1) + (inputx2*0.3) + (inputx3*0.1) +(inputx4*0.2) +(inputx5*0.1)+(inputx6*0.1)+(inputx7*0.1)
subinputx2 = (inputx1 * 0.2) + (inputx2*0.1) + (inputx3*0.3) +(inputx4*0.1) +(inputx5*0.1)+(inputx6*0.1)+(inputx7*0.1)
subinputx3 = (inputx1 * 0.2) + (inputx2*0.1) + (inputx3*0.1) +(inputx4*0.2) +(inputx5*0.1)+(inputx6*0.2)+(inputx7*0.1)
subinputx4 = (inputx1 * 0.1) + (inputx2*0.2) + (inputx3*0.1) +(inputx4*0.1) +(inputx5*0.2)+(inputx6*0.1)+(inputx7*0.2)
subinputx5 = (inputx1 * 0.3) + (inputx2*0.1) + (inputx3*0.1) +(inputx4*0.1) +(inputx5*0.1)+(inputx6*0.2)+(inputx7*0.1)
subinputx6 = (inputx1 * 0.1) + (inputx2*0.1) + (inputx3*0.3) +(inputx4*0.2) +(inputx5*0.1)+(inputx6*0.1)+(inputx7*0.1)
subinputx7 = (inputx1 * 0.2) + (inputx2*0.1) + (inputx3*0.1) +(inputx4*0.1) +(inputx5*0.1)+(inputx6*0.1)+(inputx7*0.3)

ssubinputx1 = (subinputx1 * 0.3) + (subinputx2*0.1) + (subinputx3*0.1) +(subinputx4*0.1) +(subinputx5*0.2)+(subinputx6*0.1)+(subinputx7*0.1)
ssubinputx2 = (subinputx1 * 0.1) + (subinputx2*0.2) + (subinputx3*0.1) +(subinputx4*0.2) +(subinputx5*0.2)+(subinputx6*0.1)+(subinputx7*0.1)
ssubinputx3 = (subinputx1 * 0.2) + (subinputx2*0.1) + (subinputx3*0.2) +(subinputx4*0.1) +(subinputx5*0.1)+(subinputx6*0.1)+(subinputx7*0.2)
ssubinputx4 = (subinputx1 * 0.1) + (subinputx2*0.2) + (subinputx3*0.1) +(subinputx4*0.1) +(subinputx5*0.2)+(subinputx6*0.2)+(subinputx7*0.1)
ssubinputx5 = (subinputx1 * 0.1) + (subinputx2*0.1) + (subinputx3*0.2) +(subinputx4*0.2) +(subinputx5*0.2)+(subinputx6*0.1)+(subinputx7*0.1)
ssubinputx6 = (subinputx1 * 0.3) + (subinputx2*0.1) + (subinputx3*0.1) +(subinputx4*0.1) +(subinputx5*0.1)+(subinputx6*0.1)+(subinputx7*0.2)
ssubinputx7 = (subinputx1 * 0.1) + (subinputx2*0.2) + (subinputx3*0.1) +(subinputx4*0.1) +(subinputx5*0.2)+(subinputx6*0.2)+(subinputx7*0.1)

print("ssubinput1 = " , ssubinputx1)
print("ssubinput2 = " , ssubinputx2)
print("ssubinput3 = " , ssubinputx3)
print("ssubinput4 = " , ssubinputx4)
print("ssubinput5 = " , ssubinputx5)
print("ssubinput6 = " , ssubinputx6)
print("ssubinput7 = " , ssubinputx7)