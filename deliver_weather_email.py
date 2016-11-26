#!/usr/bin/python3.4
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from datetime import date
from fetch_current_weather import get_weather_data
from jinja2 import Environment


def send_email():
    username = 'weather@piard.de'
    password = 'abcd12345678'
    fromaddr = 'weather@piard.de'
    toaddr = ['heinrich@piard.de']
    current_weather = (get_weather_data())
    weather = current_weather
    print(weather)
    location = weather[0]
    temperature = weather[1]
    humidity = weather[2]
    clouds = weather[3]
    if weather[3] == 'Clouds: CLEAR SKY':
        cloudsimg = 'http://openweathermap.org/img/w/01d.png'
    elif weather[3] == 'Clouds: FEW CLOUDS':
        cloudsimg = 'http://openweathermap.org/img/w/02d.png'
    elif weather[3] == 'Clouds: SCATTERED CLOUDS':
        cloudsimg = 'http://openweathermap.org/img/w/03d.png'
    elif weather[3] == 'Clouds: BROKEN CLOUDS':
        cloudsimg = 'http://openweathermap.org/img/w/04d.png'
    elif weather[3] == 'Clouds: OVERCAST CLOUDS':
        cloudsimg = 'http://openweathermap.org/img/w/04d.png'
    elif weather[3] == 'Clouds: SHOWER RAIN':
        cloudsimg = 'http://openweathermap.org/img/w/09d.png'
    elif weather[3] == 'Clouds: RAIN':
        cloudsimg = 'http://openweathermap.org/img/w/10d.png'
    elif weather[3] == 'Clouds: THUNDERSTORM':
        cloudsimg = 'http://openweathermap.org/img/w/11d.png'
    elif weather[3] == 'Clouds: SNOW':
        cloudsimg = 'http://openweathermap.org/img/w/13d.png'
    elif weather[3] == 'Clouds: MIST':
        cloudsimg = 'http://openweathermap.org/img/w/50d.png'
    print(cloudsimg)

    html ="""
        <!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.01 Transitional//EN'>
        <html lang='en'>
        <head>
        <title>Your weather report</title>
        </head>
        <body>
        Here is your weather report.<br>
        <img src="{{cloudsimg}}" alt="{{clouds}}">
        <ul class='mylist'>
        <li class='myitem'>{{location}}</li>
        <li class='myitem'>{{temperature}}</li>
        <li class='myitem'>{{humidity}}</li>
        <li class='myitem'>{{clouds}}</li>
        </ul>
        <p>Thank you for using our service!</p>
        </body>
        </html>"""
    email_content_html = Environment().from_string(html).render(location=location, temperature=temperature,
                                                                humidity=humidity, clouds=clouds, cloudsimg=cloudsimg)
    #text_in_body = "Today\'s weather: " + str(date.today()) + "\n\n\n\n" + weather + "\n\n\n\n"
    #print(type(weather))
    #print(weather)

    for each_recipient in toaddr:
        msg = MIMEMultipart()
        msg["Subject"] = "Weather Report " + str(date.today())
        msg["From"] = fromaddr
        msg["To"] = each_recipient
        #part1 = MIMEText(text_in_body, 'plain')
        part2 = MIMEText(email_content_html, 'html')
        msg.attach(part2)
        #msg.attach(part1)
        server = smtplib.SMTP('smtp.strato.de:587')
        server.set_debuglevel(False)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, each_recipient, msg.as_string())
        server.quit()
        print('sent email to ' + each_recipient)

send_email()
