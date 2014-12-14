#!/usr/local/bin/python3
import cgi
import athletemodel2
import yate
import sys

# 可在web页面上显示出错堆栈信息
import cgitb
cgitb.enable()


form_data = cgi.FieldStorage()
athlete_id = form_data['which_athlete'].value
athletes = athletemodel2.get_athlete_from_id(athlete_id)

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("Athlete:" + athletes['Name'] + ',Dob' + athletes['Dob'] + '.'))
print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athletes['top3']))
print(yate.include_footer({"Home": "/index.html",
                           "Select another athlete": "generate_list.py"}))