import requests


def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+%t+%h"
    response = requests.get(url)

    if response.status_code == 200:
        climate = response.text
        print(f"Weather in {city}:")
        print(climate)
    else:

        print("Error. Please check the city name...!!")


def main():
    city = input("Enter city name: ")
    get_weather(city)


if __name__ == "__main__":
    main()
