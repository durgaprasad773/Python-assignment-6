'''You're required to write a program that reads an amount A and prints the minimum number of various rupee notes required for the given amount. The denominations are 2000, 500, 200, 50, 20, 5, 2, and 1.'''


a=int(input())

two_thousands = a // 2000
remain_two_thousand = a % 2000

five_hundred = remain_two_thousand // 500
remain_five_hundred = remain_two_thousand % 500

two_hundred = remain_five_hundred // 200
remain_two_hundred = remain_five_hundred % 200

fifty = remain_two_hundred // 50
remain_fifty = remain_two_hundred % 50

twenty = remain_fifty // 20
remain_twenty = remain_fifty % 20

five = remain_twenty // 5
remain_five = remain_twenty % 5

two = remain_five // 2
remain_two = remain_five % 2


res = "2000:"+str(two_thousands) + " 500:" + str(five_hundred) +" 200:"+str(two_hundred) +" 50:"+str(fifty) +" 20:" +str(twenty)+" 5:"+str(five)+" 2:"+str(two) +" 1:"+str(remain_two)
print(res)