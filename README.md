DRAFT! License NOT OFFICIAL!!!



nsmls lists applications which have NSM (Non-Session-Manager) support.  

Usage:  

nsmls  
nsmls -i  

See nsmls -h for other options.  

Developers that have NSM support in their application, should provide a xdg *.desktop file with the NSM keys in it to be detected by nsmls. 

Nsmls checks the X-NSM-Exec key, if it's missing, the application won't be detected by nsmls. You can include your specific user settings in src/config/config.def.py.  

See CUSTOMIZATION.md for customizing nsmls.  

Note that it's possible to launch NSM applications from your Desktop Manager's launch menu, like dmenu. This way you can use nsmls to list supported applications and then just launch them from your application launcher.


"*If the NSM URL is included in the environment (by either using a fixed port number or starting nsmd early in the initialization process [like in your .xinitrc] extracting the URL from its output) then any NSM capable client will join the current session when started, even if started from outside the Non Session Manager interface (for example, by your Desktop Environment's program launch menu).*[1]"  


For Debian based distributions like Ubuntu, this should be done in ~/.xsessionrc. 

Example settings for .xinitrc / .xsessionsrc:  

export NSM_PORT=18440  
export NSM_URL=osc.udp://HOSTNAME:18440/  
export NSM_DIR=~/NSM\ Sessions  

For Wayland alternatives see:  
https://wiki.gnome.org/Initiatives/Wayland/SessionStart  


See further:  
https://wiki.debian.org/Xsession  
https://wiki.archlinux.org/title/Xinit  

License: GPLv2  

[1]  
Example:  
X-NSM-Exec=drumkv1_jack 
X-NSM-Capable=true  

[2] http://non.tuxfamily.org/session-manager/doc/MANUAL.html#n:1.2.  
