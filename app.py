from flask import Flask, render_template, request
import urllib.parse
import requests

app = Flask(__name__)

main_api = "https://www.mapquestapi.com/directions/v2/route?" #Declaring the mapquest api.
key = "FTz1C80FGGEcX94YgmGdIunBTet31wex" #Declaring the api key.

def convert(value, distance_unit): #Value conversion for distance.

    if distance_unit == "m" or distance_unit == "meter" or distance_unit == "Meter": 
        distance = value * 1610 
    elif distance_unit == "km" or distance_unit == "kilometer" or distance_unit == "Kilometer": 
        distance = value * 1.61 
    elif distance_unit == "mi" or distance_unit == "miles" or distance_unit == "Miles": 
        distance = value 

    return distance

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/route', methods=['GET', 'POST'])
def route():

    if request.method == 'POST':

        starting_point = request.form['starting_point']
        destination_point = request.form['destination_point']
        distance_unit = request.form['distance_unit']
        route_type = request.form['route_type']
        route_avoid = request.form['route_avoid']

        if route_avoid == "None":
            url = main_api + urllib.parse.urlencode({"key": key, 
                                                "from": starting_point,
                                                "routeType": route_type,
                                                "to": destination_point}) 
        else:
            url = main_api + urllib.parse.urlencode({"key": key, 
                                                "from": starting_point,
                                                "routeType": route_type,
                                                "to": destination_point, 
                                                "avoids": route_avoid}) 

        json_data = requests.get(url).json()

        json_status = json_data["info"]["statuscode"]

        duration = json_data["route"]["formattedTime"]
        distance = str("{:.2f}".format(convert(json_data["route"]["distance"], distance_unit)))
        fuel = str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78))

        maneuvers = json_data["route"]["legs"][0]["maneuvers"]

        return render_template('output.html', starting_point = starting_point, 
                                                destination_point = destination_point,
                                                duration = duration,
                                                distance = distance,
                                                distance_unit = distance_unit,
                                                fuel = fuel,
                                                route_type = route_type,
                                                maneuvers = maneuvers)

    return render_template('home.html')

if __name__ == '__main__':
    app.run()