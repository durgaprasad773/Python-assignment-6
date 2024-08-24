'''You are given the weekday of the first day of the month and a positive integer N. Your task is to determine the day of the week for the Nth day of that month. To do this, you need to consider the calendar for that month and calculate the day of the week.

For example, if the first day of the month is Monday and N is 16, you need to find out which day of the week falls on the 16th day of the month.'''

d=input()
n=int(input())

if d=="Sunday":
    day=0
elif d=="Monday":
    day=1
elif d=="Tuesday":
    day=2
elif d=="Wednesday":
    day=3
elif d=="Thursday":
    day=4
elif d=="Friday":
    day=5
elif d=="Saturday":
    day=6
target_date = n+day-1
#print(target_date)
target_date = target_date % 7


if target_date ==0:
    print("Sunday")
elif target_date ==1:
    print("Monday")
elif target_date ==2:
    print("Tuesday")
elif target_date == 3:
    print("Wednesday")
elif target_date ==4:
    print("Thursday")
elif target_date ==5:
    print("Friday")
elif target_date ==6:
    print("Sunday")
