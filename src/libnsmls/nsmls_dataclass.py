from dataclasses import dataclass, field

@dataclass(slots=True, order=True)
class Client:
    exec_name: str = ""
    info: str = field(compare=False, default="")
    url: str = field(compare=False, default="")
    installed: bool = field(compare=False, default=False)
    path: str = field(compare=False, default="")
    xdg_name: str = field(compare=False, default="")
    xdg_comment: str = field(compare=False, default="")
    X_NSM_Exec: str = field(compare=False, default="")
    nsm_star: bool = field(compare=False, default=False)
    blocked: bool = field(compare=False, default=False)
    nsmls: bool = field(compare=False, default=False)
