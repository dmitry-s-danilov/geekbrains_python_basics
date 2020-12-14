class User:
    """this is a documentation string"""
    __count = 0

    @classmethod
    def count(cls):
        return cls.__count

    # constructor
    def __init__(self, name, login, password, email):
        User.__count += 1
        self.__id = User.__count
        self.name = name
        self.login = login
        self.password = password
        self.email = email
        print(f'user {self.__id} created')

    # def __setattr__(self, key, value):
    #     if key in ('password', 'email'):
    #         self.__dict__[key] = value
    #         print(f'user {self.__id}',
    #               f'attribute {key}',
    #               f'changed to be {value}',
    #               sep=' ')
    #     else:
    #         print(f'attribute {key} is invalid')

    # string representation of object
    def __str__(self):
        return '\n'.join((f'name: {self.name}',
                          f'login: {self.login}',
                          f'password: {self.password}',
                          f'email: {self.email}'))

    # destructor
    def __del__(self):
        print(f'user {self.__id} deleted')
        User.__count -= 1


    # @classmethod
    # def on_get_attributes(cls):
    #     print(f'__name__ {cls.__name__}',  # class name
    #           f'__module__ {cls.__module__}',  # module name
    #           f'__dict__ {cls.__dict__}',  # attributes dict
    #           f'__bases__: {cls.__bases__}',  # base classes tuple
    #           f'__doc__: {cls.__doc__}',  # documentation string
    #           f'__class__: {cls.__class__}',  #
    #           f'__init__: {cls.__init__}',  # constructor
    #           f'__hash__: {cls.__hash__}',  # hash
    #           sep='\n')


print(f'User count: {User.count()}')

user = User('John Doe', 'john_doe', '123456', 'john.doe@gmail.com')

print(user)
print(f'User count: {User.count()}')

del user
print(f'count: {User.count()}')




