import requests
from twilio.rest import Client

parameters = {
    "lat": 10.527642,
    "lon": 76.214432,
    "appid": "a9e05eb3ac7b3c109e78986487e43059",
    "exclude": "current,minutely,daily",
}
hour_id = []
is_going_to_rain = False

account_sid = "AC22a17e0578f55097a125d25252054ab6"
auth_token = "3c0f12ef913ee6254dad75646bc09c8b"

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", parameters)
response.raise_for_status()
hourly_weather_data = response.json()
for hour in hourly_weather_data["hourly"][:12]:
    id = hour["weather"][0]["id"]
    hour_id.append(id)

for id in hour_id:
    if id < 700:
        is_going_to_rain = True

if is_going_to_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today, please take your umbrella ☂️.",
            from_="+13195593015",
            to="+91 9447978843"
        )

    print(message.status)
