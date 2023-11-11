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

get_existing_group_url = f"https://gitlab.apstudent.be/api/v4/groups?search={data['name']}"
get_existing_group_request = requests.get(get_existing_group_url, headers=headers)

existing_group = get_existing_group_request.json()

#check if the group already exist or not and stores the id of set group
if existing_group:
    group_id = existing_group[0].get("id")
else:
    postrequest = requests.post(api_groups_url,headers=headers, data=data)
    print(postrequest.text)
    group_id = postrequest.json().get("id")

#creates a subgroup test in the main group created above
data= {
    "name": "test",
    "path": "test-subgroup",
    "parent_id": group_id
}

postrequest = requests.post(api_groups_url,headers=headers,data=data)
print(postrequest.text)