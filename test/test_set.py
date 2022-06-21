#!/usr/bin/env python

import sys

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



x = Client("non-sequencer", "info" )
y = Client("non-sequencer", "xinfo" )



if x == y:
    print("Equal")


my_list = (x, y) 
#my_list.append(x)
#my_list.append(y)


def make_list(my_list):
    for __, entry in enumerate(my_list):
        yield entry.exec_name

# newlist = [x for x in my_list if "a" in x]
# newlist = [x for x in fruits if "a" in x]
# tuple(getattr(obj, field.name) for field in dataclasses.fields(obj))

list0 = list(make_list(my_list))

if sorted(set(list0)) != sorted(list0):
    print("Set error")


#set(my_list)

print(sorted(set(list0)))
print("")
print(sorted(list0))
