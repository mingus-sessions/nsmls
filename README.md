DRAFT! License NOT OFFICIAL!!!

NSMLS:

nsmls lists applications with Non-Session-Manager (NSM) support.


If you want to launch applications into Non-Session-Manager GUI via a terminal console or a Desktop Manager menu, like dmenu, some NSM related environment variables needs to be set early in the environment. 

"If the NSM URL is included in the environment (by either using a fixed port number or starting nsmd early in the initialization process [like in your .xinitrc] extracting the URL from its output) then any NSM capable client will join the current session when started, even if started from outside the Non Session Manager interface (for example, by your Desktop Environment's program launch menu)."

http://non.tuxfamily.org/session-manager/doc/MANUAL.html#n:1.2.

For Debian based distributions like Debian, Ubuntu and Linux Mint, this should be done in ~/.xsessionrc. See the data folder for examples.

License: GPL version 2.0 (see also NOTICE).
