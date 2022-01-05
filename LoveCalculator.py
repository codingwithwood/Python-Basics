print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#change names to lower case letters to count the specific letters
lower_name1 = name1.lower()
lower_name2 = name2.lower()

#merge the names into one long string 
long_name = lower_name1 + lower_name2

#count how many times the letters in TRUE occur
true_count = long_name.count('t') + long_name.count('r') + long_name.count('u') + long_name.count('e')
#count how many times the letters in LOVE occur
love_count = long_name.count('l') + long_name.count('o') + long_name.count('v') + long_name.count('e')
#combine both numbers to get a 2 digit number as their love score
score = str(true_count) + str(love_count)
#change the combined numbers from string back to integer
score_number = int(score)

#calculate compatibility based on their score
if score_number < 10 or score_number > 90:
  print(f"Your score is {score_number}, you go together like coke and mentos.")
elif score_number >= 40 and score_number <= 50:
  print(f"Your score is {score_number}, you are alright together.")
else:
  print(f"Your score is {score_number}.")
