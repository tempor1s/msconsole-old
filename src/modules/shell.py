"""Shell module is a center hub for all modules 
    that allows user to be emersed into a shell by 
    creating a CLI dashboard
"""

__doc__ = """
Usage:
    shell
    shell -h|--help
    shell -v|--version
Options:
    -h --help  Show help screen.
    -v --version  Show version.
"""

__maintainer__ = 'Gary Frederick'  # main contributor
__credits__ = ['Gary Frederick', 'Ben Lafferty']
__license__ = 'MIT'

# built in modules
import os
import sys


# external modules
from clint.textui import puts, colored, indent


example2 = """

                                     
                                                                          
                                ########(((((((((                              
                         ##       ######(((((((       //                       
                       ####         ####(((((         ////                     
                     ######           ##(((           //////                   
                   ########    ((*      (      /##    ////////                 
                  #########    ((((*         /####    /////////                
                   ########    ((((((*     /######    ////////                 
                     ######    ((((((((* /########    //////                   
                       ####    ((((((((((#########    ////                     
                         ##    (((((((##(//#######    //                       
                               (((((####(////#####                             
                               (((######(//////###                             
                               (########(////////#                             
                                 #######(///////                               
                                   #####(/////                                 
                                     ###(///                                   
                                       #(/                          
                                    

"""


class ShellModule(object):
    def __init__(self):
      pass

    def run(self):
        print(colored.blue(example2))


if __name__ == "__main__":
    print(colored.blue(example2))
