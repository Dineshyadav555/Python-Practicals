# WAP to create a pyramid of the character ‘*’ and a reverse pyramid

rows = int(input('Enter number of rows: '))

for i in range(rows):
    for j in range(2*i+1):
        print('*', end='')
    print()

for i in range(rows,0,-1):
    for j in range(2*i-1):
        print('*', end='')
    print()