#!/usr/bin/env python

from shutil import which
from pathlib import Path
import os
import xdg.DesktopEntry #pyxdg  https://www.freedesktop.org/wiki/Software/pyxdg/
#import xdg.IconTheme #pyxdg  https://www.freedesktop.org/wiki/Software/pyxdg/


# NOTE: the default file MUST not have a entry commented out, other then in custom_clients.
# NOTE: xdg specifications only have url for LINK entry it seems": https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html#recognized-keys
# xdg.IconTheme.getIconPath(desktopEntry.getIcon    ()

# TODO: check for multiple items
# TODO: check if installed, for all of them.



from src.config.nsmlsconfig import custom_clients 
from src.config.nsmlsconfig import green_clients
from src.config.nsmlsconfig import nsm_clients
from src.config.nsmlsconfig import blocked_clients
from src.config.nsmlsconfig import xdg_paths 


joinedlist = custom_clients + green_clients


data_list = joinedlist  # FIXME


def get_path(input_list):
    for __, entry in enumerate(input_list):
        path = which(entry.exec_name)
        if path:
            entry.path = path
            entry.installed = True


# xdg stuff was inspire by...
def get_entries(paths, nsm_clients, blocked_clients):
    result = []
    known = False
    for __, basePath in enumerate(paths):
        for file in basePath.glob('**/*'):
            if file.is_file() and file.suffix == ".desktop":
                found = xdg.DesktopEntry.DesktopEntry(file).get('X-NSM-Exec')
                if found and found not in blocked_clients:
                    for __, known_client in enumerate(nsm_clients):
                        if found == known_client.exec_name:
                            known = True
                            known_client.installed = True
                            known_client.desktop_entry = True
                            result.append(known_client)
                            break
                    if not known:
                        description = xdg.DesktopEntry.DesktopEntry(file).getComment()
                        if not description:
                            description = ""
                        unknown_client = Client(exec_name=found, installed=True, known_client=False, description=description, desktop_entry=True)
                        result.append(unknown_client)
    return result


programs = get_entries(xdg_paths, nsm_clients, blocked_clients)


get_path(data_list)
get_path(programs)


for __, client in enumerate(data_list):
    if client.installed:
        programs.append(client)


for __, program in enumerate(programs):
    print(f"{program.exec_name} - {program.description} - {program.url}" )
