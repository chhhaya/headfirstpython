#!/usr/local/bin/python3
import cgi
import os
import time
import sys
import yate
import sqlite3

print(yate.start_response('text/plain'))

addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']

cur_time = time.asctime(time.localtime())

print(host + ',' + addr + ',' + cur_time + ":" + method, file=sys.stderr)

# 所有的表单数据
form = cgi.FieldStorage()
for each_form_item in form:
    print(each_form_item + '-->' + form[each_form_item].value, end=' ', file=sys.stderr)
the_id = form['Athlete'].value
the_time = form
print(file=sys.stderr)
print("OK")