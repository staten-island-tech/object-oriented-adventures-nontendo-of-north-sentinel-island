user = {'hp':45}
def test(user):
    user['hp'] = user['hp'] - 5
    return user['hp']
def test2(user):
    user['hp'] = user['hp'] + 5
    return user['hp']

test2(user)
print(user)


