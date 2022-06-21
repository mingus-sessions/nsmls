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

import src.config.nsmlsconfig as data 
import src.libnsmls.nsmls2 as nsmls


# indent=1, width=80, depth=None, stream=None, *, compact=False, sort_dicts=True, underscore_numbers=False)

# NOTE: duplication... compare dataclasses?


def nsmls_data_mining():
    # Validate.

    # user star can't be in user  blocked
    # user star can't have duplicates 
    # 
    nsmls.star_not_in_blocked()

    def make_clients():
        for __, client in enumerate(set(data.nsm_star_clients)):
            #print(client)
            yield data.Client(exec_name=client)
        

    nsm_star_list = list(make_clients())

    #print(nsm_star_list)



    nsmls.validate_config_lists(data.nsm_clients, list_name="nsm_clients")
    nsmls.validate_config_lists(data.user_star_clients, list_name="user_star_clients")
    nsmls.validate_config_lists(nsm_star_list, list_name="nsm_star_clients")


    # filter star list, check if in nsm_clients, add info_url,
    # then check if in user list, rm from list

    # then we're only have to deal with user_list and nsm_clients.


    # Check if user star client is on nsm_clients, add info_url.
    
    # Search via xdg, add found clients to list, if not already in user_star_list, 
    # otherwise just add data.

    # If found and unknown, add to the list

    # Convert tuples to dataclasses:




    # We set the origin.
    nsmls.set_config_status(data.nsm_clients, config_list="nsm_clients")
    nsmls.set_config_status(data.user_star_clients, config_list="nsm_user_star")  # Needs the last

    nsmls.set_config_status(nsm_star_list, config_list="nsm_star")

    #nsmls.validate_config_lists(data.nsm_star_clients, list_name="nsm_star_clients")
    #nsmls.search_duplicates_in_star_lists()


    # We set the path (and check if installed or not).
    nsmls.get_path(data.user_star_clients)
    nsmls.get_path(data.nsm_clients)
    nsmls.get_path(nsm_star_list)

    # If we have a url, we add the url.
    if data.user_star_clients:
        nsmls.set_missing_url_info(data.user_star_clients)
    if nsm_star_list:
        nsmls.set_missing_url_info(nsm_star_list)

    # Ok, all data is set. Time to remove duplicates:

    # if a nsm_client is on user_list, we don't have to add.
    # if a nsm_client is on star_list, we don't have to add.
    # 




    nsmls.check_if_client_on_user_list(nsm_star_list)  # We remove the nsm_star_client if it's already on the user_star list.
    nsmls.check_if_client_on_user_list(data.user_star_clients)  # We remove the nsm_star_client if it's already on the user_star list.

    programs = nsm_star_list + data.user_star_clients + data.nsm_clients # + nsm_star_list
    #programs = data.user_star_clients  # We add a other label to the list. 
    #programs += nsm_star_list  # We add the nsm_star_clients to the user_star_clients.


    #pprint(sorted(programs))



    #print("+++++++++++++++++")



    # Now let's search for the NSM entry in the desktop files.

    nsmls.get_entries(programs)

    #pprint(sorted(programs))


    # Now add the ones which are not on the list yet.


    return programs


def print_output(args):
    #for __, client in enumerate(args.nsm_star_clients):
    #    print(f'Client("{client.exec_name}", "{client.url}", "{client.info}"),')
    if args.d:
        pprint(sorted(args.programs))
    if args.b:
        for __, client in enumerate(sorted(set(data.blocked_clients + data.user_blocked_clients))):
            print(client)
    else:
        for __, client in enumerate(sorted(args.programs)):
            if client.installed and client.nsm:
                print(client.exec_name)


            


def main():

    parser = argparse.ArgumentParser()
    programs = nsmls_data_mining()
    parser.set_defaults(
            programs=programs, 
            # user_star_clients=data.user_star_clients,
            #nsm_clients=data.nsm_clients,
            #nsm_star_clients=nsm_star_list,
            #user_blocked = sorted(set(data.user_blocked_clients)),
            #blocked = sorted(set(data.blocked_clients)),

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
