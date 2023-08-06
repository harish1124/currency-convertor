def hj():
    units=int(input("Enter your units calculated:"))
    if units>=0 and units<=100:
        print((units*0),a)
    elif units>100 and units<=200:
        print(((units-100)*2.25),a)
    elif units>200 and units<=400:
        print(((100*2.25)+((units-200)*4.5)),a)
    elif units>400 and units<=500:
        print(((100*2.25)+(200*4.5)+((units-400)*6)),a)
    elif units>500 and units<=600:
        print(((300*4.5)+(100*6)+((units-500)*8)),a)
    elif units>600 and units<=800:
        print(((300*4.5)+(100*6)+(100*8)+((units-600)*9)),a)
    elif units>800 and units<=1000:
        print(((300*4.5)+(100*6)+(100*8)+(200*9)+((units-800)*10)),a)
    elif units>1000:
        print(((300*4.5)+(100*6)+(100*8)+(200*9)+(200*10)+((units-1000)*11)),a)
    b = input("do u wanna continue? ")
    if b == "yes" or b == "YES":
        hj()
    else:
        print("seee u later")
a="rupess"
hj()