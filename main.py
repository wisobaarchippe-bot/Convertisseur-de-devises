import requests

API_URL = "https://api.exchangerate.host/convert"

def convert_currency(amount, from_currency, to_currency):
    response = requests.get(f"{API_URL}?from={from_currency}&to={to_currency}&amount={amount}")
    data = response.json()
    return data["result"]

print("=== Convertisseur de devises ===")
amount = float(input("Montant : "))
from_currency = input("De (ex: USD, EUR, TND) : ").upper()
to_currency = input("Vers (ex: USD, EUR, TND) : ").upper()

try:
    result = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
except:
    print("Erreur : impossible de convertir pour le moment.")
