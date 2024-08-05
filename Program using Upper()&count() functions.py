#Excersice no 7 - to Make a Love Calculator with using Upper()&count() functions

name1 = input("What is your name?")
name2 = input("What is his/her name? ")
combine_string = name1 + name2
Lower_case_string = combine_string.lower()
t = Lower_case_string.count('t')
r = Lower_case_string.count('r')
u = Lower_case_string.count('u')
e = Lower_case_string.count('e')

true = t + r + u + e

l = Lower_case_string.count('l')
o = Lower_case_string.count('0')
v = Lower_case_string.count('v')
e = Lower_case_string.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))
if love_score <10 or love_score >90:
    print(f"Your score is {love_score} and you go together like coke and mentos")
elif love_score >=40 and love_score <= 50:
    print (f"Your score is {love_score} and you are alright together")
else:
    print(f"Your love score is {love_score} ")

