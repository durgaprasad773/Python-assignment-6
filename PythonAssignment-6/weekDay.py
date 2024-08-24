'''The program is designed to categorize the days of a week into three types based on a given day number: Week Start, Midweek, or Weekend.

Days are represented by numbers 1 through 7.
Monday and Tuesday, represented by numbers 1 and 2, are categorized as Week Start.
Wednesday, Thursday, and Friday, represented by numbers 3, 4, and 5, are categorized as Midweek.
Saturday and Sunday, represented by numbers 6 and 7, are categorized as Weekend.'''


a=int(input())

if a==1 or a==2:
    print("Week Start")
elif a==3 or a==4 or a==5:
    print("Midweek")
else:
    print("Weekend")