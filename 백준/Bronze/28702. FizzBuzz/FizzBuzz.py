for i in range(3, 0, -1):
    w = input()
    if w not in ['Fizz', 'Buzz' ,'FizzBuzz']:
        n = int(w) + i
        break
print('Fizz' * (n % 3 == 0) + 'Buzz' * (n % 5 == 0) or n)