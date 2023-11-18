import functions as f
import getpass
import sys

if len(sys.argv) >= 3:
    studenten_nummer = sys.argv[1]
    group_naam = sys.argv[2]
    token = getpass.getpass("Token: ")
    local_path = "C:/Users/elive/OneDrive/Documenten/"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    groups_json = f.GetGroupJSON(headers,group_naam)

    for group in groups_json:
        g_id = group.get("id")
        project_ids = f.ShowProjects(headers,g_id)
        f.CloneRepo(project_ids,headers,local_path)
else:
    print("Gelieve 2 argumenten mee te geven (1|studentenummer en 2|de groupnaam)")