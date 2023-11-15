import requests

#returns a list of poject id's for given group name
def ShowProjects(group_name,headers):
    get_existing_group_url = f"https://gitlab.apstudent.be/api/v4/groups?search={group_name}" 
    get_existing_group_request = requests.get(get_existing_group_url, headers=headers)
    existing_group = get_existing_group_request.json()

    project_ids = []

    if existing_group:
        g_id = existing_group[0].get("id")

        group_projects_url = f"https://gitlab.apstudent.be/api/v4/groups/{g_id}/projects"
        group_projects_request = requests.get(group_projects_url,headers=headers)
        existing_projects = group_projects_request.json()
        for projects in existing_projects:
            project_ids.append(projects.get("id"))

    return project_ids