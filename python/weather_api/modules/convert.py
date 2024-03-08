def convert_data(data):
    if data["cod"] == 200:
        obj = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "state": data["weather"][0]["main"],
        }
    else:
        obj = {"message": data["message"]}
    return obj
