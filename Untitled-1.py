import random

num1 = range(1,36)
num2 = range(1,7)

computer1 = random.sample(num1, k=7)
computer2 = random.sample(num2, k=1)

print("welcome to lottery game!")

ask = input("do you want to start playing?(yes/no): ")

while ask != "yes":
    print("have a good day!")
    ask2 = input('do you want to start playing?(yes/no): ')
    if ask2 == "yes":
        print("lets start!")
        break
    else:
        print()


ask3 = input("pls pick 7 numbers between 1-36: ")
ask4 = input("pls pick 1 strong number between 1-7: ")

print('the numbers that you pick is', ask3, 'and your strong number is', ask4)

result = input("do you want to see the results?(yes/no): ")

if result != "yes":
    print('you lose!')
    exit

else:
    print("so the results are: ", computer1, 'and the strong number is: ', computer2)




