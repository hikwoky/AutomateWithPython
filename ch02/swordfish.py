while True:
    print('What is your name?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello Joe.  What is the password?')
    password = input()
    if password == 'swordfish':
        break
    print('Access granted.')    # This will never be reached