#!/usr/bin/env python

"""
Copyright 2022, D. Harts, The Netherlands.

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
        elif client.installed:
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
        elif client.installed and not client.blocked:
            print(f"\033[2m{client.exec_name:<18} {client.info} \033[2m{client.url}\033[m")
        elif client.installed and client.blocked:
            #print(\033[9;2mclient.exec_name\033[m\:<18{client.info} \033[2m{client.url}\033[m"  )  # FIXME
            #print(f"\033[9;2m{client.exec_name:<18} {client.info} \033[2m{client.url}\033[m")  # FIXME
            #print(f"\033[9;2m{client.exec_name}\033[m")
            #print("{0:18} Last Name: {1}".format(\033[9;2mclient.exec_name\033[m, 'Clark'))
            number = 18 + (len(client.exec_name) - (18 - len(client.exec_name))) + 1
            exec_name = f"\033[9;2m{client.exec_name}\033[m" 
            info = f"\033[9;2m{client.info} {client.url}\033[m" 
            print("%-*s %s" % ( number, exec_name, info))

    print()
    for client in args.nsm_clients:
        if not client.installed and not client.nsmls and not client.blocked:
            print(f"\033[2;3m{client.exec_name:<18} {client.info} \033[2m{client.url}\033[m")


def print_installed(args):
    for client in args.nsm_clients:
        if client.installed and client.nsmls:
            print(client.exec_name)
        elif client.installed and not client.blocked:
            print(f"\033[2m{client.exec_name}\033[m")
        elif client.installed and client.blocked:
            print(f"\033[9;2m{client.exec_name}\033[m")
            #print(f"\033[2mx {client.exec_name}\033[m")



def print_installed_info(args):
    for client in args.nsm_clients:
        if client.installed and client.nsmls:
            print(f"{client.exec_name:<18} {client.info} {client.url}")
        elif client.installed and not client.blocked:
            print(f"\033[2m{client.exec_name:<18} {client.info} \033[2m{client.url}\033[m")


def print_nsmls(args):
    for client in args.nsm_clients:
        if client.nsmls:
            print(client.exec_name)


def print_output(args):
    #grey = '\033[2m'
    #grey_italic = '\033[2;3m'
    #normal = '\033[m' 
    if args.d:
        pprint(args.nsm_clients)
    elif args.b:
        print_blocked(args)
    elif args.a:
        print_all_info(args)
    elif args.i and args.x:
        print_installed_info(args)
    #elif args.a:
    #    print_all(args)
    elif args.i:
        print_info(args)
    elif args.x:
        print_installed(args)
    else:
        print_nsmls(args)

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
    parser.add_argument("-d", help="dump data",
                    action="store_true")
    parser.add_argument("-i", help="show info",
                    action="store_true")
    parser.add_argument("-x", help="show installed (executable)",
                    action="store_true")
    parser.set_defaults(func=print_output)
    args = parser.parse_args()
    
    args.func(args)

    sys.exit(0)


if __name__ == "__main__":
    main()

