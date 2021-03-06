import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" #Declaring the mapquest api.
key = "FTz1C80FGGEcX94YgmGdIunBTet31wex" #Declaring the api key.

def convert(value): #Value conversion for distance.

    if distUnit == "m" or distUnit == "meter" or distUnit == "Meter": 
        distance = value * 1610 
    elif distUnit == "km" or distUnit == "kilometer" or distUnit == "Kilometer": 
        distance = value * 1.61 
    elif distUnit == "mi" or distUnit == "miles" or distUnit == "Miles": 
        distance = value 

    return distance 

while True:

    orig = input("Starting Location: ") #User input for starting location or origin.
    if orig == "quit" or orig == "q":
        break

    dest = input("Destination: ") #User input for the destination.
    if dest == "quit" or dest == "q":
         break

    distUnit = input("Select a unit of distance/length (m, km, or mi): ") #User input for desired unit of distance.
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

    rType = input("Select preferred route type (FASTEST,SHORTEST, or BICYCLE): ") #User input for the desired route type.

    if rType =="quit" or rType =="q":
        break
    elif rType =="FASTEST" or rType =="Fastest" or rType == "fastest":
        routeType ="FASTEST"
    elif rType =="SHORTEST" or rType =="Shortest" or rType =="shortest":
        routeType ="SHORTEST"
    elif rType =="BICYCLE" or rType =="Bicycle" or rType =="bicycle":
        routeType ="BICYCLE"
    else:
        print("Please try again.")
        break
        

    avoidFeature = input("[Route Options] What do you want to avoid? (Limited Access Highway | Toll Road | Ferry | Unpaved | Approximate Seasonal Closure | Country Border Crossing | Bridge | Tunnel | None): ")
    
    #Create query strings
    if avoidFeature = "None":
        url = main_api + urllib.parse.urlencode({"key": key, "from":orig,"routeType": routeType ,"to":dest}) #Declaring the URL.
    
    else:
        url = main_api + urllib.parse.urlencode({"key": key, "from":orig,"routeType": routeType ,"to":dest, "avoids":avoidFeature}) #Declaring the URL.

    print("URL: " + (url))
    json_data = requests.get(url).json() #Requesting the url in json format.
    json_status = json_data["info"]["statuscode"] #Getting the status code. 
    if json_status == 0:

        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Distance " + "(" + unit + "):   " + str("{:.2f}".format(convert(json_data["route"]["distance"]))))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("Type of Route: " + (routeType))
        print("=============================================")

        for each in json_data["route"]["legs"][0]["maneuvers"]:

            distance = convert(each["distance"]) #Conversion of distance.
            est_time = each["formattedTime"]  #Declaring time format.

            print((each["narrative"]) + " || (Distance: " + str("{:.2f}".format(distance)) + " " + unit + ") || (Estimated Time: " + est_time + ")") #Printing each narrative.

        print("=============================================\n")

    elif json_status == 402: #Error code (Invalid user input).
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611: #Error code (Missing entry).
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else: #Getting status code.
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")







