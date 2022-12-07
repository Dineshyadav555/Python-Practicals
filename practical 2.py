# WAP to accept a number ‘n’ and
# j. Check if ’n’is prime
# k. Generate all prime numbers till ‘n’
# l. Generate first ‘n’ prime numbers This program may be done using functions

num = int(input('Enter a number: '))

prime = True
prime_nos = []
n_prime_nos = []

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            prime = False
            # break

else:
    print('Wrong Input')

if prime == True:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number")

for a in range(1, num+1):


       for i in range(2, a):
           if (a % i) == 0:
               break
       else:
            prime_nos.append(a)

print("Prime numbers till ",num, " are ",prime_nos)






