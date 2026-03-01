# input() uses to get data from the user. it's the input function
# by default input() is in string type. 

print("please enter your recipient's name:")
r_name = input()
print("Year of birth:")
year = int(input())
age = 2026 - year 
print("What's your message:")
meg = input()
print("enter your name:")
name = input()

print("{}, let celebrate your {} years of awesomeness!\nWishing you a day filled with joy and laughter as you turn {}!\n ".format(r_name, age, age))

print(meg + "\n With love and best wishes,\n" + name)