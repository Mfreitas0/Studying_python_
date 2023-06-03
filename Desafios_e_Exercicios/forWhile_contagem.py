"""
PROPOSTA DO EXERCICIO

for / while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
9 1
10 0
...
"""

a = 0
b = 10

while a < 10:
    a += 1

    while b > 0:
        b -= 1
        print(a, b)
        break

print('Fim!')
print()


# 
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
