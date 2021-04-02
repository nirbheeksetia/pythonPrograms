if __name__ == "__main__":
    def add():
        one = input("Number One:")
        two = input("Number Two:")
        print( int(one) + int(two))

    def multiply():
        three = input("Number three:")
        four = input("Number four:")
        m = int(three) * int(four)
        print(m)

    addormultiply = input("Wuld you like to add or multiply?(add/multiply):")

    if addormultiply != "add" or addormultiply != "multiply":  
        print("Wrong Input!")
        #addormultiply = input("Wuld you like to add or multiply?(add/multiply):")
        multiply()

    elif addormultiply == "multiply":
        multiply()
    elif addormultiply == "add":
        add()





