import os
# app.py


def greet(name):
    return f"Hello, {name}! {os.getenv('GREETING_SUFFIX', 'Have a great day!')}"


print(greet("World"))
