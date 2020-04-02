import csv
import json 

def notofficial(x):
	s = ''
	count = 0
	for i in range(0,len(x)):
		if(x[i]==' '):
			s = s + 'x'
			count = count + 1
		else:
			s = s + x[i]
	if s.isalpha()==False and count==0 and s.islower() == True :
		return True
	else:
		return False

csvname = "projects.csv"
jsonname = "students.json"
print("Give name of CSV file: ")
csvname = input()
print("Give name of JSON file: ")
jsonname = input()
print("NOT Official Names are: ")
projects = []
csvfile=open(csvname, encoding = "utf-8")
csvread = csv.reader(csvfile)
for row in csvread:
	if(notofficial(row[0])==True):
		print(row[0])
	else:
		projects.append(row)
csvfile.close()
print("\nJSON Name Matching Starts\n")
jsonfile = open(jsonname)
data = json.load(jsonfile)
for student in data:
	for row in projects:
		if row[0] == student["n"]:
			print("Name:  " + row[0] + "  Roll No: " + student["i"] + "  Branch: " + student["d"] + "  Organisation:  " + row[1] + "  Project:  " + row[2])
jsonfile.close()