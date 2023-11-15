import requests
import git

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

#clones the repo from the given ids, the root dir is set to document and the cloned dir wil get the name of their id's
def CloneRepo(ids,headers,local_directory):
    og_dir = local_directory
    for id in ids:
        local_directory = og_dir
        url = f"https://gitlab.apstudent.be/api/v4/projects/{id}"
        req = requests.get(url,headers=headers)
        
        repo_info = req.json()
        repo_http = repo_info["http_url_to_repo"]

        local_directory += str(id)
        try:
            git.Repo.clone_from(repo_http, local_directory)
        except git.exc.GitError:
            pass