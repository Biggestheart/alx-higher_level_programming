#!/usr/bin/python3
"""
Module to access  the GitHub API and uses the_data
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def main(argv):
    """
    Function_that_list 10_commits (from_the_most recent_to_oldest)
    of the repository.The_first_argument will_be the_repository_name
    and_the_second_argument will_be_the_owner_name
    """

    def print_commits(i, commit_list):
        """
        List_the_commits, less_than_10_commits
        """
        sha = commit_list[i].get('sha')
        commit = commit_list[i].get('commit')
        author = commit.get('author')
        name = author.get('name')
        print('{}: {}'.format(sha, name))

    repo = argv[1]
    owner = argv[2]
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get('https://api.github.com/repos/' + owner +
                            '/' + repo + '/commits', headers=headers)
    commit_list = response.json()
    size = len(commit_list)
    if size < 10:
        for i in range(0, size):
            print_commits(i, commit_list)
    else:
        for i in range(0, 10):
            print_commits(i, commit_list)


if __name__ == "__main__":
    main(argv)
