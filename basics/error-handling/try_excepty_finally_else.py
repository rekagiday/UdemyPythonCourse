while True:
    try:
        num = int(input("please enter a number! "))
    except:
        print("Thats not a number!")
    else:
        print("Thank you!")
        break
    finally:
        print("this runs no matter what")
