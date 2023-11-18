import functions as f
import getpass

studenten_nummer = input("Geef je studenten nummer op: ")
group_naam = input("Van welke groep wil je de projecten klonen? ")
token = getpass.getpass("Token: ")
local_path = "C:/Users/elive/OneDrive/Documenten/"

headers = {
    "Authorization": f"Bearer {token}"
}

project_ids = f.ShowProjects(group_naam,headers)

f.CloneRepo(project_ids,headers,local_path)

f.GetSubGroups(headers,group_naam)