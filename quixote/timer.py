
#
#                                                    ==(W{==========-      /===-
#                                                      ||  (.--.)         /===-_---~~~~~~~~~------____
#                                                      | \_,|**|,__      |===-~___                _,-'
#                                         -==\\        `\ ' `--'   ),    `//~\\   ~~~~`---.___.-~~
#                                     ______-==|        /`\_. .__/\ \    | |  \\           _-~`
#                               __--~~~  ,-/-==\\      (   | .  |~~~~|   | |   `\        ,'
#                            _-~       /'    |  \\     )__/==0==-\<>/   / /      \      /
#                          .'        /       |   \\      /~\___/~~\/  /' /        \   /'
#                         /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'
#                        /-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
#                                          \_|      /        _) | ;  ),   __--~~
#                                            '~~--_/      _-~/- |/ \   '-~ \
#                                           {\__--_/}    / \\_>-|)<__\      \
#                                           /'   (_/  _-~  | |__>--<__|      |
#                                          |   _/) )-~     | |__>--<__|      |
#                                          / /~ ,_/       / /__>---<__/      |
#                                         o-o _//        /-~_>---<__-~      /
#                                         (^(~          /~_>---<__-      _-~
#                                        ,/|           /__>--<__/     _-~
#                                     ,//('(          |__>--<__|     /                  .----_
#                                    ( ( '))          |__>--<__|    |                 /' _---_~\
#                                 `-)) )) (           |__>--<__|    |               /'  /     ~\`\
#                                ,/,'//( (             \__>--<__\    \            /'  //        ||
#                              ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'
#                            `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/
#                          ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~
#                           ;'( ')/ ,)(                              ~~~~~~~~~~
#                          ' ') '( (/
#                            '   '  `
#                   )          )              
#               ( /(       ( /(     )        
#               )\())   (  )\()) ( /(     )  
#               ((_)\   ))\((_)\  )\()) ( /(  
#               _((_) /((_)_((_)((_)\  )(_)) 
#               | \| |(_)) |_  / | |(_)((_)_  
#               | .` |/ -_) / /  | ' \ / _` | 
#               |_|\_|\___|/___| |_||_|\__,_| 
#
#                                                /    \
#               _                        )      ((    ))     (
#              (@)                      /|\      ))_ ((     /|\
#              |-|                     / | \    (@ || @)   / | \                      (@)
#              | | -------------------/--|-voV---\`||'/--Vov-|--\---------------------|-|
#              |-|                         '^`   (o  o)  '^`                          | |
#              | |                               `\VV/'                               |-|
#              |-|                                                                    | |
#              | |       Create on 26/11/2018  All rights reserved by ZIJIAN JIANG    |-|
#              |-|                                                                    | |
#              | |                                                                    |-|
#              |_|____________________________________________________________________| |
#              (@)              l   /\ /         ( (        \ /\   l                `\|-|
#                               l /   V           \ \        V   \ l                  (@)
#                               l/                _) )_           \I
#                                                 `\ /'
# Copyright (C) 2018  ZIJIAN JIANG

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or 
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# A Very Little Simple Timer
# *********************************
#   _____ _                       *
#  /__   (_)_ __ ___   ___ _ __   *
#    / /\/ | '_ ` _ \ / _ \ '__|  *
#   / /  | | | | | | |  __/ |     *
#   \/   |_|_| |_| |_|\___|_|     *
# *********************************

import time
from typing import Deque, Tuple, Optional, List
from collections import deque


marklist: Deque[Tuple[float, str]] = deque()

def mark(text: Optional[str] = None):
    marklist.append((time.process_time(), text or "Mark {}".format(len(marklist))))

def dump(text: Optional[str] = None) -> List[Tuple[float, str]]:
    global marklist
    marklist.append((time.process_time(), text or "Mark {} - Dump point".format(len(marklist))))
    dumplist = [(time-marklist[0][0], text) for time, text in marklist]
    marklist = deque()
    return dumplist

