#!/usr/bin/python3

'''Generate a CSV file of Github data for import into documentation.

Could do something similar for SQL queries, if they are in an organized folder

Same with data auditing and validation stuff

'''

import csv
import pprint
import requests


def convert_to_csv(repo_data):
    return [[repo.get('owner').get('login'),
             repo.get('name'),
             repo.get('html_url'),
             repo.get('description'),
             repo.get('created_at'),
             repo.get('updated_at')
                ] for repo in repo_data 
                  if repo.get('fork') == False
                  and int(repo.get('updated_at').split('-')[0]) > 2016
            ]


def get_github_repo_data(username):
    github_uri = f"https://api.github.com/users/{username}/repos"
    github_data = requests.get(github_uri).json()
    return github_data

def get_github_report(usernames):
    main_csv = []
    for username in usernames:
        github_data = get_github_repo_data(username)
        github_csv =  convert_to_csv(github_data)
        main_csv.extend(github_csv)
    return main_csv


def main():
    # set these in a config
    usernames = ['ucancallmealicia', 'yalemssa', 'YaleArchivesSpace']
    github_repo_csv = get_github_report(usernames)
    output_fp = input('Please enter path to output CSV: ')
    fields = ['owner', 'repository', 'url', 'description', 'created', 'updated']
    with open(output_fp, 'a', encoding='utf8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(fields)
        writer.writerows(github_repo_csv)


if __name__ == '__main__':
    main()

# TODO
# need a way to dedupe forked repos, etc.



