# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

# Sample Json
userJSON = '{"first_name": "Alice", "last_name": "Cooper","age": 90}'

# Pare to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

car = {
    'make': 'Ford',
    'model': 'Mustang',
    'year': 1970
}

carJSON = json.dumps