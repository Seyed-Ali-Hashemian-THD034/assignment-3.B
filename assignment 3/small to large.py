#small to large
x =list(input('Please enter your numbers. Example: 8, 9, 13, ... .').split(','))
for  i in range (len(x)-1):
    if x[i]>x[i+1]:
        print("Array values are sorted from small to large ")
        break
    else :
        print("Array values are not sorted from small to large ")
        break