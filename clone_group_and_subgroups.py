import functions as f
import getpass

studenten_nummer = input("Geef je studenten nummer op: ")
group_naam = input("Van welke groep wil je de projecten klonen? ")
token = getpass.getpass("Token: ")

headers = {
    "Authorization": f"Bearer {token}"
}

project_ids = f.ShowProjects(group_naam,headers)
print(project_ids)