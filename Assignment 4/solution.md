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
</br>

## 2. JSON Update in a Branch
git checkout -b sanjana2070_new </br>
</br>
git add path/to/your/json_file.json </br>
git commit -m "Update JSON content for /api route" </br>
</br>
git checkout main </br>
git merge <your_name>_new </br>
</br>
git add path/to/resolved/file </br>
git commit -m "Resolved merge conflicts from sanjana2070_new" </br>
git push origin main </br>
</br>

##  3.Two Feature Branches from main
git checkout main </br>
git pull origin main </br>
</br>
git checkout -b master_1 </br>
git push -u origin master_1 </br>
</br>
git checkout main </br>
git checkout -b master_2 </br>
git push -u origin master_2 </br>
</br>
### in master_1
git add path/to/your/frontend/file </br>
git commit -m "Add To-Do form with Item Name and Description" </br>
git push </br>

### in master_2
git checkout master_2 </br>
</br>
git add path/to/your/backend/file </br>
git commit -m "Add /submittodoitem backend route for storing To-Do items" </br>
git push </br>

### merge both into main
git checkout main </br>
git merge master_1 </br>
git merge master_2 </br>
</br>
If any merge conflicts: </br>
git add . </br>
git commit -m "Resolve merge conflicts and merge To-Do feature branches" </br>
git push origin main </br>

## Enhance To-Do Form in master_1
git checkout master_1 </br>
</br>
git add path/to/form.html </br>
git commit -m "Add Item ID field to To-Do form" </br>
</br>
git add path/to/form.html </br>
git commit -m "Add Item UUID field to To-Do form" </br>
</br>
git add path/to/form.html </br>
git commit -m "Add Item Hash field to To-Do form" </br>
git push </br>



