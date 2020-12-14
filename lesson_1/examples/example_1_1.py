access = None
original_password = '123'
password = input('input password: ')
if password == original_password:
    access = True
if password != original_password:
    access = False
print('access:', access)
