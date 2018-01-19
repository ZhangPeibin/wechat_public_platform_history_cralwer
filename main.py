#!/usr/bin/env
# coding=utf-8

import redis

"""
核心入口文件
我们订阅redis的topic
调用{@link uiauto.py}去处理
"""

host = "127.0.0.1"
port = 6379
channel = ()


class Task(object):
    def __init__(self):
        self.__pool__ = redis.ConnectionPool(host=host, port=port)
        self.__conn__ = redis.Redis(connection_pool=self.__pool__)
        self.__pubsub__ = self.__conn__.pubsub()
        self.__pubsub__.subscribe(channel)

    def list_task(self):
        for i in self.__pubsub__.listen():
            print "Task get", i


if __name__ == "__main__":
    print "list task "
    Task().list_task()