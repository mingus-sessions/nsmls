from dataclasses import dataclass, field

#@dataclass(slots=True, order=True)
@dataclass(slots=True, order=True)
class Client:
    exec_name: str = ""
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
 
