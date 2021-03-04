stop = ''
while stop != 'n':
    user_num = int(input("Enter a number to check if it is prime:\n"))
    count = 2
    prime = True
    while count <= (user_num / 2):
        if user_num % count == 0:
            prime = False
            break
        count += 1
    print(user_num, 'is prime') if prime else print(user_num, 'is not prime')
    stop = input('enter n to stop, or anything else to continue.')