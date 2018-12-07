```
#
#  ██████╗ ██╗   ██╗██╗██╗  ██╗ ██████╗ ████████╗███████╗    ██████╗ ██████╗ ██████╗ ███████╗
# ██╔═══██╗██║   ██║██║╚██╗██╔╝██╔═══██╗╚══██╔══╝██╔════╝   ██╔════╝██╔═══██╗██╔══██╗██╔════╝
# ██║   ██║██║   ██║██║ ╚███╔╝ ██║   ██║   ██║   █████╗     ██║     ██║   ██║██████╔╝█████╗
# ██║▄▄ ██║██║   ██║██║ ██╔██╗ ██║   ██║   ██║   ██╔══╝     ██║     ██║   ██║██╔══██╗██╔══╝
# ╚██████╔╝╚██████╔╝██║██╔╝ ██╗╚██████╔╝   ██║   ███████╗██╗╚██████╗╚██████╔╝██║  ██║███████╗
#  ╚══▀▀═╝  ╚═════╝ ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
```

Quixote is a minimal dataflow based computational graph skeleton library

It provides you a clean and right-thinking data processing paradigm.

In data processing, we concern about three things:
1. Where is the data came from
2. What is the purpose of the data
3. Where is the destination of data

So quixote's graph consists of two things, Node and Bind, Node is in which the data is transformed, Bind binds two nodes' data interface into pipeline.
And quixote's dataflow graph is like below.
![graph](image/graph.png)(image is powered by graphviz, rectangle represents Node, and data Bind is presented by arrowed spline, green ones are updated with newest data feed, this image is from one real airplane system project I'm leading)

___In the quixote dataflow graph, left node(or forward nodes) is data feed of right linked ones. Once left node is updated successfully, it will output and push its newest result into linked node's input. When one node's forward, or "data dependent nodes", all updated successfully (newest data feed is ready), this node will try to update itself's output with respect to the newest data inputs. The `update` function is user defined, quixote graph will call it on evaluation time in data dependency order. When node's `update` function is called, quixote will make sure that all it's data inputs are updated and ready to be read. All the node should do is take different sources of data and calculate or transform input data and put them into its outputs. (Tunnel is a simple node takes one input and transform into one output, it helps graph more self explainable when node's input takes single specific data over a large amount of complex data with a lot of redundant information, I mean if our data interface is opaque, how can we expect node's behavior from that?)___

> Be noticed that you should not change forward node's input data, it is possible to but quite an undefined behavior.

# WHY? 

You must have question like "WHY WE BOTHER DO THIS"?

Let me list some of advantages comes with quixote's data processing paradigm.

* Data Lineage is sound and clear
* Focus on data interface makes user rethink about design of architecture 
* Debug is more painless than if I have a junk of codes and I have no idea what's are going on
* Nodes provide nature variable scope isolation which makes functions purer and unsurprised
* Errors can be caught easily, and not interfere other nodes' functions when they have no dependency
* Refactoring should be quick and easy
* MOST IMPORT ONE - New project team member could immediately participate in development
* ...

It would be unfair if I don't list some shortages.

* At present quixote.core is written in python
* It _force_ you to write code in specific way rather than a powerful and unconstrained style you are thinking of.


# Installation

You could get quixote by pip.
``` 
pip install pyquixote
```

You can validate the installation by `import quixote.core` and you should see 😊
```
import quixote.core
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
....
```

Graphviz library is optional, if you want to visualize the data graph please install `graphviz`

It is recommanded to use `anaconda` for `graphviz` installation and development.

```
conda install graphviz
```
This will install `graphviz` c library into anaconda environment
```
pip install graphviz
```
And this will install `graphviz` python binding package

> You may found some additional operation like enviroment variable settings on Windows operation system. If you have any further question about how to install `graphviz` please refer to:

* [https://pypi.org/project/graphviz/](https://pypi.org/project/graphviz/)
* [https://graphviz.readthedocs.io/en/stable/manual.html](https://graphviz.readthedocs.io/en/stable/manual.html)
* [https://stackoverflow.com/questions/18438997/why-is-pydot-unable-to-find-graphvizs-executables-in-windows-8](https://stackoverflow.com/questions/18438997/why-is-pydot-unable-to-find-graphvizs-executables-in-windows-8)

# Usage
```Python

from quixote.core import QNode, QGraph, QTunnel, qlog
from typing import List, Dict, Tuple

class Contact(QNode):
    def __init__(self):
        super().__init__() # don't forget init super class QNode

        # EVERY THING SHOULD BE DEFINED HERE WITH TYPE HINTS, before evaluation starts

        # `const`, `var`, `qin`, `qout` are builtin js-object like object in `QNode`
        # every thing defined in `const` should not be modified after first assignment
        self.const.mycontacts: List[Dict[str, str]] = [
            {
                "name": "Johanna",
                "phone": "132-987-098"
            }, 
            {
                "name": "Steve",
                "phone": "167-321-777"
            }
        ]
        # Things defined in `var` are mutable, they are states maintained in `QNode` itself
        # and not accessible to other `QNode`s
        self.var.count: int = 0

        # attribute defined in `qout` is `QNode`'s data "interface", it will be pushed to 
        # linked `QNode`'s `qin.some_attrib` when it `update` successfully
        self.qout.contacts: List[Tuple[str, str]] = [] # type hint tells the difference!

    def update(self) -> bool: # `update` is abstract method should be implemented
        try:
            self.var.count = len(self.const.mycontacts)
            self.qout.contacts = [ (contact["name"], contact["phone"]) for contact in  self.const.mycontacts ]
        except Exception:
            print("some error")
            return False   # quixote will pause the following evaluation when it meets `update` error
        
        return True # `update` successfully

class PrintNames(QNode):
    def __init__(self):
        super().__init__()
        self.qin.contacts: List[Tuple[str, str]] = []
        self.qin.names: List[str] = []
    
    def update(self) -> bool:
        print(self.qin.names)
        return True
    
if "__main__" == __name__:

    contactbook = Contact()
    prints = PrintNames()

    datatunnel = QTunnel( lambda contacts: [ x[0] for x in contacts ] )
    
    contactbook.bind("contacts", datatunnel).bind("names", prints) # forward bind data interface
    prints.rbind("contacts", contactbook) # also can reverse bind data interface
    # prints.rbind("contacts", contactbook, "contacts") do the same thing... the line above is a suger

    QGraph.get_default().view() # Graphviz Libaray must be installed if you want to see graph
    QGraph.get_default().debugstepview = True # show every step debug graph
    prints.eval() # evaluate the terminal node and see how much time elapsed
```

The example's result will be like below.
```
['Johanna', 'Steve'] 
Press Enter to continue...
```

Best wishes:
I hope you enjoy using this library 😊

Author: ZIJIAN JIANG








