access = None
original_password = '123'
password = input('input password: ')
if password == original_password:
    access = True
else:
    access = False
print('access:', access)
