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


def star_not_in_blocked():
    for __, client in enumerate(data.user_star_clients):
        if client.exec_name in data.user_blocked_clients:
            print("Error: you can't add and block the same client in user settings. Fix your config.", file=sys.stderr)
            sys.exit(1)

'''
def search_duplicates_in_star_lists():
    for __, user_star_client in enumerate(data.user_star_clients):
        for __, star_client in enumerate(data.nsm_star_clients):
            if user_star_client == star_client:
                print("Error: User star client, already in the 'nsm_star_clients' list. Please fix.", file=sys.stderr)
                sys.exit(1)

'''

# FIXME: there's probably a better method, when working with dataclasses.
def dataclass_field_to_tuple(input_list):
    for __, client in enumerate(input_list):
        yield client.exec_name


# FIXME: it doesn't tells us which list and which entry.
def validate_config_lists(input_list, *, list_name=""):
    exec_name_tuple = tuple(dataclass_field_to_tuple(input_list))
    if sorted(set(exec_name_tuple)) != sorted(exec_name_tuple):
        print(f"Error: duplicated entry found in list {list_name}. Please fix your config.", file=sys.stderr)
        sys.exit(1)


# FIXME: code
def set_missing_url_info(star_list):
    for __, star_client in enumerate(star_list):
        for __, nsm_client in enumerate(data.nsm_clients):
            if star_client.exec_name == nsm_client.exec_name:
                if not star_client.url:
                    star_client.url = nsm_client.url
                if not star_client.info:
                    star_client.info = nsm_client.info
                break


def set_missing_url_info_star(star_list):
    for __, nsm_client in enumerate(data.nsm_clients):
        for __, star_client in enumerate(star_list):
            if nsm_client.exec_name == star_client:
                client = nsm_client
            
        


# NOTE: should be done after converting tuple to dataclas nsm star clients!
def check_if_client_on_user_list(nsm_star_list):
    for star_item, nsm_star in enumerate(nsm_star_list):
        for __, user_star in enumerate(data.user_star_clients):
            if nsm_star.exec_name == user_star.exec_name:
                nsm_star_list.pop(star_item)




def set_config_list(input_list, config_list):
    for __, client in enumerate(input_list):
        if client.exec_name in data.user_blocked_clients or client.exec_name in data.blocked_clients:
            client.blocked = True
        client.config_list = config_list
        # client.known = True


def get_path(input_list):
    for __, entry in enumerate(input_list):
        path = which(entry.exec_name)
        if path:
            entry.path = path
            entry.installed = True


def is_already_added_check(X_NSM_Exec, program_list):
    for __, client in enumerate(program_list):
        if X_NSM_Exec == client.exec_name:
            return client
    return None



def check_if_on_nsm_clients_list(X_NSM_Exec):
    for __, client in enumerate(data.nsm_clients):
        if X_NSM_Exec == client.exec_name:
            return client



def get_entries(programs):
    for __, xdg_desktop_path in enumerate(data.xdg_paths):
        for file in xdg_desktop_path.glob('**/*'):
            if file.is_file() and file.suffix == ".desktop":
                desktop_file = xdg.DesktopEntry.DesktopEntry(file)
                X_NSM_Exec = desktop_file.get('X-NSM-Exec')
                # X_NSM_Capable = xdg.DesktopEntry.DesktopEntry(file).get('X-NSM-Capable')  
                # We hope we don't need a extra check. Apps should have X_NSM_Exec in their *.desktop file to be listed by this app (KISS). Grabbing for both on all apps seems slow too.
                if X_NSM_Exec:  # or X_NSM_Capable:
                    xdg_comment = desktop_file.getComment()
                    xdg_icon = desktop_file.getIcon()
                    xdg_name = desktop_file.getName()
                    client = is_already_added_check(X_NSM_Exec, programs)
                    if not client:
                        client = Client(exec_name=X_NSM_Exec)
                        programs.append(client)
                    client.xdg_nsm_confirmed = True 
                    #client.X_NSM_Capable = X_NSM_Capable
                    client.X_NSM_Exec = X_NSM_Exec 
                    client.xdg_comment = xdg_comment
                    client.xdg_icon = xdg_icon
                    client.xdg_name = xdg_name
                    if client in data.user_blocked_clients or client in data.blocked_clients:
                        client.blocked = True
 
