# Here, we use an efficient Fibonacci sequence generator (no recursion). The ith Fibonacci number is equal to the sum
#  of the (i-1)th (denote it b) and (i-2)th (denote it a) Fibonacci numbers, so we only need to keep track of those.

a = 1
b = 2
c = a+b

s = 2

while c < 4E6:
    if c % 2 == 0:
        s += c

    c = a+b

    a = b
    b = c

print "The answer is {0}".format(s)