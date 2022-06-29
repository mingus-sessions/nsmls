DRAFT! License NOT OFFICIAL!!!



nsmls lists applications which have NSM (Non-Session-Manager) support.  

Usage:  

nsmls  
nsmls -i  

See nsmls -h for other options.  

Applications that have NSM support, should provide a xdg *.desktop file with the NSM keys[1] in it to be detected by nsmls. Nsmls checks for the X-NSM-Exec key. 
You can include your specific user settings in src/config/config.py. See CUSTOMIZATION.md for instructions about the src/config/config.def.py and the src/config/config.py file and the 'suckless setup'.  


**Support**


The project is started as a personal project to learn python. It's now at a stage where it might be useful for others too. License is GPLv2, feel free to maintain your own version. See the NOTICE file in that case. Contribute if possible.

In general, don't expect support. Feel free to report your issue though. Your issue is probably my issue as well and bugs are not good. Don't expect new features. Ideally users help users.  

Please sent a patch if you think a NSM client should be added to the nsm_clients list in src/config/config.def.py.  

No support for .xinitrc / .xsessionrc / wayland related problems.  

No support for git related problems, unless the documentation of nsmls could be improved.  

No support for pip related problems, unless the problem is in the setup files.

Missing NSM keys in desktop files should be fixed by upstream developers. They can make your life more easy.  

To keep things simple, tools that are designed specifically for other GUIs are blocked by default. Users can enable them in their own src/config/config.py.


**Requirements**  

It's recommended to install the dependencies via your distribution package manager before running make.   

python >= 3.10  (Ubuntu >= 22.04)  
python-setuptools (setuptools >=42)  
python-pip (pip https://pypi.org/project/pip/)  
python-pyxdg  (pyxdg https://pypi.org/project/pyxdg/)  


**Installation**  

make  
make install 

(no sudo)  


**Launch from menu**

Note that it's possible to launch NSM applications from your Desktop Manager's launch menu, like dmenu. This way you can use nsmls to list supported applications and then just launch them from your application launcher.


"*If the NSM URL is included in the environment (by either using a fixed port number or starting nsmd early in the initialization process [like in your .xinitrc] extracting the URL from its output) then any NSM capable client will join the current session when started, even if started from outside the Non Session Manager interface (for example, by your Desktop Environment's program launch menu).*"[2]  


For Debian based distributions like Ubuntu, this should be done in ~/.xsessionrc. 

Example settings for .xinitrc / .xsessionsrc:  

export NSM_PORT=18440  
export NSM_URL=osc.udp://HOSTNAME:18440/  
export NSM_DIR=~/NSM\ Sessions  


See further:  
https://wiki.debian.org/Xsession  
https://wiki.archlinux.org/title/Xinit  
https://wiki.gnome.org/Initiatives/Wayland/SessionStart  

[1] Example:  
X-NSM-Exec=drumkv1_jack  
X-NSM-Capable=true  

[2] http://non.tuxfamily.org/session-manager/doc/MANUAL.html#n:1.2.  


