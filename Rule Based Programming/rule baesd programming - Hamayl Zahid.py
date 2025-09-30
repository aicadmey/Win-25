# example no.01
print("\nLet's plan your weekend!")

weather = input("Is the weather going to be nice or bad? (nice/bad): ").lower()

if weather == "nice":
    activity_type = input("Do you prefer active or relaxing activities? (active/relaxing): ").lower()
    if activity_type == "active":
        location = input("Do you prefer nature or the city? (nature/city): ").lower()
        if location == "nature":
            print("Go hiking, biking!")
        elif location == "city":
            print(" go to a street fair, or visit a museum.")
        else:
            print("Invalid input for location.")
    elif activity_type == "relaxing":
        print("Have a picnic in the park, or read a book outdoors.")
    else:
        print("Invalid input for activity type.")

elif weather == "bad":
    activity_type = input("Do you want to stay home or go out? (home/out): ").lower()
    if activity_type == "home":
        print("Watch a movie, play board games, or try a new recipe.")
    elif activity_type == "out":
        print("Go to a museum, see a movie at the cinema,")
    else:
        print("Invalid input for location.")
else:
    print("Invalid input for weather.")

# example n0.02
print("\nLet's help you choose a bachelor's degree field!")
interest_area = input("Are you more interested in stem(Science, Technology, Engineering, Math),or Business? ").lower()

if interest_area == "stem":
    stem_subject = input("Which STEM subject interests you most? (bio/math/computer): ").lower()
    if stem_subject == "bio":
        bio_focus = input("Are you more interested in organisms or molecular").lower()
        if bio_focus == "organisms":
            print("Consider fields like Ecology, Zoology, Botany, or Marine Biology.")
        elif bio_focus == "molecular":
            print("Consider fields like Biochemistry, Microbiology, Genetics, or Biotechnology.")
        else:
            print("Invalid input for bio focus.")
    elif stem_subject == "math":
        math_focus = input("Are you more interested in pure math or applied math? (pure/applied): ").lower()
        if math_focus == "pure":
            print("Consider fields like Pure Mathematics, Number Theory, or Topology.")
        elif math_focus == "applied":
            print("Consider fields like Applied Mathematics, Statistics, Actuarial Science, or Financial Mathematics.")
        else:
            print("Invalid input for math focus.")
    elif stem_subject == "computer":
        computer_focus = input("Are you more interested in software or hardware? (software/hardware): ").lower()
        if computer_focus == "software":
            print("Consider fields like Computer Science, Software Engineering, or Information Technology.")
        elif computer_focus == "hardware":
            print("Consider fields like Computer Engineering or Embedded Systems.")
        else:
            print("Invalid input for computer focus.")
    else:
        print("Invalid input for STEM subject.")

elif interest_area == "business":
    business_focus = input("Are you more interested in finance/numbers or marketing/people?").lower()
    if business_focus == "finance":
        print("Consider fields like Finance, Accounting, or Economics.")
    elif business_focus == "marketing":
        print("Consider fields like Marketing, Human resources, or Public relations.")
    else:
        print("Invalid input for business focus.")
else:
    print("Invalid input for interest area.")

# example no.3
print("\nWelcome to the Mars Alien Adventure!")

mission = input("What are you doing on Mars? (looking for aliens/talking to aliens: ").lower()

if mission == "looking for aliens":
    search = input("Where are you searching? (old buildings/caves): ").lower()
    if search == "old buildings":
        what_you_find = input("What do you find? (old tools/dead aliens): ").lower()
        if what_you_find == "old tools":
            print("You found some cool alien tools! Maybe they used them a long time ago.")
        elif what_you_find == "dead aliens":
            print("You found some alien skeletons! What happened to them?")
        else:
            print("Wrong answer.")
    elif search == "caves":
        what_inside = input("Are the caves dry or wet? (dry/wet): ").lower()
        if what_inside == "dry":
            print("You found some cool rocks in the dry caves.")
        elif what_inside == "wet":
            print("You found some weird water in the wet caves. Maybe there's life in it!")
        else:
            print("Wrong answer.")
    else:
        print("Wrong answer.")

elif mission == "talking to aliens":
    find = input("How did you find them? (radio signals/saw them): ").lower()
    if find == "radio signals":
        what_they_say = input("What kind of message is it? (hello/help): ").lower()
        if what_they_say == "hello":
            print("The aliens said hello! Maybe they are friendly.")
        elif what_they_say == "help":
            print("The aliens are asking for help! What should you do?")
        else:
            print("Wrong answer.")

print("Your Mars adventure continues!")

# example no.04
print("\nhi! ! welcome to our shoe store ..\n")
color = input(" plz mention the color you want(black,red,pink): ")
if color == "black" or color == "red" or color == "pink":
    range = input("plz mention the range (2k,3k,4k,5k: ")
    if range == "2k":
        print("these are our collections .plz have a look")
    elif range == "3k":
        print("these are our collections .plz have a look")
    elif range == "4k":
        print("these are our collections .plz have a look")
    elif range == "5k":
        print("its limited collection .plz have a look")
    else:
        print("Invalid price range. Please choose from 2k, 3k, 4k, or 5k.")
else:
    print("Sorry, we don't have that color. Please choose from black, red, or pink.")

shoe = input("which shoe you liked?\n mention its range and color: ")
print("\nyou won discount!!")

if '2k' in shoe:
    print("your discount is 10%")
elif '3k' in shoe:
    print("your discount is 20%")
elif '4k' in shoe:
    print("your discount is 25%")
elif '5k' in shoe:
    print("your discount is 30%")
else:
    print("no discount")


# example no.05
print("\nLet's choose a programming language!")

goal = input("Do you want to build web applications or desktop/mobile apps? (web/apps): ").lower()

if goal == "web":
    frontend_or_backend = input("Are you interested in frontend or backend development? (frontend/backend): ").lower()
    if frontend_or_backend == "frontend":
        print("Consider learning HTML, CSS, and JavaScript.")
    elif frontend_or_backend == "backend":
        print("Consider learning Python , Node.js, or Ruby on Rails.")
    else:
        print("Invalid input for web development specialization.")
elif goal == "apps":
    mobile_or_desktop = input("Are you interested in mobile or desktop app development? (mobile/desktop): ").lower()
    if mobile_or_desktop == "mobile":
        print("Consider learning Java/Kotlin (for Android), Swift (for IOS).")
    elif mobile_or_desktop == "desktop":
        print("Consider learning C#, Java, or Python.")
    else:
        print("Invalid input for app development platform.")
else:
    print("Invalid input for initial goal.")



