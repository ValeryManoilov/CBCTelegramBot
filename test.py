import redis

r = redis.Redis(host='localhost', port=6380, db=0, username='ValeryManoilov', password='Pineapple0399')

try:
    info = r.info()
    print(info['redis_version'])
    response = r.ping()
    if response:
        print("Подключение успешно!")
    else:
        print("Не удалось подключиться к Redis.")
except redis.exceptions.RedisError as e:
    print(f"Ошибка: {e}")