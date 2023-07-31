import mysql.connector
import configparser

from _pytest.config import Config


def getConn():
    conn = mysql.connector.connect(host='127.0.0.1', database='QADBT', user='root', password='root')
    if conn.is_connected():
        return conn


def get_env_data():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def getQuery(query):
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()

    return row


def get_password():
    return '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'

