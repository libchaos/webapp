import cgi

import athletemodel
import yate

import cgitb

cgitb.enable()

athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
athlete_name = form_data['which athlete'].value

print(yate.start_response())

print(yate.include_header("Coach libchaos's timing data"))

print(yate.header("Athlete:" + athlete_name + ", DOB:" + athletes[athlete_name].dob+"."))

print(yate.para("the top times for this athletes are:"))

print(yate.u_list(athletes[athlete_name].top3))

print(yate.include_footer({"Home":"/index.html", "Select another athlete":"generate_list.py"}))
