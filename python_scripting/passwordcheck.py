# python3 passwordcheck.py Password1 Password2 Password3
import requests

url = "https://api.pwnedpasswords.com/range/" + "CBFDA"
res = requests.get(url)
print(res)