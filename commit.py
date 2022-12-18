from github import Github
from datetime import datetime,timezone
import pytz
access_token = "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"
g = Github(access_token)
repo = g.get_repo("ishita0207/Automate_CICD_Pipeline")
branch = repo.get_branch("dev")
sha = branch.commit.sha
commit = repo.get_commit(sha=sha)
commit_time = commit.commit.author.date
gmt_timenow = datetime.now(pytz.timezone('GMT'))

diff = gmt_timenow.replace(tzinfo=None) - commit_time
print(diff)
# gmt_timenow = gmt_timenow.split('.')
# gmt_timenow = str(gmt_timenow[0])
# date_commit = commit_time.split(" ")[0]
# gmt_date = gmt_timenow.split(" ")[0]
# print(date_commit)
# print(gmt_date)
# time_commit = commit_time.split(" ")[1]
# time_gmt = gmt_timenow.split(" ")[1]
# print(time_commit)
# print(time_gmt)