#Go to the Desktop (or whatever directory you want to clone into).


#In a web browser, find the directory on your Github.com profile that you want to clone (probably ~/cs114) and locate the green 'clone or download' button on the right near the top. Click it and a box will appear with a link to clone that github repository.

#The link should look something like this:

#https://github.com/YOUR-GITHUB-USERNAME-HERE/cs114.git
#In Terminal, type the following command:

#git clone https://github.com/YOUR-GITHUB-USERNAME-HERE/cs114.git
#Git will copy the cs114 directory into the Desktop.

#Use 'cd' to change directories into the new cs114 folder you just created.

#Now we need to initialize a new git locally on the computer you are using, with this command:

#git init
#Make changes as needed, edit files, add new files and directories.

#Use git to 'add' and then 'commit' your changes.

#git add -A
#git status
#then

#git commit -m"updates"
#git status
#Now, when you have changes you want to appear on your Github.com profile, it is time to 'push' back to your Github profile. Use the following command:

#git push
#Git will ask for your github username and password, enter them and continue your workflow as normal.

#On our student computers these folders will be erased when a new student logs-on.
