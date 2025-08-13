# <p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers
# is $9009 = 91 \times 99$.</p><p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>

largest_palindrome = 0

for a in range(999,0,-1):
    for b in range(a,0,-1):
        number=a*b

        if number <= largest_palindrome:
            break

        
        if str(number)==str(number)[::-1]:
            largest_palindrome=number
            

print("largest palindrome: ", largest_palindrome)
