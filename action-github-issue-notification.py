#!/usr/bin/python3
# usage: python action-github-issue-notification.py
# export  as env variable
#########################################################################################################
# coding=utf-8

import os
from github import Github


def search_open_issues(auth, github_org: str, github_repo: str, custom_label: str, branch_label: str) -> int:
    repo = auth.get_repo(github_org + "/" + github_repo)
    open_issues = repo.get_issues(state='open', labels=[custom_label, branch_label])
    return open_issues.totalCount


def create_issue(auth, github_org: str, github_repo: str, custom_label: str, branch_label: str) -> None:
    repo = auth.get_repo(github_org + "/" + github_repo)
    repo.create_issue(title=custom_label + " failure", labels=[custom_label, branch_label])


def main():
    # setting env variables
    github_token = os.environ["GITHUB_TOKEN"]
    github_org = os.environ["GITHUB_ORG"]
    github_repo = os.environ["GITHUB_REPO"]
    custom_label = os.environ["GITHUB_CUSTOM_LABEL"]
    branch_label = os.environ["GITHUB_BRANCH_LABEL"]

    auth = Github(github_token)
    # checking if issue already exist
    open_issues_count = search_open_issues(auth, github_org, github_repo, custom_label, branch_label)

    # if issues doesn't exist create one with labels
    if open_issues_count == 0:
        create_issue(auth, github_org, github_repo, custom_label, branch_label)
    else:
        print('not creating issue, already exist........')


main()
