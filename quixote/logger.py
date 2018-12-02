
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
#              | |       Create on 26/10/2018  All rights reserved by ZIJIAN JIANG    |-|
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
#   One Little Logger
# ************************************ #
#     __                               #
#    / /  ___   __ _  __ _  ___ _ __   #
#   / /  / _ \ / _` |/ _` |/ _ \ '__|  #
#  / /__| (_) | (_| | (_| |  __/ |     #
#  \____/\___/ \__, |\__, |\___|_|     #
#              |___/ |___/             #
# ************************************ #
import logging
import logging.config
import yaml
import os
from typing import Dict


def setup(default_path='logging.yaml', default_level=logging.DEBUG,
          env_key='LOG_CFG'):
    """
    Setup logging configuration
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


# get logger
def getlogger(name):
    return logging.getLogger(name)



# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')

fun_ascii_bloody: Dict[str, str] = {
    "error": r"""
    ▓█████  ██▀███   ██▀███   ▒█████   ██▀███  
    ▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒
    ▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒
    ▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄  
    ░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒
    ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
    ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░
    ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░ 
    ░  ░   ░        ░         ░ ░     ░     
                                            
    """
}
