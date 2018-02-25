import sys
import time
import math

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

start = time.time()
i = 0
divisors = 0
trinum = 0
#bight =

while divisors < 500:
    i += 1
    trinum += i
    bight = int(math.sqrt(trinum))

    divisors = 1 #itself

    #print(str(trinum) + " is divisible by:")

    for j in range(1, int(trinum/bight) + 1):
        if trinum % j == 0:
            #print(" * " + str(j))
            divisors +=1

    for k in range(2, bight):
        if trinum % k == 0:
            #print(" * 1/" + str(k) + " (" + str(trinum / k) + ")")
            divisors +=1

    #print " * " + str(trinum)
            
    #print str(trinum) + " has " + str(divisors) + " divisors"
        
print("The first triangle number with to have over 500 divisors at " + str(divisors) + " divisors is " + str(trinum))

end = time.time()
sys.exit("Elapsed: "+str(end - start)+" with a bight of the square root of the triple number")

