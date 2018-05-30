#!/usr/bin/python

import rospy
from std_msgs.msg import String
from diagnostic_msgs.msg import DiagnosticArray
import MySQLdb
import random

import os
mysql_server = os.environ['MYSQL_SERVER']

db = MySQLdb.connect(host=mysql_server,
                     user="root",
                     passwd="root",
                     db="test")


def callback(data):
    battery_level = data.status[18].values[0].value
    temperature = data.status[1].values[0].value
    cur = db.cursor()
    query = "INSERT INTO test_data (`battery_level`, `temperature`) VALUES ({}, {})".format(battery_level, temperature)
    cur.execute(query)
    db.commit()

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/diagnostics", DiagnosticArray, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        db.close()
