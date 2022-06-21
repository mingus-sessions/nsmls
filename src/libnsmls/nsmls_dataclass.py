from dataclasses import dataclass, field

#@dataclass(slots=True, order=True)
@dataclass(slots=True, order=True)
class Client:
    exec_name: str = ""
    info: str = field(compare=False, default="")
    url: str = field(compare=False, default="")
    installed: bool = field(compare=False, default=False)
    path: str = field(compare=False, default="")
    xdg_name: str = field(compare=False, default="")
    xdg_comment: str = field(compare=False, default="")
    # xdg_version: str = field(compare=False, default="")
    xdg_icon: str = field(compare=False, default="")
    xdg_nsm_confirmed: bool = field(compare=False, default=False)
    X_NSM_Exec: str = field(compare=False, default="")
    #X_NSM_Capable: str = field(compare=False, default="")
    # config_list: str = field(compare=False, default="unknown")
    nsm_star: bool = False
    blocked: bool = field(compare=False, default=False)
    nsm: bool = field(compare=False, default=False)
