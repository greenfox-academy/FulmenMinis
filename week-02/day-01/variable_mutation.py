#1
a = 3
# make it bigger by 10
a += 10
print(a)

#2
b = 100
# make it smaller by 7
b -= 7
print(b)

#3
c = 44
# please double c's value
c *= 2
print(c)

#4
d = 125
# please divide by 5 d's value 
d /= 5
print(d)

#5
e = 8
# please cube of e's value
e **= 3
print(e)

#6
f1 = 123
f2 = 345
# tell if f1 is bigger than f2 (pras a boolean)
if f1 > f2:
    print ('bigger')
if f1 < f2:
    print ("smaller")

#7
g1 = 350
g2 = 200
# tell if the double of g2 is bigger than g1 (pras a boolean)
if g1 > g2 * 2:
    print ('bigger')
if g1 < g2 * 2:
    print ("smaller")

#8
h = 1357988018575474
h %= 11
print (h)
# tell if it has 11 as a divisor (pras a boolean)
if h > 0:
    print (False) 
if h <= 0:
    print (True)

#9
i1 = 10
i2 = 3
# tell if i1 is higher than i2 squared and smaller than i2 cubed (pras a boolean)
if i1 > i2 ** 2 and i1 < i2 ** 3:
    print (True)
else:
    print (False)

#10
j = 1521
# tell if j is dividable by 3 or 5 (pras a boolean)
if (j % 3) == 0 or (j % 5) == 0:
    print (True)
else:
    print (False)

#11
k = "Apple"
#fill the k variable with its cotnent 4 times
k = [k * 4]
print(k)
