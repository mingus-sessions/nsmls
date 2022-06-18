#!/usr/bin/env python

from shutil import which
from pathlib import Path
import os
import xdg.DesktopEntry #pyxdg  https://www.freedesktop.org/wiki/Software/pyxdg/
#import xdg.IconTheme #pyxdg  https://www.freedesktop.org/wiki/Software/pyxdg/


# NOTE: the default file MUST not have a entry commented out, other then in user_clients.
# NOTE: xdg specifications only have url for LINK entry it seems": https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html#recognized-keys

# TODO: check for multiple items
# TODO: check if installed, for all of them.


from src.config.nsmlsconfig import user_clients 
from src.config.nsmlsconfig import nsm_clients_plus
from src.config.nsmlsconfig import nsm_clients
from src.config.nsmlsconfig import blocked_clients
from src.config.nsmlsconfig import xdg_paths 
from src.config.nsmlsconfig import Client



def get_path(input_list):
    for __, entry in enumerate(input_list):
        path = which(entry.exec_name)
        if path:
            entry.path = path
            entry.installed = True


def check_for_duplicate(found, nsm_list):
    for __, client in enumerate(nsm_list):
        if found == client.exec_name:
            return True 
    

# xdg stuff was inspire by...
def get_entries(paths, nsm_clients, nsm_list, blocked_clients):
    result = []
    known = False
    for __, basePath in enumerate(paths):
        for file in basePath.glob('**/*'):
            if file.is_file() and file.suffix == ".desktop":
                # There is also ("X-NSM-Capable")
                found = xdg.DesktopEntry.DesktopEntry(file).get('X-NSM-Exec')
                if found and found not in blocked_clients:
                    if check_for_duplicate(found, nsm_list):
                        continue
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



nsm_list = user_clients + nsm_clients_plus


programs = get_entries(xdg_paths, nsm_clients, nsm_list, blocked_clients)


get_path(nsm_list)
get_path(programs)


for __, client in enumerate(nsm_list):
    if client.installed:
        programs.append(client)


for __, program in enumerate(programs):
    print(f"{program.exec_name} - {program.installed} - {program.desktop_entry} - {program.description} - {program.url}" )
