import json


def my_handler(event, context):
    message = 'Hello Nagaraju'
    return {
        'message': message
    }
