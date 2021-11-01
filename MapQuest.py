import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "FTz1C80FGGEcX94YgmGdIunBTet31wex"

def convert(value): 

    if distUnit == "m" or distUnit == "meter" or distUnit == "Meter": 
        distance = value * 1610 
    elif distUnit == "km" or distUnit == "kilometer" or distUnit == "Kilometer": 
        distance = value * 1.61 
    elif distUnit == "mi" or distUnit == "miles" or distUnit == "Miles": 
        distance = value 

    return distance 

while True:

    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break

    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
         break

    distUnit = input("Select a unit of distance/length (m, km, or mi): ")
    if dest == "quit" or dest == "q":
        break
    elif distUnit == "m" or distUnit == "meter" or distUnit == "Meter":
        unit = "m"
    elif distUnit == "km" or distUnit == "kilometer" or distUnit == "Kilometer":
        unit = "km"
    elif distUnit == "mi" or distUnit == "miles" or distUnit == "Miles":
        unit = "mi"
    else:
        print("Please try again.")
        break
        
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:

        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Distance " + "(" + unit + "):   " + str("{:.2f}".format(convert(json_data["route"]["distance"]))))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")

        for each in json_data["route"]["legs"][0]["maneuvers"]:

            distance = convert(each["distance"])

            print((each["narrative"]) + " (" + str("{:.2f}".format(distance) + " " + unit + ")"))

        print("=============================================\n")

    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")







