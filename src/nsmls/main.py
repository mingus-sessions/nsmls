#!/usr/bin/env python

import argparse
import sys
from pprint import pprint

'''
pseudo:


    what should it provide?

    Default: list installed and confirmed nsm clients, no argument.

    list default + description
    list default + url

    list all: all clients, installed, not installed, confirmed, unconfirmed. (origin?)

    list blocked
    List who doesn't have a desktop file

    dump: dump 'all' information.

'''

import src.config.nsmlsconfig as config 
import src.nsmls.nsmls2 as nsmls


def print_output(args):
    pprint(args.user_clients)
    pprint(args.nsm_clients)
    #pprint(args.user_clients)

    '''
    match args:
        case args.d:
            pprint(args.programs)
        case _:
            for __, program in enumerate(args.programs):
                print(program.exec_name)
    '''
            

def data_mining():
    nsmls.validate_user_entries()
    # We set the origin.
    nsmls.set_origin(config.user_clients, origin="user")
    nsmls.set_origin(config.nsm_clients, origin="nsm_clients")
    nsmls.set_origin(config.nsm_star_clients, origin="star")

    # We set the path (and check if installed or not).
    nsmls.get_path(config.user_clients)
    nsmls.get_path(config.nsm_clients)
    nsmls.get_path(config.nsm_star_clients)

    if config.user_clients:
        nsmls.set_missing_url_info()

    # We go through the xdg desktop files to find the 'NSM' entry.
    programs = nsmls.get_entries()

    # We add the user_clients and the nsm_star_clients.
    nsmls.add_installed_to_list(config.user_clients, programs)
    nsmls.add_installed_to_list(config.nsm_star_clients, programs)

    return programs


def main():

    parser = argparse.ArgumentParser()
    programs = data_mining()
    parser.set_defaults(
            programs=programs, 
            user_clients=config.user_clients,
            nsm_clients=config.nsm_clients,
            nsm_star_clients=config.nsm_star_clients,
            )

    parser.add_argument("-d", help="dump all info",
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


    #print(f"programs {config.nsm_clients}")

    #print(f"programs {programs}")
    #print("##########################################")


    # We print the output.
    #for __, program in enumerate(programs):
    #    print(f"{program.exec_name}" )

    sys.exit(0)




if __name__ == "__main__":
    main()

'''
def main():
    client_list = tuple(nsmd_ctl.read_nsmls_file())
    parser = argparse.ArgumentParser()
    parser.set_defaults(port=NSM_PORT)
    subparsers = parser.add_subparsers(dest='task', help='sub-command help')
    parser_new = subparsers.add_parser('new', help='new session')
    parser_new.add_argument('session', help='Specify a name for the new session.')
    parser_new.set_defaults(func=liblo_server_send)
    parser_duplicate = subparsers.add_parser('duplicate', help='duplicate session')
    parser_duplicate.add_argument('session', help='Specify a name for the new session.')
    parser_duplicate.set_defaults(func=liblo_server_send)
    parser_open = subparsers.add_parser('open', help='Open session') # aliases=['o'], 
    parser_open.add_argument('session', help='Specify the session name to open').completer = list_sessions 
    parser_abort = subparsers.add_parser('abort', help='Abort session')
    parser_abort.add_argument("-y", "--yes", help="Skip confirmation", action="store_true") 
    parser_abort.set_defaults(func=liblo_server_send) 
    parser_close = subparsers.add_parser('close', help='Close session')
    parser_close.set_defaults(func=liblo_server_send)
    parser_open.set_defaults(func=liblo_server_send)
    parser_save = subparsers.add_parser('save', help='Save running session') # aliases=['o'], 
    parser_save.set_defaults(func=liblo_server_send)
    parser_list = subparsers.add_parser('list', help='List sessions') # aliases=['o'], 
    parser_list.set_defaults(func=liblo_server_send)
    parser_ping = subparsers.add_parser('ping', help='Ping nsmd server') # aliases=['o'], 
    parser_ping.set_defaults(func=liblo_server_send)
    parser_add = subparsers.add_parser('add_client', help='Add NSM client') # aliases=['o'], 
    parser_add.add_argument('client', choices=client_list, help='Specify the NSM client to open')
    parser_add.set_defaults(func=liblo_server_send)
    argcomplete.autocomplete(parser)
    args = parser.parse_args()  




    
    if not args.task:
        parser.error('No arguments provided.') # NOTE: this prints two lines.
        sys.exit(1)
    
    nsmd_ctl.right_nsmd_running() # FIXME: should be a ping.
    # FIXME: check if a session is running.

    args.func(args)
    sys.exit(0)




if __name__ == "__main__":
    main()

'''