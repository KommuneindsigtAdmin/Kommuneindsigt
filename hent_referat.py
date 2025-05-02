import requests
import pandas as pd

url = "https://dagsordener.vardekommune.dk/api/agenda/udvalgsliste"
response = requests.get(url)



data = response.json()
print(data)


# Antag at du har hentet dataet med requests
response = requests.get(url)
data = response.json()

# Hvis data er en liste af ordbøger, fx: [{"id": 1, "navn": "Byråd"}, {"id": 2, "navn": "Økonomiudvalg"}]
df = pd.DataFrame(data)

# Vis de første rækker
print(df.head())


{"resultater": [{"id": 1, "navn": "Byråd"}, {"id": 2, "navn": "Økonomiudvalg"}]}

df = pd.DataFrame(data["resultater"])
print(df)