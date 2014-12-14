#!/usr/local/bin/python3
import athletemodel2
import yate
# import glob

# data_files = glob.glob("data/*.txt")
# athletes = athletemodel2.put_to_store(data_files)
athletes = athletemodel2.get_namesID_from_store()

print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("select an athlete from the list to work with:"))
for e in athletes:
    print(yate.radio_button_id("which_athlete", e[0], e[1]))
print(yate.end_form("Select"))
print(yate.include_footer({"Home": "/index.html"}))