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
from src.config.nsmlsconfig import nsm_clients_star
from src.config.nsmlsconfig import nsm_clients
from src.config.nsmlsconfig import blocked_clients
from src.config.nsmlsconfig import xdg_paths 
from src.config.nsmlsconfig import Client


def set_description(client, file):
    print(f"!{client.exec_name}")
    description = xdg.DesktopEntry.DesktopEntry(file).getComment()
    if not description:
        description = ""
    client.description = description 


def set_status(input_list, status):
    for __, client in enumerate(input_list):
        client.status = status


def get_path(input_list):
    for __, entry in enumerate(input_list):
        path = which(entry.exec_name)
        if path:
            entry.path = path
            entry.installed = True


def check_for_duplicate(found, input_list):
    for __, client in enumerate(input_list):
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
                    for __, known_client in enumerate(nsm_clients):
                        if found == known_client.exec_name:
                            known = True
                            known_client.desktop_file = True 
                            if not known_client.description:
                                set_description(known_client, file)
                        if check_for_duplicate(found, nsm_list):
                            continue
                        # known_client.installed = True
                        result.append(known_client)
                        break
                    if not known:
                        unknown_client = Client(exec_name=found, installed=True, known_client=False, status="found")
                        set_description(unknown_client, file)
                        result.append(unknown_client)
                        known = False
    return result


# We set the status.
set_status(user_clients, status="user")
set_status(nsm_clients_star, status="plus")
# user_blocked
# blocked

# We concatenate both list which only needs a 'installed' check.
nsm_list = user_clients + nsm_clients_star


# We go through the xdg desktop files to find the 'NSM' entry.
programs = get_entries(xdg_paths, nsm_clients, nsm_list, blocked_clients)

# We set the path (and check if installed or not).
get_path(nsm_list)
get_path(programs)
set_status(programs, status="found")

# We add the applications from the nsm_list, which are installed.
for __, client in enumerate(nsm_list):
    if client.installed:
        programs.append(client)

# We print the output.
for __, program in enumerate(programs):
    print(f"{program.exec_name} - {program.known_client} - {program.status} - {program.description} - {program.url}" )
