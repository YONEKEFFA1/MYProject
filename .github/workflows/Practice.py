print ("Welcome to the Basic Calculator")
count = 0
history = []
fullhistory = []
counter = 0
while(True):
    if count == 0:
        num1 = float(input("Enter First Number : "))
        history.append(num1)
        fullhistory.append(num1)
        counter +=1
        count+=1
    op = input("""Enter an Operator (+,-,*,/) C for Clear E for Exit
    H for History P for Previuos N for Next : """)
    if op == "n" or op == "N":
        if (len(history) >= 1 and len(history) > counter):
            print(history[counter])
            counter+=1
            continue
        else:
            print("No Next Elements")
            continue
    if op == "p" or op == "P":
        if (len(history) > 0 and counter > 0):
            counter-=1
            print(history[counter])
            continue
        else:
            print("No previous Elements Left")
            continue
    if op == "C" or op =="c":
        count=0
        del history[0::]
        continue
    if op == "e" or op =="E":
        file = open("fullhistory.txt","w")
        file.close()
        file = open("fullhistory.txt","a")
        file.write(str(fullhistory));
        file.write("\n")
        file.close()

        break
    if op == "h" or op =="H":
        print (history)
        continue
    counter = len(history)
    num2 = float (input("Enter Second Number: "))
    counter +=1
    history.append(num2)
    res = 0.0
    fullhistory.append(op)
    fullhistory.append(num2)
    if (op == "+"):
        res = num1 + num2
    elif (op == "-"):
        res = num1 - num2
    elif (op == "*"):
        res = num1 * num2
    elif (op == "/"):
        res = num1 / num2
    else:
        res = 0
        print ("Invalid Operator")
        continue
    print ("Result of %.3f %s %.3f= : %.3f" % (num1,op,num2,res))
    num1 = res
