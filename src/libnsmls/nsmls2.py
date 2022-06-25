#!/usr/bin/env python

"""
Copyright 2022, D. H., The Netherlands.

This file is part of 

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Library General Public
License version 2 as published by the Free Software Foundation.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Library General Public License for more details.

You should have received a copy of the GNU Library General Public
License along with this library; if not, write to the
Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
Boston, MA  02110-1301, USA.
"""



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



from shutil import which

import sys
import xdg.DesktopEntry #pyxdg  https://www.freedesktop.org/wiki/Software/pyxdg/



import src.config.nsmlsconfig as data 
import src.libnsmls.nsmls2 as nsmls


# indent=1, width=80, depth=None, stream=None, *, compact=False, sort_dicts=True, underscore_numbers=False)

# NOTE: duplication... compare dataclasses?

def star_not_in_blocked(list1, list2):
    for __, client in enumerate(list1):  # data.user_star_clients):
        if client in list2:  # data.user_blocked_clients:
            print("Error: you can't add and block the same client in either the user or general settings. Fix your config.", file=sys.stderr)
            sys.exit(1)


def filter_blocked(blocked_clients): 
    for __, client in enumerate(blocked_clients):
        if client not in data.user_star_clients:
            yield client


# Set the star clients:
def set_star_status(input_list):
    for __, client in enumerate(data.nsm_clients):
        if client.exec_name in input_list:
            client.nsm_star = True


def set_blocked_status(input_list):
    for __, client in enumerate(data.nsm_clients):
        if client.exec_name in input_list:
            client.blocked = True


def set_nsmls_status():
    for __, client in enumerate(data.nsm_clients):
        if (client.nsm_star or client.X_NSM_Exec) and client.installed and not client.blocked:
            client.nsmls = True


def check_if_on_nsm_clients_list(X_NSM_Exec):
    for __, client in enumerate(data.nsm_clients):
        if X_NSM_Exec == client.exec_name:
            return client 


def search_for_nsm_clients():
    for __, xdg_desktop_path in enumerate(data.xdg_paths):
        for file in xdg_desktop_path.rglob('*'):
            if file.is_file() and file.suffix == ".desktop":
                desktop_file = xdg.DesktopEntry.DesktopEntry(file)
                X_NSM_Exec = desktop_file.get('X-NSM-Exec')
                # X_NSM_Capable = xdg.DesktopEntry.DesktopEntry(file).get('X-NSM-Capable')  
                # We hope we don't need a extra check. Apps should have X_NSM_Exec in their *.desktop file to be listed by this app (KISS). Grabbing for both on all apps seems slow too.
                if X_NSM_Exec:  # or X_NSM_Capable:
                    xdg_comment = desktop_file.getComment()
                    xdg_name = desktop_file.getName()
                    client = check_if_on_nsm_clients_list(X_NSM_Exec)
                    if not client:
                        client = data.Client(exec_name=X_NSM_Exec)
                        data.nsm_clients.append(client)
                    #client.X_NSM_Capable = X_NSM_Capable
                    client.X_NSM_Exec = X_NSM_Exec 
                    client.xdg_comment = xdg_comment
                    client.xdg_name = xdg_name


def make_star_clients(star_clients):
    for __, client in enumerate(star_clients):
        yield data.Client(exec_name=client, nsm_star=True)


def remove_duplicates(star_clients):
    for __, client in enumerate(data.nsm_clients):
        for item, star in enumerate(star_clients):
            if client.exec_name == star:  # The client becomes the star client. Incl url and info.
                client.nsm_star = True
                star_clients.pop(item)


def get_paths():
    for __, client in enumerate(data.nsm_clients):
        path = which(client.exec_name)
        if path:
            client.path = path
            client.installed = True


def nsmls_data_mining():
    # Validate.

    # user star can't be in user  blocked
    # user star can't have duplicates 
    # 

    # VALIDATE

    star_not_in_blocked(data.user_star_clients, data.user_blocked_clients)
    star_not_in_blocked(data.nsm_star_clients, data.blocked_clients)

    # Handle the blocked related data.

    # Unblock clients that are in user_star_list.

    blocked_clients = list(filter_blocked(data.blocked_clients))

    # Concatenate user_blocked_clients and blocked_clients.

    blocked_clients = set(blocked_clients + data.user_blocked_clients)


    # Handle the stars.

    # Remove duplicates from star_clients and concatenate star_clients and user_star_clients.

    star_clients = data.user_star_clients + data.nsm_star_clients

    # Check if star_client is on nsm_clients list, set the client to star and rm from star list.

    remove_duplicates(star_clients)

    # Convert star tuples to Client dataclass objects.

    star_objects = list(make_star_clients(set(star_clients)))

    # Search for NSM clients in the desktop files.

    search_for_nsm_clients()

    # Add the star clients to nsm_clients list.
    data.nsm_clients = sorted(data.nsm_clients + star_objects)


    # We've gathered all our data. Let's set the star and blocked status for the Client objects in nsm_clients list.

    set_star_status(star_clients)
    set_blocked_status(blocked_clients)

    # Now check which clients are actually installed. 
    get_paths()

    # Now we know the star, blocked and installed status. We also gathered the desktop files with a NSM entry. Let's set the nsmls (display) status.
    set_nsmls_status()


