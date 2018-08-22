#coding:utf-8
import redis

r = redis.Redis(host='0.0.0.0', port=6379)
r.set('name', 'test')
