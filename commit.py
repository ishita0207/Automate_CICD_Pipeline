from github import Github
from datetime import datetime,timezone, timedelta
import pytz
import os
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
if diff<timedelta(minutes=10):
    os.system("bash script.sh")    
else:
    print("Not required")