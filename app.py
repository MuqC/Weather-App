import requests

api_key = "b384d38bae75d31a80069bb82caea003"
while True:
    user_input = input("Enter a city: ")

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    if weather_data.json()["cod"] == "404":
        print("No city found")
    else: 
        weather = weather_data.json()["weather"][0]["main"]
        temp = round(weather_data.json()["main"]["temp"])
        feel = round(weather_data.json()["main"]["feels_like"])
        press = weather_data.json()["main"]["pressure"]

        print(f"The weather in {user_input} is currently: {weather}")
        print(f"The current temperature is: {temp} degrees Fahreinheit")
        print(f"The temperature feels like: {feel} degrees Fahreinheit")
    print("")