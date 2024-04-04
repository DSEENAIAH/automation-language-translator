while True:
    print(" 1.Triangle \n 2.circle \n 3.square \n 4.Rectangle \n 5.parallagram \n 6.Rhombus \n ")
    a=(int(input("enter a option: ")))

    if(a==1):
        b=(float(input("base: ")))
        c=(float(input("height: ")))
        d= 1/2 * (b * c)
        print(d)
    elif(a==2):
        b=(float(input("radius: ")))
        c= 3.14
        d= b**2
        e= c*d
        print(e)
    elif(a==3):
        b=(float(input("length: ")))
        c= b*b
        print(c)
    elif(a==4):
        b=(float(input("lenght: ")))
        c=(float(input("bredth: ")))
        d= b * c
        print(d)
    elif(a==5):
        b=(float(input("base: ")))
        c=(float(input("height: ")))
        d= b * c
        print(d)
    elif(a==6):
        b=(float(input("base: ")))
        c=(float(input("height: ")))
        d= b * c
        print(d)
    else:
        print("error")