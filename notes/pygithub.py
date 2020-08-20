from github import Github, GithubException
from datetime import datetime

g = Github('user', 'password')   # your github logging data
commits = 0

with open('urls_repo.txt') as f:   # formatted strings in a file 'user/repo'
    for i in f:
        try:
            i = i.rstrip()
            r = g.get_repo(i)
            commits += r.get_commits(sha='master', since=datetime(year=2016, month=1, day=1, hour=0, minute=0), until=datetime(year=2016, month=12, day=31, hour=23, minute=59)).totalCount
        except GithubException:
            continue

print(commits)


# or

from github import Github #pip install pygithub
import urllib
import datetime as dt

url = "https://gist.githubusercontent.com/agbragin/47e66aaa1232d2cc6478821d18203e90/raw/b428fdb651c93c3eb9a03fa8da9a57a7aa24e835/Awsome%2520Pipeline%2520Repositories"
f = urllib.request.urlopen(url)
addrs = ['/'.join(line.decode("utf-8").replace("\n", "").split('/')[-2:]) for line in f]
g = Github("your_github_login", "your_github_password")
cnts = 0
start = dt.datetime(year=2016, month=1,day=1,hour=0,minute=0)
end = dt.datetime(year=2016, month=12,day=31,hour=23,minute=59)

for i, addr in enumerate(addrs):
    try:
        repo = g.get_repo(addr)
        cnts += repo.get_commits(sha="master", since=start, until=end).totalCount
        print("Progress: {}; counts: {}.".format(float(i+1)/len(addrs), cnts), end="\r")
    except Exception as e:
      continue
        # print("#  {}".format(e))
        # print("#  {} was not processed.".format(addr))

# or

from datetime import datetime
import logging
from logging import config
import sys

from github3 import login

logging.config.fileConfig('logging.cfg')
logger = logging.getLogger('main')


class GitHub:

    def __init__(self, username, password):
        self.github = login(username, password)

    def get_repository_commits(self, owner, repository, since=None, until=None):
        repository = self.github.repository(owner, repository)

        logger.info('Got repository: %s, %s', repository, repository.id)

        commits = []

        for commit in repository.iter_commits(since=since, until=until):
            commits.append(commit)

        logger.info('Number of commits in %s is %s', repository, len(commits))

        return commits

    def get_repository_uri(self, owner, repository):
        repository = self.github.repository(owner, repository)
        return repository.html_url


def dump_commits_to_file(repository, commits, file_path):

    with open(file_path, 'w') as f:
        for commit in commits:
            logger.debug('Commit id: %s, commit date: %s',
                         commit.sha,
                         commit._json_data['commit']['committer']['date'])
            f.write('{}\t{}\t{}\n'.format(
                repository,
                commit.sha,
                commit._json_data['commit']['committer']['date']
            ))


if __name__ == '__main__':
    logger.debug('Get commit statistics for selected GitHub repositories')

    if len(sys.argv) < 3:
        print('Provide username and password as arguments')
        exit(1)

    github = GitHub(sys.argv[1], sys.argv[2])

    # Get commits for 2016 only
    since = datetime(2016, 1, 1, 0, 0)
    until = datetime(2016, 12, 31, 23, 59)

    commits_total = 0

    with open('uris/github_uris_all') as f, open('uris/task', 'w') as f_uri:
        for line in f:
            fields = line.strip().split('\t')
            commits = github.get_repository_commits(fields[0], fields[1], since, until)

            f_uri.write(github.get_repository_uri(fields[0], fields[1]) + '\n')

            commits_total += len(commits)

            dump_commits_to_file(fields[0] + '/' + fields[1], commits,
                                 'data_no_commit_message/{}_{}'.format(fields[0], fields[1]))

    logger.info('Total number of commits: %s', commits_total)

# or

import requests
import json

uu = "https://gist.githubusercontent.com/agbragin/47e66aaa1232d2cc6478821d18203e90/raw/b428fdb651c93c3eb9a03fa8da9a57a7aa24e835/Awsome%2520Pipeline%2520Repositories"
url_list = [ x.replace( "https://github.com/", "") for x in requests.get( uu ).text.split() ]

cnt = 0

params = { "since" : "2016-01-01T00:00:00Z", "until" : "2016-12-31T23:59:59Z", 
           "page" : 1,
           "client_id" : "xxx", 
           "client_secret" : "xxx" }

for i in url_list:
    page = 1
    repo_cnt = 0
    while True:
        params[ "page" ] = page
        r = requests.get( "https://api.github.com/repos/" +i+ "/commits", params=params )
        ln = len(json.loads(r.text))
        if r.status_code != 200 or ln == 0:
            break
        repo_cnt += ln
        page += 1
    #print( i, str(repo_cnt) )
    cnt += repo_cnt
    
    
print( cnt )
