__doc__ = r"""
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


#  ██████╗ ██╗   ██╗██╗██╗  ██╗ ██████╗ ████████╗███████╗    ██████╗ ██████╗ ██████╗ ███████╗
# ██╔═══██╗██║   ██║██║╚██╗██╔╝██╔═══██╗╚══██╔══╝██╔════╝   ██╔════╝██╔═══██╗██╔══██╗██╔════╝
# ██║   ██║██║   ██║██║ ╚███╔╝ ██║   ██║   ██║   █████╗     ██║     ██║   ██║██████╔╝█████╗  
# ██║▄▄ ██║██║   ██║██║ ██╔██╗ ██║   ██║   ██║   ██╔══╝     ██║     ██║   ██║██╔══██╗██╔══╝  
# ╚██████╔╝╚██████╔╝██║██╔╝ ██╗╚██████╔╝   ██║   ███████╗██╗╚██████╗╚██████╔╝██║  ██║███████╗
#  ╚══▀▀═╝  ╚═════╝ ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
"""
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

print(__doc__)

from abc import ABC, abstractmethod

from typing import Dict, List, Tuple, Set, Any, Callable, Optional
from . import logger, timer
from collections import deque
from copy import copy, deepcopy
from contextlib import contextmanager
import uuid
import pip
import xml.etree.ElementTree as ET
import time
import os
import sys


def import_or_install(package: str):
    try:
        pkg = __import__(package)
        return pkg
    except ImportError:
        pip.main(['install', package])     



logger.setup()
qlog = logger.getlogger('core')
qtimer = timer
qdefaultgraph: 'QGraph'


