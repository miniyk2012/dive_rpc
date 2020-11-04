import redis


# redis/connection.py中打印了日志, 可以看到redis协议的最初形式
if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('foo', 'bar')
    r.get('foo')
    r.scan(0)