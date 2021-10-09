import json
import csv

with open ('covid_cases.json','r') as covids: #Read the json file
    data = json.loads(covids.read()) #Load the json file

with open('parsed_data','w', newline='') as json_parsed: #Created a csv of parsed data
    csv_file = csv.writer(json_parsed)
    csv_file.writerow(["dateRep","countriesAndTerritories","cases","deaths"]) #instruction for rows

    for lists in data["records"]: #created rows
        csv_file.writerow([lists["dateRep"],
        lists["countriesAndTerritories"],
        lists["cases"],
        lists["deaths"]])


