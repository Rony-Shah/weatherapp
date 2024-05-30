#import flask library along with flask render template, request and requests
from flask import Flask, render_template, request
import requests
#initialize flask
app = Flask(__name__)
#Define visitor function to check how many visitor are there
@app.route('/')
def visitors():

    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    visitors_count = visitors_count + 1

    counter_write_file = open("count.txt", "w")
    counter_write_file.write(str(visitors_count))
    counter_write_file.close()
    return render_template('index.html', count=visitors_count)

    # Render HTML with count variable


# Add route for your webpage
@app.route('/', methods=['post'])
def weather_stats():
    # Load current count
    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()
    latitude = request.form['latitudeinput']
    longitude = request.form['longitudeinput']
    #Get latitude and longitude from the from
    api_url = 'https://weather-l6tl.onrender.com/api/getCurrentWeather/'+latitude+'/'+longitude
    response = requests.get(api_url)
    weather_data = response.json()
    print(weather_data)
    return render_template('index.html', weather=weather_data, count=visitors_count)
    # Call the weather api 'https://weather-l6tl.onrender.com/api/getCurrentWeather/'+latitude+'/'+longitude and return weather and visitor count while rendering index.html


#add code for executing flask
if __name__ == "__main__":
    app.run()
