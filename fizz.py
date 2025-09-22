# fizzbuzz

# 1부터 임의의 양의 정수에 대해
# i가 5의 배수라면, fizz

for i in range(1, 15+1):
    if i % 3 == 0:
        print('fizz')
    else:
        print(i)
