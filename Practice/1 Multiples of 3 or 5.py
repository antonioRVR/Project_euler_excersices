#solved

# <p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these4
# multiples is $23$.</p>
# <p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>

sum=0
a=3

def mult_5(number):
    if number%5==0:
        return True
    else:
        return False


def mult_3(number):
    if number%3==0:
        return True
    else:
        return False
    
while a<1000:
    if mult_3(a) or mult_5(a):
        sum+=a
    a+=1

print("sum is: ", sum)