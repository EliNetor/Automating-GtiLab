import requests
import getpass

#Tests connection and gives information about the user of the token
token = getpass.getpass("Token: ")
api_url = "https://gitlab.apstudent.be/api/v4/user"

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(api_url, headers=headers)

print(response.json())
