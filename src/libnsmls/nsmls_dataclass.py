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
