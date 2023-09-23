import redis

r = redis.StrictRedis(host="host_name", port="port_number", password= "password")

# String key value pair push
r.set('foo', 'bar')
k = r.get('foo')
print(k)

# Hset creation or updation
r.hset('user-session:123', mapping={
    'name': 'Krishna Chaitanya',
    "surname": 'Kavali',
    "company": 'Redis',
    "age": 23
})
# True

print(r.hgetall('user-session:123'))