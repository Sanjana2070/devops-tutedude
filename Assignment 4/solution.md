## 1. Create a new GitHub repository

For Windows the commands for SSH key are: </br>
ssh-keygen -t rsa -b 4096 -C "<emailid@email.com>" </br>
cat ~/.ssh/id_rsa.pub </br>


git checkout -b sanjana2070 </br>
git add . </br>
git commit -m "adding current project" </br>
git push -u origin sanjana2070 </br>
git checkout main </br>
git merge sanjana2070 </br>
git push origin main </br>

