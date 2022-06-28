DRAFT! License NOT OFFICIAL!!!



nsmls lists applications which have NSM (Non-Session-Manager) support.  

Usage:  

nsmls  
nsmls -i  

See nsmls -h for other options.  

Applications that have NSM support, should provide a xdg *.desktop file with the NSM keys[1] in it to be detected by nsmls. Nsmls checks for the X-NSM-Exec key. 
You can include your specific user settings in src/config/config.def.py. See CUSTOMIZATION.md for instructions about the config.def.py/ config.py files.  

**Support**


The project is a personal project, which is released because it might be useful for others. License is GPLv2, feel free to maintain your own version. See the NOTICE file in that case.  

No support, feel free to report your issue though. Your issue is probably my issue as well. Users should help users.

No support for .xinitrc / .xsessionrc / wayland related problems.  

No support for git related problems, unless the documentation of nsmls could be improved.  

Please sent a patch if you think a NSM client should be added to the nsm_clients list.  

The nsm_star_clients list is short for a reason. Missing NSM keys in desktop files should be fixed by upstream developers, in meantime users should edit their custom config.def.py file.

To keep things simple, tools that are designed specifically for other GUIs are blocked by default. Users can enable them in their own config if they prefer.  

**Launch from menu**

Note that it's possible to launch NSM applications from your Desktop Manager's launch menu, like dmenu. This way you can use nsmls to list supported applications and then just launch them from your application launcher.


"*If the NSM URL is included in the environment (by either using a fixed port number or starting nsmd early in the initialization process [like in your .xinitrc] extracting the URL from its output) then any NSM capable client will join the current session when started, even if started from outside the Non Session Manager interface (for example, by your Desktop Environment's program launch menu).*"[2]  


For Debian based distributions like Ubuntu, this should be done in ~/.xsessionrc. 

Example settings for .xinitrc / .xsessionsrc:  

export NSM_PORT=18440  
export NSM_URL=osc.udp://HOSTNAME:18440/  
export NSM_DIR=~/NSM\ Sessions  

[3]


License: GPLv2  



[1] Example:  
X-NSM-Exec=drumkv1_jack  
X-NSM-Capable=true  

[2] http://non.tuxfamily.org/session-manager/doc/MANUAL.html#n:1.2.  

[3] See further:  
https://wiki.debian.org/Xsession  
https://wiki.archlinux.org/title/Xinit  
https://wiki.gnome.org/Initiatives/Wayland/SessionStart  
