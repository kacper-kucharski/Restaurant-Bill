print('Please enter the value of the bill you have to pay')
AMOUNT = int(input())

print('Please enter the amount of 100, 20 and 1 banknotes in your wallet')
P = int(input())
Q = int(input())
R = int(input())

ways = 0

combinations = []

for x in range(P+1):
    for i in range(Q+1):
        for j in range(R+1):
            if AMOUNT - ((j*1) + (i*20) + (x*100)) == 0:
                ways += 1
                combination = str(x) + ' x 100, ' + str(i) + ' x 20, ' + str(j) + ' x 1'
                combinations.append(combination)

print('\nThere are ' + str(ways) + ' ways to pay this bill')
for e in combinations:
    print(e)