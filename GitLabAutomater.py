import requests
import getpass

#Tests connection and gives information about the user of the token
token = getpass.getpass("Token: ")
api_users_url = "https://gitlab.apstudent.be/api/v4/user"

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(api_users_url, headers=headers)

print(response.json())

#Creates a group PythonAdvancedELIVERMEULEN
api_groups_url = "https://gitlab.apstudent.be/api/v4/groups"
data = {
    "name": "PythonAdvancedELIVERMEULEN",
    "path": "PythonAdvancedELIVERMEULEN-group"
}
postrequest = requests.post(api_groups_url,headers=headers, data=data)

print(postrequest.text)