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

    user_blocked_clients_set = set(data.user_blocked_clients)
    blocked_clients_set = set(data.blocked_clients)


    def filter_blocked(blocked_clients): 
        for __, client in enumerate(blocked_clients):
            if client not in data.user_star_clients:
                yield client


    blocked_clients = list(filter_blocked(blocked_clients_set))
    


    blocked_clients += user_blocked_clients_set
    star_clients = set(data.user_star_clients + data.nsm_star_clients)


    # we know nsm_clients
    # we know found clients
    # we know star clients


    # Set the star clients:
    def set_star_status(input_list):
        for __, client in enumerate(data.nsm_clients):
            if client in input_list:
                client.nsm_star = True


    def set_blocked_status(input_list):
        for __, client in enumerate(data.nsm_clients):
            if client in input_list:
                client.blocked = True


    def check_if_on_nsm_clients_list(X_NSM_Exec):
        for __, client in enumerate(data.nsm_clients):
            if X_NSM_Exec == client.exec_name:
                return client 
        return None


    def get_entries(blocked_list):
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
                        client = check_if_on_nsm_clients_list(X_NSM_Exec)
                        if not client:
                            client = data.Client(exec_name=X_NSM_Exec)
                            data.nsm_clients.append(client)
                        client.xdg_nsm_confirmed = True
                        #client.X_NSM_Capable = X_NSM_Capable
                        client.X_NSM_Exec = X_NSM_Exec 
                        client.xdg_comment = xdg_comment
                        client.xdg_icon = xdg_icon
                        client.xdg_name = xdg_name
                        if client.exec_name in blocked_list:
                            client.blocked = True
                        else:
                            client.nsm = True

   

    set_star_status(star_list)
    set_blocked_status(blocked_list)
    
    nsmls.get_entries()

    def make_star_clients(star_clients):
        for __, client in enumerate(star_clients):
            yield data.Client(exec_name=client, client.nsm_star=True, client.nsm=True)  # what if on blocking?


    star_objects = list(make_star_clients(star_clients))


    def remove_duplicates(star_objects):
        for x, star in enumerate(star_objects):
            for __, client in enumerate(data.nsm_clients):
                if star.exec_name == client.exec_name:
                    client.nsm_star = True
                    client.nsm = True
                    star_objects.pop(x)


    # Now concatenate them to one list
    data.nsm_clients += star_objects




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
            if client.installed and client.nsm and not client.blocked:
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
