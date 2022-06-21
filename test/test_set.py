#!/usr/bin/env python

import sys
from pprint import pprint

from dataclasses import dataclass, field

#@dataclass(slots=True, order=True)
@dataclass(slots=True, order=True, unsafe_hash=True)
class Client:
    exec_name: str = field(hash=False, default="")
    info: str = field(compare=False, default="")
    url: str = ""
    installed: bool = False
    path: str = ""
    blocked: bool = False
    config_list: str = "unknown"
    xdg_nsm_confirmed: bool = False 
    X_NSM_Exec: str = ""
    #X_NSM_Capable: str = "" 
    xdg_name: str = ""
    xdg_comment: str = ""
    # xdg_version: str = ""
    xdg_icon: str = ""


my_tuple = ("non-sequencer", "non-daw")

def make_Clients(my_tuple):
    for __, client in enumerate(my_tuple):
        yield Client(exec_name=client)
    

my_dc_list = list(make_Clients(my_tuple))

pprint(my_dc_list)




