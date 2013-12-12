#import relevant libraries
import git
import os

#Define repo location & url locations
repo = git.Repo('/users/Tucker/Documents/GitHub/Cal-Carbon-Dash-automation')
url = "https://github.com/twillsie/Cal-Carbon-Dash-automation"
repo_loc = '/users/Tucker/Documents/GitHub/Cal-Carbon-Dash-automation'
    #current_repository = git.Repo.clone_from(url,repo_loc)

#Update repo
#repo.git.checkout('origin/master')
repo.git.reset()
repo.git.checkout()

#Modify the file
os.chdir(repo_loc)
f = open('CarbonPrice.txt','a')
f.write('\n')
f.write('lets do this')
f.close()

#Stage files for commit
repo.git.add('CarbonPrice.txt')

#Commit the changes
repo.git.commit(m ='Latest carbon price update')

#Push the repo
#note: to automate login you must follow the instructions here: https://help.github.com/articles/set-up-git
repo.git.push()
