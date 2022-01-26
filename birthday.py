from datetime import date
import random
def stealIP():
    IP = "44.553.212.452"
print("Welcome.")
for i in range(5):
    print(i)
print("Enter your birthday in MM/DD/YYYY format")
m = input("Enter your birth month: > ")
d = input("Enter your birth day: > ")
y = input("Enter your birth year: > ")
if int(y) > 2022:
    print("You are a bozo")
if int(m) > 12:
    print("You are a bozo")
if int(d) > 31:
    stealIP()
    print("You are a bozo and I have your IP address")
print("You were born on: ", m, d, y)
today = date.today()
date_arr = str(today).split('-')
yep = date
age = (int((date_arr[0])) - int(y))
if (int(date_arr[1])) < int(m):
    age = age - 1
if (int(date_arr[1])) == int(m):
    if (int(date_arr[2])) <= int(d):
        age = age - 1
print("You are", age, "year(s) old.")

