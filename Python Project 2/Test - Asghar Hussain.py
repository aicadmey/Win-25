quiz ={
    "Q1":{
        "Q":"What is capital of india ?",
        "Ans":"Mumbai"
    },
    "Q2":{
        "Q":"What is a capital of UAE ?",
        "Ans":"Dubai"
    },
    "Q3":{
        "Q":"What is a capital of Pakistan ?",
        "Ans":"Islamabad"
    },
    "Q4":{
        "Q":"What is a capital of Iran ?",
        "Ans":"Tehran"
    },
    "Q5":{
        "Q":"What is a capital of Iraq ?",
        "Ans":"Baghdad"
    }

}

score = 0
for keys , values in quiz.items():
    print(values['Q'])
    Ans = input("Enter your answer here :")
    if Ans.lower() == values['Ans'].lower():
        print("Correct")
        score +=1
        print("Your Score is :" +str(score))

    else:
        print(" The Answer is wrong ")
        print("The correct answwer is :" + values["Ans"])
        print("Your Score is :" +str(score))
        print("")
        print("")

print("You got a score :"+ str(score) + "out of 5 ")
print("Your percentage is :"+ str((score/5)*100) +"%")

