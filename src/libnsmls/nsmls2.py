#!/usr/bin/env python

from shutil import which
from pathlib import Path
import os
import sys
import xdg.DesktopEntry #pyxdg  https://www.freedesktop.org/wiki/Software/pyxdg/
#import xdg.IconTheme #pyxdg  https://www.freedesktop.org/wiki/Software/pyxdg/


# NOTE: the default file MUST not have a entry xdg_commented out, other then in user_star_clients.
# NOTE: xdg specifications only have url for LINK entry it seems": https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html#recognized-keys

# TODO: check for multiple items
# TODO: check if installed, for all of them.


import src.config.nsmlsconfig as data 
from src.libnsmls.nsmls_dataclass import Client 


def validate_user_entries():
    for __, client in enumerate(data.user_star_clients):
        if client.exec_name in data.user_blocked_clients:
            print("Error: you can't add and block the same client in user settings. Fix your config.", file=sys.stderr)
            sys.exit(1)



# FIXME: code
def set_missing_url_info():
    for __, entry in enumerate(data.user_star_clients):
        for __, client in enumerate(data.nsm_clients):
            if entry.exec_name == client.exec_name:
                if not entry.url:
                    entry.url = client.url
                if not entry.info:
                    entry.info = client.info
                break
    for __, client in enumerate(data.nsm_star_clients):
        if entry.exec_name == client.exec_name:
            if not entry.url:
                entry.url = client.url
            if not entry.info:
                entry.info = client.info
            break




# We add the applications from the nsm_list, which are installed.
def add_installed_to_list(input_list, programs):
    for __, client in enumerate(input_list):
        if client.installed and client.exec_name not in data.user_blocked_clients:
            programs.append(client)


def set_info(client, xdg_comment):
    if xdg_comment:
        client.info = xdg_comment
    else:
        client.info = "" 


def set_config_list(input_list, config_list):
    for __, client in enumerate(input_list):
        if client.exec_name in data.user_blocked_clients or client in data.blocked_clients:
            client.blocked = True
        client.config_list = config_list
        # client.known = True


def get_path(input_list):
    for __, entry in enumerate(input_list):
        path = which(entry.exec_name)
        if path:
            entry.path = path
            entry.installed = True


# FIXME: code.
def check_for_duplicate(X_NSM_Exec):
    for __, client in enumerate(data.user_star_clients):
        if X_NSM_Exec == client.exec_name:
            return True 
    for __, client in enumerate(data.nsm_star_clients):
        if X_NSM_Exec == client.exec_name:
            return True 


def check_this_list(X_NSM_Exec, input_list):
    for __, client in enumerate(input_list):
        if X_NSM_Exec == client.exec_name:
            #print(f"known {X_NSM_Exec}")
            return client

    
# FIXME: code.
def check_if_known(X_NSM_Exec):
    client = check_this_list(X_NSM_Exec, data.user_star_clients)
    if client:
        return client
    client = check_this_list(X_NSM_Exec, data.nsm_clients)
    if client:
        return client
    client = check_this_list(X_NSM_Exec, data.nsm_star_clients)
    if client:
        return client


def get_entries():
    result = []
    known = False
    for __, path in enumerate(data.xdg_paths):
        for file in path.glob('**/*'):
            if file.is_file() and file.suffix == ".desktop":
                X_NSM_Exec = xdg.DesktopEntry.DesktopEntry(file).get('X_NSM_Exec')
                if X_NSM_Exec:  # or X_NSM_Capable:
                    # X_NSM_Capable = xdg.DesktopEntry.DesktopEntry(file).get('X-NSM-Capable')  
                    # We hope we don't need a extra check. Apps should have X_NSM_Exec in their *.desktop file to be listed by this app. Grabbing for both seems slow.
                    xdg_comment = xdg.DesktopEntry.DesktopEntry(file).getComment()
                    xdg_icon = xdg.DesktopEntry.DesktopEntry(file).getIcon()
                    xdg_name = xdg.DesktopEntry.DesktopEntry(file).getName()
                    client = check_if_known(X_NSM_Exec)
                    if not client:
                        client = Client(exec_name=X_NSM_Exec)
                    client.xdg_nsm_confirmed = True 
                    #client.X_NSM_Capable = X_NSM_Capable
                    client.X_NSM_Exec = X_NSM_Exec 
                    client.xdg_comment = xdg_comment
                    client.xdg_icon = xdg_icon
                    client.xdg_name = xdg_name
                    if client in data.user_blocked_clients or client in data.blocked_clients:
                        client.blocked = True
                    if check_for_duplicate(X_NSM_Exec): 
                        continue
                    else:
                        result.append(client)
    return result
