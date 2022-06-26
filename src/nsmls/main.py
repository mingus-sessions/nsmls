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
    elif args.a and args.i:
        print_all_info(args)
    elif args.i and args.p:
        print_installed_info(args)
    elif args.a:
        print_all(args)
    elif args.i:
        print_info(args)
    elif args.b:
        print_blocked(args)
    elif args.p:
        print_installed(args)
    else:
        for client in args.nsm_clients:
            if client.nsmls:
                print(f"{client.exec_name}")


# ENDC = '\033[m'
# https://www.instructables.com/Printing-Colored-Text-in-Python-Without-Any-Module/
# https://ozzmaker.com/add-colour-to-text-in-python/
            
#print(f"{'First Name: ' + 'Jim':<25} Last Name: {'Clark'}")
#print(f"{'Age: ' + '42':<25} Website: {'DelftStack.com'}")
# https://www.delftstack.com/howto/python/python-print-column-alignment/

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
    parser.add_argument("-i", help="show info",
                    action="store_true")
    parser.add_argument("-p", help="show clients which are found in PATH (installed)",
                    action="store_true")
    #parser.add_argument("-u", help="show NSM unconfirmed",
    #                action="store_true")
    parser.set_defaults(func=print_output)
    args = parser.parse_args()
    #if args.echo:
    #    print("xtest")
    # parser.set_defaults(port=NSM_PORT)
    '''
    subparsers = parser.add_subparsers(dest='task', help='sub-command help')
    parser_new = subparsers.add_parser('new', help='new session')
    parser_new.add_argument('session', help='Specify a name for the new session.')
    parser_new.set_defaults(func=liblo_server_send)
    parser_duplicate = subparsers.add_parser('duplicate', help='duplicate session')
    parser_duplicate.add_argument('session', help='Specify a name for the new session.')
    parser_duplicate.set_defaults(func=liblo_server_send)
    '''

    

    args.func(args)


    #print(f"programs {data.nsm_clients}")

    #print(f"programs {programs}")
    #print("##########################################")


    # We print the output.
    #for __, program in enumerate(programs):
    #    print(f"{program.exec_name}" )

    sys.exit(0)




if __name__ == "__main__":
    main()

