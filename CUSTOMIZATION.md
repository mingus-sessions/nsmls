**The suckless way**

Tools following the suckless philosophy are customized through editing its source code, this should make the tools fast and secure - it does not process any input data which isn't known at 'compile time'.  

**Config**

A vanilla download will contains a file src/config/config.def.py, a template you can use to create your own src/config/config.py file. 
To start customising, simply copy src/config/config.def.py into src/config/config.py before you run make. 



The default distributed **Makefile**, will not overwrite your customised src/config/config.py with the contents of src/config/config.def.py, even if it was updated in the latest git pull. Therefore, you should always compare your customised config.py with src/config/config.def.py and make sure you include any changes to the latter in your src/config/config.py!




Customizations can be managed directly in **git**.

**The concept**

By recording changes and applied patches as commits in a special branch they can be rebased on top of the main branch when required.


**Recording customizations**

Clone the repository


Create a special branch where all the customizations will be kept. It doesn't matter what the name is, it just needs to be something different than main.

git branch my_custom_branch

Now switch to the new branch. This will do nothing at the moment as the branches are the same.

git checkout my_custom_branch

**Custom version in git**

You could push your custom branch to your own (online) repository. This can be done by adding a remote branch.

For example:  
Make a new repository on codeberg or github.

Add the repository as remote (https or ssh):

git add remote codeberg https://codeberg.org/username/appname_custom.git

Push your custom branch to the new remote repository:

git push codeberg my_custom_branch  

(Codeberg is a arbitrary chosen name).


Now make your changes. 


Then record the changes as commits (note the dot):

git add .  
git commit -m "my commit"  
(git push codeberg my_custom_branch)



**Updating customizations after new release**

When the time comes to update your customizations after a new release, you first pull the new upstream changes into the main branch  

git checkout main  
git pull  

**Rebase your customization branch on top of the main branch**

git checkout my_custom_branch  
git rebase --rebase-merges main  


The --rebase-merges option ensures that you don't have to resolve conflicts which you have already resolved while performing merges again.

In case there are merge conflicts anyway, resolve them (possibly with the help of git mergetool), then record them as resolved and let the rebase continue

git add resolved_file  
git rebase --continue  

If you want to give up, you can always abort the rebase  

git rebase --abort  



NOTE: in Python one can install a package using: pip install -e /path/to/application  
When you now change something in your configuration, it will automatically applied to your installed version.  
When you're happy about your configuration, uninstall it via pip and install the package using make.


Sources:  
http://suckless.org/philosophy/  
http://dwm.suckless.org/customisation/  
http://dwm.suckless.org/customisation/patches_in_git/  

