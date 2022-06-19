from dataclasses import dataclass

#@dataclass(slots=True)
@dataclass()
class Client:
    exec_name: str = ""
    info: str = ""
    url: str = ""
    installed: bool = False
    path: str = ""
    blocked: bool = False
    config_list: str = "unknown"
    xdg_nsm_confirmed: bool = False 
    xdg_nsm_exec: str = ""
    xdg_nsm_capable: str = ""
    xdg_name: str = ""
    xdg_comment: str = ""
    # xdg_version: str = ""
    xdg_icon: str = ""
 
