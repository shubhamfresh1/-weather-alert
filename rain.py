import requests
from twilio.rest import Client # create Acc/  on Twilio API

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "Open_weather_API-key"
account_sid = "Your-Twilio-Sid"
auth_token = " Your-Twilio-token "


weather_params={
    'lat':'' , #  put your  location Lattitude here
    "lon" : " ", # put your location longitude here
    "appid":api_key,
    "cnt" : 4,
    
}

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="it's going to Rain today Shubham . Remember to bring an ☔️",
        from_="Your-Twilio-number",
        to="Your-Number"
        )
    # message = client.messages.create(
    # from_="whatsapp:TWILIO_WHATSAPP_NUMBER",
    #  body="It's going to rain today. Remember to bring an umbrella",
    # to="whatsapp:YOUR_TWILIO_VERIFIED_NUMBER"
    # )    
    print(message.status)