sum = 10
def cal():
    global sum
    sum = 20
    sum = sum + 10
    currentSum = 200
    total = sum + currentSum
    print (total)
cal();
print (sum)