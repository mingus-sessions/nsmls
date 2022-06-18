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


import src.config.nsmlsconfig as config 


# check if user_clients are known:
def set_missing_url_info():
    for __, entry in enumerate(config.user_clients):
        for __, client in enumerate(config.nsm_clients):
            if entry.exec_name == client.exec_name:
                if not entry.url:
                    entry.url = client.url
                if not entry.info:
                    entry.info = client.info
                break


# We add the applications from the nsm_list, which are installed.
def add_installed_to_list(input_list, programs):
    for __, client in enumerate(input_list):
        if client.installed and client.exec_name not in config.user_blocked_clients:
            programs.append(client)


def validate_user_entries():
    for __, client in enumerate(config.user_clients):
        if client.exec_name in config.user_blocked_clients:
            print("Error: you can't add and block the same custom client.", file=sys.stderr)
            sys.exit(1)


def set_info(client, comment):
    if comment:
        client.info = comment
    else:
        client.info = "" 



def set_status(input_list, status):
    for __, client in enumerate(input_list):
        if client.exec_name in config.user_blocked_clients or client in config.blocked_clients:
            client.blocked = True
        client.status = status
        client.known = True


def get_path(input_list):
    for __, entry in enumerate(input_list):
        path = which(entry.exec_name)
        if path:
            entry.path = path
            entry.installed = True


def check_for_info(found, comment):
    for __, client in enumerate(config.nsm_clients):
        if found == client.exec_name:
            if not client.info and comment:
                set_info(client, comment)
                return
    for __, client in enumerate(config.nsm_star_clients):
         if found == client.exec_name:
                    if not client.info and comment:
                        set_info(client, comment)
                        return


def check_for_duplicate(found):
    for __, client in enumerate(config.user_clients):
        if found == client.exec_name:
            return True 
    for __, client in enumerate(config.nsm_star_clients):
        if found == client.exec_name:
            return True 


def check_this_list(found, input_list):
    for __, client in enumerate(input_list):
        if found == client.exec_name:
            #print(f"known {found}")
            return client

    

def check_if_known(found):
    client = check_this_list(found, config.user_clients)
    if client:
        return client
    client = check_this_list(found, config.nsm_clients)
    if client:
        return client
    client = check_this_list(found, config.nsm_star_clients)
    if client:
        return client


# xdg stuff was inspire by...
def get_entries():
    result = []
    known = False
    for __, path in enumerate(config.xdg_paths):
        for file in path.glob('**/*'):
            if file.is_file() and file.suffix == ".desktop":
                # There is also ("X-NSM-Capable")
                found = xdg.DesktopEntry.DesktopEntry(file).get('X-NSM-Exec')
                if found and (found not in config.blocked_clients) and (found not in config.user_blocked_clients):
                    comment = xdg.DesktopEntry.DesktopEntry(file).getComment()
                    client = check_if_known(found)
                    if client:
                        client.desktop_file = True
                        check_for_info(found, comment)  # If no info, we set the one from the *.desktop file if exists.
                        if check_for_duplicate(found):  # We don't have to add it, if it's already on the user or star list.
                            continue
                        else:
                            client.status = "xdg"
                            result.append(client)
                    else:
                        # The application isn't status.
                        client = Client(exec_name=found, known=False, status="xdg", desktop_file=True)
                        set_info(client, comment)
                        result.append(client)
    return result



validate_user_entries()

# We set the status.
set_status(config.user_clients, status="user")
set_status(config.nsm_clients, status="nsm_clients")
set_status(config.nsm_star_clients, status="star")

# We set the path (and check if installed or not).
get_path(config.user_clients)
get_path(config.nsm_clients)
get_path(config.nsm_star_clients)



if config.user_clients:
    set_missing_url_info()


# We concatenate both list which only needs a 'installed' check.
# FIXME check for duplicates + warning


# We go through the xdg desktop files to find the 'NSM' entry.
programs = get_entries()




add_installed_to_list(config.user_clients, programs)
add_installed_to_list(config.nsm_star_clients, programs)


#print(f"programs {config.nsm_clients}")

#print(f"programs {programs}")
#print("##########################################")


# We print the output.
for __, program in enumerate(programs):
    print(f"{program.exec_name} - {program.blocked} - {program.status} - {program.info} - {program.url}" )

