# A prime number is a number that is only divisible
# by one and itself

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("This is a Prime Number.")
    else:
        print("This is not a Prime Number.")


n = int(input("Check This Number: "))
prime_checker(number=n)