#!/bin/env python
import redis,sys

ip = "127.0.0.1"
port = "6379"
password = ""
db = 0

redis_conn = redis.StrictRedis(host=ip, port=port, db=db,password=password)
info_list = redis_conn.info()

if sys.argv[1] in info_list:
    	print info_list[sys.argv[1]]

elif sys.argv[1] == "dbsize":
	print redis_conn.dbsize()
else:
	try:
		print redis_conn.config_get(sys.argv[1])[sys.argv[1]]
	except:
		print sys.argv[1] + " is not found"
