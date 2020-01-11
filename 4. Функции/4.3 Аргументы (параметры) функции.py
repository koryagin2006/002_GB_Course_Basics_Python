def hello_max():
    print('Hello, Max')


hello_max()


def hello(who):
    print('Hello,', who)


hello('Leo')


def greeting(who, say):
    print(say, who)


greeting('Leo', 'Hi')

# передача параметром возможна также по имени
greeting(say='Hi', who='Leo')


# Можно задавать значение по-умолчанию
def greeting(who, say='Hello'):
    print(say, who)


greeting('Leo')  # Hello Leo


def greeting(say, *args):
    print(say, args)


greeting('Hello', 'Leo', 'Max', 'Kate')


def get_person(**kwargs):
    print(kwargs)
    # for k, w in kwargs.items():
    #     print(k, w)


get_person(name='Leo', age=20, has_car=True)