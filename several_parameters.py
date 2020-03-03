# **args => multiple keywords arguments
# plusieurs paramètres nommés


def save_user(**user):
    print(user["name"])


save_user(id=1, name="John", age=22)  # => value of the key of dictionary
