import redis



if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('foo', 'bar')
    r.get('foo')
    r.scan(0)