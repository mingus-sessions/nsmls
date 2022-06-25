#!/usr/bin/env python

"""
Copyright 2022, D. H., The Netherlands.

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



    



def print_output(args):
    #for __, client in enumerate(args.nsm_star_clients):
    #    print(f'Client("{client.exec_name}", "{client.url}", "{client.info}"),')
    if args.d:
        pprint(args.nsm_clients)
    if args.b:
        for __, client in enumerate(args.blocked_clients):
            print(client)
    else:
        for __, client in enumerate(args.nsm_clients):
            if client.installed and client.nsmls and not client.blocked:
                print(f"\033[2m{client.exec_name}\033[m")


# ENDC = '\033[m'
# https://www.instructables.com/Printing-Colored-Text-in-Python-Without-Any-Module/
# https://ozzmaker.com/add-colour-to-text-in-python/
            


def main():

    parser = argparse.ArgumentParser()
    nsmls.nsmls_data_mining()
    parser.set_defaults(
            # programs=programs, 
            nsm_clients=data.nsm_clients,
            # user_star_clients=data.user_star_clients,
            #nsm_clients=data.nsm_clients,
            #nsm_star_clients=nsm_star_list,
            #user_blocked = sorted(set(data.user_blocked_clients)),
            #blocked = sorted(set(data.blocked_clients)),
            #blocked=sorted(blocked_clients),
            #stars=sorted(star_clients),

            )

    parser.add_argument("-d", help="dump all info",
                    action="store_true")
    parser.add_argument("-b", help="show blocked",
                    action="store_true")
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

