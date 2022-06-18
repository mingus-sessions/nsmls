#!/usr/bin/env python

from shutil import which
from pathlib import Path
import os
import sys
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
from src.config.nsmlsconfig import user_blocked_clients
from src.config.nsmlsconfig import xdg_paths 
from src.config.nsmlsconfig import Client


def validate_user_entries(user_clients, user_blocked_clients):
    for __, client in enumerate(user_clients):
        if client.exec_name in user_blocked_clients:
            print("Error: you can't add and block the same custom client.", file=sys.stderr)
            sys.exit(1)


def set_description(client, comment):
    if comment:
        client.description = comment
    else:
        client.description = "" 



def set_status(input_list, status):
    for __, client in enumerate(input_list):
        client.status = status
        client.known = True


def get_path(input_list):
    for __, entry in enumerate(input_list):
        path = which(entry.exec_name)
        if path:
            entry.path = path
            entry.installed = True


def check_for_description(found, comment, input_list):
    for __, client in enumerate(input_list):
        if found == client.exec_name:
            if not client.description and comment:
                set_description(client, comment)
                return
 

def check_for_duplicate(found, input_list):
    for __, client in enumerate(input_list):
        if found == client.exec_name:
            return True 
    

def check_if_known(found, input_list):
    for __, client in enumerate(input_list):
        if found == client.exec_name:
            print(f"url{client.url}")
            return client


# xdg stuff was inspire by...
def get_entries(paths, nsm_clients, user_list, blocked_clients):
    result = []
    known = False
    for __, path in enumerate(paths):
        for file in path.glob('**/*'):
            if file.is_file() and file.suffix == ".desktop":
                # There is also ("X-NSM-Capable")
                found = xdg.DesktopEntry.DesktopEntry(file).get('X-NSM-Exec')
                if found and (found not in blocked_clients) and (found not in user_blocked_clients):
                    comment = xdg.DesktopEntry.DesktopEntry(file).getComment()
                    client = check_if_known(found, user_list)
                    if not client:
                        client = check_if_known(found, nsm_clients)
                    if client:
                        client.status = "found"
                        client.known = True
                        check_for_description(found, comment, nsm_clients)  # If no description, we set the one from the *.desktop file if exists.
                        if check_for_duplicate(found, nsm_clients):  # We don't have to add it, if it's already on the user or star list.
                            continue
                        else:
                            result.append(client)
                    else:
                        # The application isn't listed.
                        client = Client(exec_name=found, known=False, status="found")
                        set_description(client, comment)
                        result.append(client)
    return result



validate_user_entries(user_clients, user_blocked_clients)

# We set the status.
set_status(user_clients, status="user")
set_status(nsm_clients_star, status="star")
# user_blocked
# blocked


# check if user_clients are known:
def check_if_recognize(user_list, nsm_clients):
    for __, entry in enumerate(user_list):
        for __, client in enumerate(user_list):
            if entry.exec_name == client.exec_name:
                if not entry.url:
                    print("TURE")
                    entry.url = client.url
                if not entry.description:
                    entry.description = client.description


if user_clients:
    check_if_recognize(user_clients, nsm_clients)


# We concatenate both list which only needs a 'installed' check.
# FIXME check for duplicates + warning


# We go through the xdg desktop files to find the 'NSM' entry.
programs = get_entries(xdg_paths, nsm_clients, user_clients, blocked_clients)


nsm_list = user_clients + nsm_clients_star
# We set the path (and check if installed or not).
get_path(nsm_list)
get_path(programs)

# We add the applications from the nsm_list, which are installed.
for __, client in enumerate(nsm_list):
    if client.installed:
        programs.append(client)

# We print the output.
for __, program in enumerate(programs):
    print(f"{program.exec_name} - {program.known} - {program.status} - {program.description} - {program.url}" )
