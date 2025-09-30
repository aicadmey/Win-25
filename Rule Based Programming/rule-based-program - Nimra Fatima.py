# rule-based-programs: 
#Example1:
internship = input("Do you wanna go for internship in summer vocation? (yes/No): ")
if internship == "yes":
    city = input("Which city do you prefer? (Lahore/Islamabad)")
    if city == "Lahore":
        print("Wow! You are going to Lahore")
    elif city == "Islamabad":
        print("Wow! You are going to Islamabad")    
    else:
        print("You are not going to any city") 
else:
    plans = input("Then what's the plan? (self study/stay at home)") 
    if plans == "self study":
        print("It is also a good idea")   
    elif plans =="stay at home":
        print("Wow! you want to spend time with family")      
    else:
        print("You are not going to any plan")   

#Example2:
food = input("Do you want to eat burger? (Yes/No): ")
if food == "yes":
    burger = input("Which burger you want to eat? (chicken-burger/zinger-burger/simple-burger): ")
    if burger == "chicken-burger":
        print("Let's eat chicken-burger")
    elif burger == "zinger-burger":
        print("Let's eat zinger-burger")  
    elif burger == "simple-burger":
        print("Let's eat simple-burger")    
    else:
        print("You don't want to eat")   
else:
    Next = input("Ok! Then what about pizza? (Yes/No): ")
    if Next == "yes":
        pizza = input("Which pizza you want to eat? (fatija-pizza/chicken-tika-pizza/tanduri-pizza): ")
        if pizza ==  "fatija-pizza":
            print("Let's eat fatija-pizza")   
        elif pizza == "chicken-tika-pizza"  :
            print("Let's eat chicken-tika-pizza")  
        elif pizza == "tanduri-pizza"  :
            print("Let's eat tanduri-pizza") 
        else:
            print("You don't want to eat ")             

#Example3:
Sports = input("Do you want to play games with me? (Yes/No): ")
if Sports == "yes":
    Game = input("Which game you want to play with me? (cricket/football/basketball)")
    if Game == "cricket":
        print("Let's play cricket")
    elif Game == "football":
        print("Let's play football")
    elif Game == "basketball":
        print("Let's play basketball")
    else:
        print("You don't want to play ")
else:
    Movie = input("Then what about movie? (Yes/No): ")  
    if Movie == "yes":
        film = input("Which film you want to watch? (spiderman/inception/interstellar): ")
        if film == "spiderman":
            print("Let's watch spiderman")
        elif film == "inception":
            print("Let's watch inception")
        elif film == "interstellar":
            print("Let's watch interstellar")   
        else:
            print("You don't want to watch")     


# Example4:
Drama = input("Do you want to watch Pak-dramas? (Yes/No): ")
if Drama == "yes":
    Pakdrama = input("Which drama you most liked? (Rangmahal/iqtadar/terebin): ")
    if Pakdrama ==  "Rangmahal":
        print("You liked Rangmahal")
    elif Pakdrama ==  "iqtadar":
        print("You liked iqtadar")   
    elif Pakdrama ==  "terebin":
        print("You liked terebin")  
else:
    drama = input("Then what about kdramas? (Yes/No): ") 
    if drama == "yes":
        kdrama = input("Which drama you most liked? (mouse/k2/king): ")
        if kdrama ==  "mouse":
          print("You liked mouse")
        elif kdrama ==  "k2":
          print("You liked k2")   
        elif kdrama ==  "king":
          print("You liked king")   
        else:
           print("You don't want to watch")     


#Example5:
Abroad = input("Do you wanna go abroad? (yes/No): ")
if Abroad == "yes":
    country = input("Which country do you prefer? (USA/Astralia/Uk/Turkish)")
    if country == "USA":
        print("Wow! You are going to USA")
    elif country == "Astralia":
        print("Wow! You are going to Astralia")   
    elif country == "Uk":
        print("Wow! You are going to Uk")       
    elif country == "Turkish":
        print("Wow! You are going to Turkish")           
    else:
        print("You are not going to any country") 
else:
    plans = input("Then what's the plan? (Admission in Pakistan/ job)") 
    if plans == "Admission in Pakistan":
        print("Wow! You want to take admission in Pakistan")   
    elif plans =="Job":
        print("Wow! Its good idea")      
    else:
        print("You are not going to any plan")   