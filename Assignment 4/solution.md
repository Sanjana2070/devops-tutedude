## 1. Create a new github repository

for windows the commands for SSH key is:
ssh-keygen -t rsa -b 4096 -C "<emailid@email.com>" 
cat ~/.ssh/id_rsa.pub


git branch sanjana2070
git add .
git commit -m "adding current project"
git push -u origin sanjana2070
git merge sanjana2070
git push origin main

