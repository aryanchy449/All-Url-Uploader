import ast
import redis
import os



if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

INFO = Config.REDIS_URI.split(":")

DB = redis.StrictRedis(
    host=redis-19292.c251.east-us-mz.azure.redns.redis-cloud.com,
    port=19292,
    password="SjEOvX0VEvxV6UBuY7wherS6BmrsX6v5",
    charset="utf-8",
    decode_responses=True,
)

def get_stuff(WHAT):
    n = []
    cha = DB.get(WHAT)
    if not cha:
        cha = "{}"
    n.append(ast.literal_eval(cha))
    return n[0]
