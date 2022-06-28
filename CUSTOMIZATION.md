**The suckless way**

**Config**

A vanilla download of nsmls will contain a folder src/config with a file called config.def.py, a template you can use to create your own config.py file. 
To start customising nsmls, simply copy config.def.py into config.py in the same src/config folder, before you run make. 



The default **Makefile** distributed with nsmls will not overwrite your customised **config.py** with the contents of **config.def.py**, even if it was updated in the latest git pull. Therefore, you should always compare your customised config.py with config.def.py and make sure you include any changes to the latter in your config.py.




Customizations can be managed directly in **git**.

**The concept**

By recording changes and applied patches as commits in a special branch they can be rebased on top of the main branch when required.

**Cloning the repository**

git clone nsmls url

**Recording customizations**

Create a special branch where all the customizations will be kept. It doesn't matter what the name is, it just needs to be something different than main.

git branch my_nsmls

Now switch to the new branch. This will do nothing at the moment as the branches are the same.

git checkout my_nsmls

**Custom version in git**

It's recommended to backup your custom branch of nsmls. This can be done by adding a remote branch.

For example:  
Make a new repository on codeberg or github.

Add the repository as remote (https or ssh):

git add remote codeberg https://codeberg.org/username/nsmls_custom.git

Push your custom nsmls to the new remote repository:

git push codeberg my_nsmls


Now make your changes. 


Then record the changes as commits

- tell git to add the changes in the given file(s) to be recorded  
git add some_file  
git commit -m "my commit"  
- show a diff of what's being commited.  
git commit -v  



**Updating customizations after new release**

When the time comes to update your customizations after a new release of nsmls or when the nsmls repository contains a commit fixing some bug, you first pull the new upstream changes into the main branch  

git checkout main  
git pull  

**Rebase your customization branch on top of the main branch**

git checkout my_nsmls  
git rebase --rebase-merges main  


The --rebase-merges option ensures that you don't have to resolve conflicts which you have already resolved while performing merges again.

In case there are merge conflicts anyway, resolve them (possibly with the help of git mergetool), then record them as resolved and let the rebase continue

git add resolved_file  
git rebase --continue  

If you want to give up, you can always abort the rebase  

git rebase --abort  




***Using pip install -e***


Note that in Python one can test a installation using: 

pip install -e /path/to/local/nsmls/repo

or when you're in the nsmls folder containing the setup.py file:

pip install -e .

(Yes, that's a dot.)

When you now change something in your nsmls configuration, it will automatically applied to your installed version.

If you've the nsmls configuration the way you like, unstall it using: pip uninstall nsmls

Then install it the normal way using the makefile.



Sources:  
http://dwm.suckless.org/customisation/  
http://dwm.suckless.org/customisation/patches_in_git/  

