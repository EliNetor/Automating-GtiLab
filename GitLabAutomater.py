import requests
import getpass
import pandas

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
    "name": "blub", #need to be changed to PythonAdvancedELIVERMEULEN
    "path": "blub-group" #need to be changed to PythonAdvancedELIVERMEULEN-group
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

print(group_id)
#creates a subgroup test in the main group created above
data= {
    "name": "test",
    "path": "test-subgroup",
    "parent_id": group_id
}

postrequest = requests.post(api_groups_url,headers=headers,data=data)
print(postrequest.text)

#shows the information about the to be created classes
klasgroep = []
vak = []

df = pandas.read_csv("testfile.csv", header=None)
for row in df.iloc[:, 0]:
    if row not in vak:
        vak.append(row)
for row in df.iloc[:, 1]:
    if row not in klasgroep:
        klasgroep.append(row)
vak.sort()
klasgroep.sort()

student = {}
for index, row in df.iterrows():
    student.update({index: [row[2], row[0], row[1]]})
    print(f"Nu moet een groep gemaakt worden voor {student[index][0]}. Dit is een subgroep van klasgroep {student[index][2]} ({klasgroep.index(student[index][2])}) voor het vak {student[index][1]} met id ({vak.index(student[index][1])}).")

#creates the groupes from which te information is shown above
#create vak subroup
print(group_id)
vakken = {}
for course in vak:
    data={
        "name": course,
        "path": course,
        "parent_id": group_id,
    }

    postrequest = requests.post(api_groups_url,headers=headers, data=data)
    print(postrequest.text)
    vakken.update({course: postrequest.json().get("id")})

#create klas subgroup
klassen = {}
for index, student_info in student.items():
    vak_id = vakken.get(student_info[1])
    data={
        "name": student_info[2],
        "path": student_info[2],
        "parent_id": vak_id 
    }

    postrequest = requests.post(api_groups_url,headers=headers, data=data)
    print(postrequest.text)
    klassen.update({student_info[2]: postrequest.json().get("id")})