'''Write a program that reads a distance D in km and calculates the score.
For the first 50 km (050 km), the score for each km is 3.
. For the next 50 km (51-100 km), the score for each km is 5.
• For the next 100 km (101-200 km), the score for each km is 6.
For the distance above 200 km, the score for each km is 10.
• Apart from the above scores, there is a bonus score of 100
Input
The input will be a single line containing an integer representing D
Output
The output should be a single line containing an integer that is the score.'''


d=int(input())
bonus = 100
if d<= 50:
    val= (d*3) + bonus
    print(val)
elif d> 50 and d <=100:
    val = (50*3) + ((d-50) * 5) + bonus
    print(val)
elif d>100 and d <= 200:
    val = (50*3) + (50*5) +((d-100) *6) + bonus
    print(val)
else:
    val = (50*3) + (50*5) +(100*6) + ((d-200) * 10) + bonus
    print(val)