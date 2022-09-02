#!/usr/bin/python3

'''Generate a CSV file of Github data for import into documentation.

Could do something similar for SQL queries, if they are in an organized folder

Same with data auditing and validation stuff

'''



import csv
import json
from operator import itemgetter
import os
import requests
import yaml

def get_readmes(owners, sesh, inclusions, exclusions):
    output = "/Users/aliciadetelich/Dropbox/git/dmac_data_docs/readmes"
    for owner in owners:
        repo_data = get_github_repo_data(owner, sesh)
        for repo in repo_data:
            if ((repo.get('fork') == False or 
                      repo.get('name') in inclusions
                     )
                  and repo.get('name') not in exclusions
                  and int(repo.get('updated_at').split('-')[0]) > 2016):
                print(repo.get('name'))
                fp = f"https://api.github.com/repos/{owner}/{repo.get('name')}/contents/README.md"
                readme = get_github_file(fp, sesh)
                with open(f"{output}/{owner}_{repo.get('name')}.md", 'w', encoding='utf8') as outfile:
                    outfile.write(readme)

def get_github_file(fp, sesh):
    plugin_data = sesh.get(fp, headers={'Accept': 'application/vnd.github.v4.raw'}).text
    if fp.endswith('yml'):
        return yaml.safe_load(plugin_data)
    return plugin_data

def convert_yml_to_csv(yaml_file):
    return [[f"`{item.get('name')} <{item.get('url').replace('.git', '')}>`_",
                 item.get('branch')
                ] for item in list(yaml_file.values())[0]
            ]

def convert_json_to_csv(repo_data, inclusions, exclusions):
    return [[f"`{repo.get('name')} <{repo.get('html_url')}>`_",
             repo.get('description'),
             repo.get('updated_at').split('T')[0],
             repo.get('fork')
                ] for repo in repo_data 
                  if (repo.get('fork') == False or 
                      repo.get('name') in inclusions
                     )
                  and repo.get('name') not in exclusions
                  and int(repo.get('updated_at').split('-')[0]) > 2016
            ]

def get_github_repo_data(username, sesh):
    github_uri = f"https://api.github.com/users/{username}/repos?per_page=100"
    github_data = sesh.get(github_uri).json()
    return github_data

def get_github_report(usernames, inclusions, exclusions):
    main_csv = []
    for username in usernames:
        github_data = get_github_repo_data(username)
        github_csv =  convert_json_to_csv(github_data, inclusions, exclusions)
        main_csv.extend(github_csv)
    sorted_main_csv = sorted(main_csv, key=itemgetter(2), reverse=True)
    fields = ['repo', 'description', 'updated']
    return sorted_main_csv, fields

def get_plugin_report():
    fp = "https://api.github.com/repos/YaleArchivesSpace/aspace-deployment/contents/prod/plugins.yml"
    plugin_list = get_github_file(fp)
    fields = ['plugin', 'branch']
    return convert_yml_to_csv(plugin_list), fields

def get_writers(outputs):
    for fields, data, output in outputs:
        with open(output, 'w', encoding='utf8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            writer.writerows(data)

def generate_data(config):
    repo_csv, repo_fields = get_github_report(config.get('usernames'), config.get('inclusions'), config.get('exclusions'))
    plugin_csv, plugin_fields = get_plugin_report()
    data_to_write = [(repo_fields, repo_csv, config.get('repo_output')),
                     (plugin_fields, plugin_csv, config.get('plugin_output'))]
    get_writers(data_to_write)

def main():
    with open('config.json', encoding='utf8') as json_file, requests.Session() as sesh:
        config = json.load(json_file)
        headers = {'Authorization': f"token {config.get('gh_key')}"}
        sesh.headers.update(headers)
        get_readmes(config.get('usernames'), sesh, config.get('inclusions'), config.get('exclusions'))


if __name__ == '__main__':
    main()
