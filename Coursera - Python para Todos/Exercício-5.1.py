"""5.1 Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, 
count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except
and print an error message and skip to the next number"""
number = 0;
total = 0.0;

while True:
    sval = input("Enter a number: ");
    if(sval == "done"):
        break;
    try:
        fval = float(sval);
    except:
        print("Invalid input");
        continue;
    #fval = float(sval);
    print(fval);
    number = number + 1;
    total = total + fval;

#print("ALL DONE");
print(total, number, total / number);