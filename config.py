#coding=utf-8
import os
settings = dict(
        static_path = os.path.join(os.path.dirname(__file__), "static"),
        cookie_secret = "5f7ff94067154b65a8765862e4de163",
        xsrf_cookies = True,
        debug = True
                )

mysql_options = dict(
        host = '127.0.0.1',
        database = 'ihome',
        user = 'root',
        password = "0215"
)

redis_options = dict(
        host = "127.0.0.1",
        port = 6379
)

log_path = os.path.join(os.path.dirname(__file__),"logs/log")
log_level = 'info'

passwd_hash_key = "5f7ff94067154b65a8765862e4de163b"