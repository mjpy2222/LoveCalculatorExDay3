
print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
names = name1 + name2
lower_names = names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
score1 = t + r + u + e

l1 = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e2 = lower_names.count("e")
score2 = l1 + o + v + e2

total_score = str(score1) + str(score2)
love_score = int(total_score)
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
