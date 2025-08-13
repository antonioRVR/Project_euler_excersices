# <p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
# <p>What is the largest prime factor of the number $600851475143$?</p>

number=600851475143
divisor=2
factor_list=[]

while number>1:

    if number%divisor==0:

        factor_list.append(divisor)
        number=number//divisor
    else:
        divisor+=1

print("factors list: \n", factor_list)
print("We got the highest factor!!!", factor_list[-1])