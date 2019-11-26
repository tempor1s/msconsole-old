""" Conosle moodule is a center hub for all modules 
    that allows user to be emersed into a shell by 
    creating a CLI dashboard
"""


# built in modules
import os
import sys


# external modules
from clint.textui import puts, colored, indent

__author__ = 'Gary Frederick'  # main contributor
__latest_editor__ = None  # last user to edit document
__date__ = 'November 26, 2019'  # last date edited
__version__ = 0.1  # version number


example_banner = """

                                                     
                                                           
               *#############################.             
             .#################################.           
           .#####################################.         
          ###########   /###########(   ###########        
       .#############     ,########     #############.     
     .################      ,#### #     ###############.   
     ################  #          #     ################   
      ###############    #        #     ###############    
        #############     (#     /#     #############      
          ###########     (### ####     ###########        
            #########     (########     #########          
              #################################            
                #############################              
                  #########################                
                    #####################                  
                      #################                    
                        #############                      
                          #########                        
                            #####                     

"""

if __name__ == "__main__":
    print(colored.blue(example_banner))
