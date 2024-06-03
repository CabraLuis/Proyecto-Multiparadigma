import pymysql
import pymysql.cursors


def connect():
    return pymysql.connect(host="localhost", user="cabra", password="3000", db="goat", cursorclass=pymysql.cursors.DictCursor)
