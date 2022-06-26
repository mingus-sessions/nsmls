#!/usr/bin/env python

"""
Copyright 1822, D. Harts, The Netherlands.

This file is part of nsmls.

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


import argparse
from pprint import pprint
import sys


import src.libnsmls.nsmls2 as nsmls 
import src.config.nsmlsconfig as data 
from src.libnsmls.nsmls_dataclass import Client 


def print_all(args):
    for client in args.nsm_clients:
        if client.nsmls:
            print(client.exec_name)
    print()
    for client in args.nsm_clients:
        if client.installed and not client.nsmls:
            print(f"\033[2m{client.exec_name}\033[m")
    print()
    for client in args.nsm_clients:
        if not client.installed and not client.nsmls:
            print(f"\033[2;3m{client.exec_name}\033[m")


def print_blocked(args):
    for client in args.nsm_clients:
        if client.blocked:
            print(client.exec_name)


def print_info(args):
    for client in args.nsm_clients:
        if client.nsmls:
            if client.info:
                # print(f"{client.exec_name:<18} {client.info} \033[2m{client.url}\033[m")
                print(f"{client.exec_name:<18} {client.info} {client.url}")
            else:
                print(f"{client.exec_name:<18} {client.xdg_comment} {client.url}")


def print_all_info(args):
    for client in args.nsm_clients:
        if client.nsmls:
            print(f"{client.exec_name:<18} {client.info} {client.url}")
            #print({client.exec_name)
    print()
    for client in args.nsm_clients:
        if client.installed and not client.nsmls:
            print(f"\033[2m{client.exec_name:<18} {client.info} \033[2m{client.url}\033[m")
    print()
    for client in args.nsm_clients:
        if not client.installed and not client.nsmls:
            print(f"\033[2;3m{client.exec_name:<18} {client.info} \033[2m{client.url}\033[m")


def print_installed(args):
    for client in args.nsm_clients:
        if client.nsmls:
            print(f"{client.exec_name}")
            #print({client.exec_name)
    for client in args.nsm_clients:
        if client.installed and not client.nsmls:
            print(f"\033[2m{client.exec_name}\033[m")


def print_installed_info(args):
    for client in args.nsm_clients:
        if client.nsmls:
            print(f"{client.exec_name:<18} {client.info} {client.url}")
            #print({client.exec_name)
    for client in args.nsm_clients:
        if client.installed and not client.nsmls:
            print(f"\033[2m{client.exec_name:<18} {client.info} \033[2m{client.url}\033[m")


def print_output(args):
    #grey = '\033[2m'
    #grey_italic = '\033[2;3m'
    #normal = '\033[m' 
    if args.d:
        pprint(args.nsm_clients)
    elif args.a and args.u:
        print_all_info(args)
    elif args.u and args.i:
        print_installed_info(args)
    elif args.a:
        print_all(args)
    elif args.u:
        print_info(args)
    elif args.b:
        print_blocked(args)
    elif args.i:
        print_installed(args)
    else:
        for client in args.nsm_clients:
            if client.nsmls:
                print(f"{client.exec_name}")


def main():

    parser = argparse.ArgumentParser()
    nsmls.nsmls_data_mining()
    parser.set_defaults(
            nsm_clients=data.nsm_clients,
            )
    parser.add_argument("-a", help="show all",
                    action="store_true")
    parser.add_argument("-b", help="show blocked",
                    action="store_true")
    parser.add_argument("-d", help="dump all info",
                    action="store_true")
    parser.add_argument("-u", help="show url and description",
                    action="store_true")
    parser.add_argument("-i", help="show installed",
                    action="store_true")
    parser.set_defaults(func=print_output)
    args = parser.parse_args()
    
    args.func(args)

    sys.exit(0)


if __name__ == "__main__":
    main()

