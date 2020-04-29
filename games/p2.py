
def fibonacci(second_last, last):
    next_num = second_last + last
    return next_num

def call_fib():
    even_fib_numbers = [2]
    second_last = 1
    last = 2
    fib_number = 0 
    while fib_number < 4000000:
        fib_number = fibonacci(second_last, last)
        if fib_number%2==0:
            even_fib_numbers.append(fib_number)
        second_last = last
        last = fib_number
    total = sum(even_fib_numbers)
    print(even_fib_numbers)
    print(fib_number)
    print("total: {0}".format(total))

if __name__ == '__main__':
    call_fib()

