def cake():
#case 1: To cut the cake into N equal pieces
    input1=int(input("How many parts do you want to cut the cake in: "))
    if 360%input1==0:
        print("Yes, you can cut the cake into",input1,"equal pieces")
    else:
        print("No, you can't cut the cake into",input1,"equal pieces")

#case 2: To cut the cake into N pieces of any size
    if input1 < 360:
        print("Yes, you can cut the cake into",input1,"pieces of any size")
    else:
        print("No, you can't cut the cake into",input1,"pieces of any size")

#case 3: To cut the cake into N pieces such that no two of them are equal
    if input1*(input1+1)/2 <= 360:
        print("Yes, you can cut the cake into",input1,"pieces such that no two of them are equal")
    else:
        print("No, you can't cut the cake into",input1,"pieces such that no two of them are equal")
switch = True
while switch:
    cake()
    again=input("Type 'Yes' if you want to run the program again type 'No' to exit: ")
    if again == 'No':
        switch = False
        print("Thank You!")