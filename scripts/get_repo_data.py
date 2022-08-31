#!/usr/bin/python3

'''Generate a CSV file of Github data for import into documentation.

Could do something similar for SQL queries, if they are in an organized folder

Same with data auditing and validation stuff

'''

import csv
import json
from operator import itemgetter
import requests


def convert_to_csv(repo_data, inclusions, exclusions):
    return [[repo.get('html_url'),
             repo.get('description'),
             repo.get('updated_at').split('T')[0],
             #repo.get('fork')
                ] for repo in repo_data 
                  if (repo.get('fork') == False or 
                      repo.get('name') in inclusions
                     )
                  if repo.get('name') not in exclusions
                  and int(repo.get('updated_at').split('-')[0]) > 2016
            ]


def get_github_repo_data(username):
    github_uri = f"https://api.github.com/users/{username}/repos"
    github_data = requests.get(github_uri).json()
    return github_data

def get_github_report(usernames, inclusions, exclusions):
    main_csv = []
    for username in usernames:
        github_data = get_github_repo_data(username)
        github_csv =  convert_to_csv(github_data, inclusions, exclusions)
        main_csv.extend(github_csv)
    sorted_main_csv = sorted(main_csv, key=itemgetter(2), reverse=True)
    return sorted_main_csv


def main():
    with open('config.json', encoding='utf8') as json_file:
        config = json.load(json_file)
        github_repo_csv = get_github_report(config.get('usernames'), config.get('inclusions'), config.get('exclusions'))
        fields = ['url', 'description', 'updated']
        with open(config.get('output'), 'w', encoding='utf8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            writer.writerows(github_repo_csv)


if __name__ == '__main__':
    main()