# ******************************************
#  Attrib Dictionary like js object        *
# ******************************************
class QAttrDict(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

    def __getattr__(self, name):
        return self.get(name, None)


class BindError(RuntimeError):
    """QNode basic bind error
    """
    def __init__(self, *args, **kwargs):
        self.args = args

class QNode(ABC):
    """
    QNode is basic component of NodeGraph
    """
    def __init__(self):
        self._qin: QAttrDict = QAttrDict()
        self._qout: QAttrDict = QAttrDict()
        self._const: QAttrDict = QAttrDict()
        self._var: QAttrDict = QAttrDict()
        self._graph: Optional[QGraph] = None
        self._uuid: str = str(uuid.uuid4())
        #
        qdefaultgraph.add(self)
    

    @property
    def qin(self):
        """qin.member property will be accessible when `update()` is called
        after binded to forward node's qout.member. it is recommanded to 
        add qin.member definition in `__init__()` to keep code well documented
        and crystal.
        """
        return self._qin
    
    @property
    def qout(self):
        """qout.member property will be assigned to binded qin.member when 
        `update()` is called after binded to forward node's qout.member. it
        is recommanded to add qout.member definition in `__init__()` to keep
        code well documented and crystal.
        """
        return self._qout
    
    @qout.setter
    def qout(self, val):
        self._qout = val

    @property
    def const(self):
        return self._const

    @property
    def var(self):
        return self._var

    @property
    def uuid(self):
        return self._uuid 

    @abstractmethod
    def update(self) -> bool:
        pass

    def bind(self, attr: str, dst: 'QNode', dstattr: Optional[str] = None) -> 'QNode':
        if not self._graph:
            qlog.error("bind error, no graph assigned {}".format({"node": self}))
            raise BindError("bind error, no graph assigned {}".format({"node": self}))
        if dst._graph is not self._graph:
            qlog.error("bind error, nodes not in same graph {}".format({"node": self, "dstnode": dst}))
            raise BindError("bind error, nodes not in same graph {}".format({"node": self, "dstnode": dst}))
        
        if isinstance(self, QTunnel) and isinstance(dst, QTunnel):
            self._graph.bind(self, "value", dst, "value")
        elif isinstance(self, QTunnel):
            self._graph.bind(self, "value", dst, dstattr or attr)
        elif isinstance(dst, QTunnel):
            self._graph.bind(self, attr, dst, "value")
        else:
            self._graph.bind(self, attr, dst, dstattr or attr)
        return dst

    def rbind(self, attr: str, src: 'QNode', srcattr: Optional[str] = None) -> 'QNode':
        """reverse bind
        """
        if not self._graph:
            qlog.error("bind error, no graph assigned {}".format({"node": self}))
            raise BindError("bind error, no graph assigned {}".format({"node": self}))
        if src._graph is not self._graph:
            qlog.error("bind error, nodes not in same graph {}".format({"node": self, "srcnode": src}))
            raise BindError("bind error, nodes not in same graph {}".format({"node": self, "srcnode": src}))
        
        if isinstance(src, QTunnel) and isinstance(self, QTunnel):
            self._graph.bind(src, "value", self, "value")
        elif isinstance(self, QTunnel):
            self._graph.bind(src, srcattr or attr, self, "value")
        elif isinstance(src, QTunnel):
            self._graph.bind(src, "value", self, attr)
        else:
            self._graph.bind(src, srcattr or attr, self, attr)
        return src

    def eval(self, *, timeit:bool = False):
        if not self._graph:
            qlog.error("eval error, no graph assigned {}".format({"node": self}))
            return
        self._graph.eval(self, timeit=timeit)

   
class QTunnel(QNode):
    """QTunnel is basic component of NodeGraph it takes only input qin 
    and merely transform data into another format and outputs it
    Notice that it should not ever throw any exceptions since it just
    a data transformer, all the data checking and error handling should
    keep within QNode inheritances' update function.
     ┐           ┌---------┐              ┌---------┐ 
     |-----------┘ QTunnel └------------- |         |
    o|------------>   ...   ------------->|o Node 1 |
     |----------------------------------- |         |
     ┘                                    └---------┘
    """
    def __init__(self, transform: Callable[[Any],Any]):
        super().__init__()
        self.qin.value = None
        self.qout.value = None
        self._transform: Callable[[Any],Any] = transform
    
    def update(self) -> bool:
        """
        Notice that it should not ever throw any exceptions since it just
        a data transformer, all the data checking and error handling should
        keep within QNode inheritances' update function.

        Returns:
            True
        """
        self.qout.value = self._transform(self.qin.value)
        return True

class QGraph:
    """
    QGraph contains nodes and execute computation as well as deal with dependencies
    """
    def __init__(self, name: str):
        self.name: str = name
        self.debug: bool = True
        self.debugstepview: bool = False
        self._nodes: Set[QNode] = set()
        self._dirty: Dict[QNode, bool] = {}


        Bind = Tuple[QNode, str, QNode, str]
        # Dict[dstnode, Tuple[srcnode, srcattrib, dstnode, dstattrib]]
        self._bindings: Dict[QNode, List[Bind]] = {}

        self._debuginfo: Dict[str, Any] = {}

    @staticmethod
    def get_default() -> 'QGraph':
        return get_default_graph()

    @contextmanager
    def as_default(self):
        temp = qdefaultgraph
        try:
            qdefaultgraph = self
            yield self
        finally:
            qdefaultgraph = temp


    def add(self, node: QNode):
        if node._graph is not None:
            qlog.error("add error, graph has been assigned {}".format({"node": node, "graph": node._graph}))
            return
        self._nodes.add(node)
        self._dirty[node] = True
        self._bindings[node] = []
        node._graph = self


    def remove(self, node: QNode):
        if node._graph is not self:
            qlog.error("discard error, node not belongs to graph {}".format({"node": node, "graph": node._graph, "self": self}))
            return
        self._nodes.remove(node)
        del self._dirty[node]
        del self._bindings[node]
        node._graph = None

    def bind(self, src: QNode, srcattr: str, dst: QNode, dstattr: str):
        """
        Bind source node's attribute with destination node's attribute
        """
        # check
        if srcattr not in src.qout.__dict__:
            qlog.error("bind error node output data interface has no attribute {}".format({"node": src, "attrib": srcattr}))
            return
        if dstattr not in dst.qin.__dict__:
            qlog.error("bind error node input data interface has no attribute {}".format({"node": dst, "attrib": dstattr}))
            return

        self._bindings[dst].append( (src, srcattr, dst, dstattr) )

    def eval(self, node: QNode, *, timeit: bool = False):
        if node not in self._bindings:
            qlog.error("eval error, node not in graph {}".format({"node": node, "graph": self}))
            return
        
        stack: deque = deque()
        def recursive_append(node: QNode):
            if node not in self._bindings:
                qlog.error("eval error, node not in graph {}".format({"node": node, "graph": self}))
                return

            stack.append(node)
            for bind in self._bindings[node]:
                fnode = bind[0]
                if fnode in self._bindings:
                    recursive_append(fnode)
                else:
                    continue
        recursive_append(node)

        stack_copy = list(copy(stack))
        if self.debug:
            self._debuginfo["eval stack"] = stack_copy

        # set nodes in stack dirty
        for node0 in stack:
            self._dirty[node0] = True

        # update one by one
        while len(stack) > 0:
            node0 = stack.pop()
            if not self._dirty[node0]:
                continue

            # before node0 update we assign value
            for bind in self._bindings[node0]:
                srcnode, srcattrib, _, dstattrib = bind
                setattr(node0.qin, dstattrib, getattr(srcnode.qout, srcattrib), )

            qtimer.mark()
            if node0.update():
                self._dirty[node0] = False
                if self.debug:
                    qlog.debug("node update time elapse {}".format({"node": node0, "time": qtimer.dump()}))
                if self.debugstepview:
                    self.view()
                    input("Press Enter to continue...")
                    sys.stdout.write("\033[F") #move up one line
                    sys.stdout.write("\r")
                    sys.stdout.write("\033[K") #clear current line
                    
            else:
                qlog.error("update error, {}".format({"node": node}))
                break
        
        if self.debug:
            self._debuginfo["eval fails"] = [self._dirty[node0] for node0 in self._debuginfo["eval stack"]]

    def view(self):
        graphviz = import_or_install("graphviz")
        dot: "graphviz.Digraph" = graphviz.Digraph(comment="Graph {}".format(self.name), graph_attr= {'rankdir': 'LR'}, node_attr={'shape': 'plaintext', 'fontname': 'Menlo'})
        for node in self._nodes:
            dot.node(node.uuid, self.style(node))
        
        for node, node_bindings in self._bindings.items():
            line_color = "black" if self._dirty[node] else "limegreen"
            for bind in node_bindings:
                srcnode, srcattr, dstnode, dstattr = bind
                dot.edge("{}:{}".format(srcnode.uuid, "O"+srcattr), 
                    "{}:{}".format(dstnode.uuid, "I"+dstattr), 
                    "", {"color": line_color})

        if sys.platform == "win32":
            import os
            os.environ["PATH"] += os.pathsep + os.path.abspath(r'C:\ProgramData\Miniconda3\Library\bin\graphviz')

        # dot.render(view=True)
        dot.view(cleanup=True)

    def style(self, node: QNode) -> str:
        head_bgcolor = "BLACK" if self._dirty[node] else "GREEN"
        font_color = "WHITE" if head_bgcolor == "BLACK" else "BLACK"
        if isinstance(node, QTunnel):
            table = ET.Element("TABLE", {"BORDER":"1", "CELLBORDER":"1", "CELLSPACING":"0", "CELLPADDING": "0", "PADDING": "0"})
            tr_class = ET.SubElement(table, "TR")
            td_class = ET.SubElement(tr_class, "TD", {"COLSPAN": "2", "BGCOLOR": head_bgcolor})
            font = ET.SubElement(td_class, "FONT", {"COLOR": font_color})
            font.text = str(node.__class__)
            tr_in_out = ET.SubElement(table, "TR", {"align": "left"})

            for key in sorted(node.qin.__dict__.keys()):
                td_in = ET.SubElement(tr_in_out, "TD", {"PORT": "I"+key, "align": "left"})
                td_in.text = "I: " + key

            for key in sorted(node.qout.__dict__.keys()):
                td_out = ET.SubElement(tr_in_out, "TD", {"PORT": "O"+key, "align": "left"})
                td_out.text = "O: " + key

            return "<" + ET.tostring(table, encoding="unicode") + ">"

        else:
            table = ET.Element("TABLE", {"BORDER":"1", "CELLBORDER":"1", "CELLSPACING":"0", "CELLPADDING": "0", "PADDING": "0"})
            tr_class = ET.SubElement(table, "TR")
            td_class = ET.SubElement(tr_class, "TD", {"BGCOLOR": head_bgcolor})
            font = ET.SubElement(td_class, "FONT", {"COLOR": font_color})
            font.text = str(node.__class__)

            for key in sorted(node.qin.__dict__.keys()):
                tr_in = ET.SubElement(table, "TR", {"align": "left"})
                td_in = ET.SubElement(tr_in, "TD", {"PORT": "I"+key, "align": "left"})
                td_in.text = "I: " + key

            for key in sorted(node.qout.__dict__.keys()):
                tr_out = ET.SubElement(table, "TR")
                td_out = ET.SubElement(tr_out, "TD", {"PORT": "O"+key, "align": "left"})
                td_out.text = "O: " + key

            for key in sorted(node.const.__dict__.keys()):
                tr_const = ET.SubElement(table, "TR")
                td_const = ET.SubElement(tr_const, "TD", {"align": "left"})
                td_const.text = "C: " + key

            return "<" + ET.tostring(table, encoding="unicode") + ">"

    @property
    def debuginfo(self):
        return self._debuginfo





qdefaultgraph = QGraph("root")

def get_default_graph() -> QGraph:
    return qdefaultgraph


