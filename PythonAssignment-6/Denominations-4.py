'''The program's goal is to calculate the minimum number of currency notes of denominations 100, 50, 20, and 10 rupees required to make up a given amount A. The program should print the count of each denomination needed, starting from the highest denomination and going down to the lowest.
Example for Clarity:

If the given amount A is 370:
The number of 100 rupee notes is 370 // 100 = 3, and the remaining amount is 370 - 300 = 70.
The number of 50 rupee notes is 70 // 50 = 1, and the remaining amount is 70 - 50 = 20.
The number of 20 rupee notes is 20 // 20 = 1, and the remaining amount is 20 - 20 = 0.
There are no 10 rupee notes required.
The output will be:
  100 Notes: 3
  50 Notes: 1
  20 Notes: 1
  10 Notes:
'''

a=int(input())

hundred = a // 100
remain = a%100

fifty = remain //50
remain_fifty = remain % 50

twenty = remain_fifty // 20
remain_twenty = remain_fifty % 20

tens = remain_twenty //10

print("100 Notes:",hundred)
print("50 Notes:",fifty)
print("20 Notes:",twenty)
print("10 Notes:",tens)