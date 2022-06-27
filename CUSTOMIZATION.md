A vanilla download of nsmls will contain a file called config.def.py, a template you can use to create your own config.py file. 
To start customising nsmls, simply copy config.def.py into config.py before you run make.


(cp config.def.py config.py)


The default Makefile distributed with nsmls will not overwrite your customised config.py with the contents of config.def.py, even if it was updated in the latest git pull. Therefore, you should always compare your customised config.py with config.def.py and make sure you include any changes to the latter in your config.py.


http://dwm.suckless.org/customisation/


Customizations can be managed directly in git.

The concept

By recording changes and applied patches as commits in a special branch they can be rebased on top of the main branch when required.

git clone .....nsmls url

Recording customizations

Create a special branch where all the customizations will be kept. It doesn't matter what the name is, it just needs to be something different than main.

git branch my_nsmls

Now switch to the new branch. This will do nothing at the moment as the branches are the same.

git checkout my_nsmls

Now make your changes. If you want to apply one of the contributed patches you can use the git apply command

git apply some_patch.diff

Note that many patches make changes config.def.py instead of config.py. Either move those changes also to config.py, or add rm config.py to the clean target in the Makefile.

Then record the changes as commits

# tell git to add the changes in the given file(s) to be recorded
git add some_file
# git will ask you to provide a message describing your changes,
# while showing a diff of what's being commited.
git commit -v


Updating customizations after new release

When the time comes to update your customizations after a new release of nsmls or when the nsmls repository contains a commit fixing some bug, you first pull the new upstream changes into the main branch

git checkout main
git pull

Then rebase your customization branch on top of the main branch

git checkout my_nsmls
git rebase --preserve-merges main

The --preserve-merges option ensures that you don't have to resolve conflicts which you have already resolved while performing merges again.

In case there are merge conflicts anyway, resolve them (possibly with the help of git mergetool), then record them as resolved and let the rebase continue

git add resolved_file
git rebase --continue

If you want to give up, you can always abort the rebase

git rebase --abort

http://dwm.suckless.org/customisation/patches_in_git/

