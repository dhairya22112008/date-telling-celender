q = int(input("enter day of month "))
m = int(input("enter month "))
if m == 1:
    m = 13
    j = int(input("enter century "))
    k = int(input("enter year "))
    if m == 13:
        k = k - 1
    h = (q + ((13*(m + 1)) // 5) + k + (k // 4) + (j // 4) + (5 * j))% 7
    if h == 0:
        print("saturday")
    elif h == 1:
        print("sunday")
    elif h == 2:
        print("monday")
    elif h == 3:
        print("tuesday")
    elif h == 4:
        print("wednesday")
    elif h == 5:
        print("thursday")
    elif h == 6:
        print("friday")
    else:
        print("check the enteries and try again")
else:
 j = int(input("enter century "))
 k = int(input("enter year "))
 if m == 13:
     k = k - 1
 h = (q + ((13*(m + 1)) // 5) + k + (k // 4) + (j // 4) + (5 * j))% 7
 if h == 0:
     print("saturday")
 elif h == 1:
     print("sunday")
 elif h == 2:
     print("monday")
 elif h == 3:
     print("tuesday")
 elif h == 4:
     print("wednesday")
 elif h == 5:
     print("thursday")
 elif h == 6:
     print("friday")
 else:
     print("check the enteries and try again")
a = input("press enter to exit")
   # This is a program that will tell you day on a particular day, i call it zelda

