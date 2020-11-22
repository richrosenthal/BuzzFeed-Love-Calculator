# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

trueCount = 0
loveCount = 0 

#calculate the count of true in name1
trueCount += name1.count("t")
trueCount += name1.count("r")
trueCount += name1.count("u")
trueCount += name1.count("e")

#calculate the count of true love in name2
trueCount += name2.count("t")
trueCount += name2.count("r")
trueCount += name2.count("u")
trueCount += name2.count("e")

#calculate the count of love in name1
loveCount += name1.count("l")
loveCount += name1.count("o")
loveCount += name1.count("v")
loveCount += name1.count("e")

#calculate the count of love in name2
loveCount += name2.count("l")
loveCount += name2.count("o")
loveCount += name2.count("v")
loveCount += name2.count("e")

if trueCount < 1 and trueCount > 9:
  print("You go together like Coke and Mentos")
elif trueCount < 6 and trueCount > 3:
  print("You go quite well together")
else:
  print("You score is " + str(trueCount) + str(loveCount) + "%")


