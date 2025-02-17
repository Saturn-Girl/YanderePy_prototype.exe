#GraphicsApi.py

choice = input("select data from GraphicsApi A algebra data B circumference C Area D power of 2  E cirlce data > ")

if choice == "A":
    C = 10
    A = 10
    N = 1
    dat1 = int(C) / int(A)
    dat2 = int(dat1) + int(N)
    print(f"Collected data from GraphicsApi answear is {dat2}")
    input("press any key to exit")

elif choice == "B":
    X = 3.14
    Y = 2
    dat3 = float(X) * float(Y)
    print(f"Collected data from GraphicsApi answear is {dat3}")
    input("press any key to exit")

elif choice == "C":
    X = 3.14
    Y = 2
    Z = 2
    dat4 = float(X) * float(Y)
    dat5 = float(dat4) * float(Z)
    print(f"Collected data from GraphicsApi answear is {dat5}")
    input("press any key to exit")

elif choice == "D":
    dat6 = 100
    dat7 = 100
    sum = int(dat6) + int(dat7)
    print(f"Collected data from GraphicsApi answear is {sum}")
    input("press any key to exit")
    
elif choice == "E":
    dat8 = 1.2
    dat9 = 5
    dat10 = float(dat8) * float(dat9)
    print(f"Collected data from GraphicsApi answear is {dat10}")
    input("press any key to exit")

else:
    print("select choice from A B C D E")
   
    
    
