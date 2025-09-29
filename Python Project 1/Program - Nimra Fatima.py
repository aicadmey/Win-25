def center():
    print("Wellcome To A Brand New  Shoe Center! ")
    print("Today's Special: Discount for lucky people!")
def calculat_discount(age) :
    if age < 18:
        return 0.1
# 10% discount for children
    elif age >= 50:
        return 0.3
# 20% discount for seniors
    else:
        return 0
# No discount for others
center()
def get_user_input():
    total_discount = 0
    for i in range(3):
        age = int(input(f"Enter age of the person {i+1}: "))
        discount = calculat_discount(age)
        if discount > 0:
            print(f" Congratulations!! There is discount for Person {i + 1}. ")
            total_discount = discount
            print(f" Total discount :{total_discount * 100}% ")
            # {discount*100}%
        else:
              print(f" Oops!! There is no discount for Person {i + 1}. ") 
              print(" Total discount :0% ")  
def main():
  get_user_input() 
if __name__ == "__main__":
    main()