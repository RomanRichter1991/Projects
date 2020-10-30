import random

number = random.randint(1,10)
loop_count = 0


while loop_count < 10 :
    print("Loop:", loop_count + 1)
    if (int(number) >= 5):
        print(int(number),"more than 5!")
        number = random.randint(1,10)
    else:
        print(int(number),"less than 5!")
        number = random.randint(1,10)
    loop_count += 1
else :
    print ('Program finished')
