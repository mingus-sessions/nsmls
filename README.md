DRAFT! License NOT OFFICIAL!!!

NSMLS:

nsmls lists applications with Non-Session-Manager (NSM) support.

It's possible to launch NSM applications from your Desktop Manager's launch menu, like dmenu:


"If the NSM URL is included in the environment (by either using a fixed port number or starting nsmd early in the initialization process [like in your .xinitrc] extracting the URL from its output) then any NSM capable client will join the current session when started, even if started from outside the Non Session Manager interface (for example, by your Desktop Environment's program launch menu)."

http://non.tuxfamily.org/session-manager/doc/MANUAL.html#n:1.2.

For Debian based distributions like Debian, Ubuntu and Linux Mint, this should be done in ~/.xsessionrc.

Example settings for .xinitrc / .xsessionsrc:

export NSM_PORT=18440
export NSM_URL=osc.udp://HOSTNAME:18440/
export NSM_DIR=~/NSM\ Sessions


See further:
https://wiki.debian.org/Xsession
https://wiki.archlinux.org/title/Xinit

License: GPL version 2.0 (see also NOTICE).
