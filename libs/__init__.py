from redis import Redis

config = {
    'host': '47.102.218.113',
    'password':'1qaz2wsx',
    'port': 6379,
    'db': '9',
    'decode_responses': True
}

rd_client = Redis(**config)

if __name__ == '__main__':
    rd_client.keys('*')



