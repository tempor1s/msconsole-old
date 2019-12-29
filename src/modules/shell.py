"""Shell module is a center hub for all modules
    that allows user to be emersed into a shell by
    creating a CLI dashboard
"""

__doc__ = """Usage:
    shell
    shell -h|--help
    shell -v|--version
Options:
    modules   Show all avilable modules.
    help      Show help screen.
    version   Show version.
"""

__maintainer__ = 'Gary Frederick'  # main contributor
__license__ = 'MIT'
__version__ = '1.0.0'

# built in modules
import random
import pprint
import sys
import os
import re


# external modules
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
from colorama import Fore
import colorama
import emoji


# local Python Modules
from src.modules.checkin import CheckInModule

# # Module Docs
# from checkin import __doc__ as checkin_doc
# from brute import __doc__ as brute_doc
# from links import __doc__ as link_doc
# from library import __doc__ as library_doc

# initilize colorama
colorama.init()
# console styling
style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


# dashboard = [
#     {
#         'type': 'input',
#         'name': 'server',
#         'message': 'What module do you want to use',
#         'choices': ['checkin', 'links', 'library', 'brute', 'meet'],
#         'filter': lambda val: val.lower()
#     },
#     {
#         'type': 'list',
#         'name': 'repo_type',
#         'message': 'Existing or New Repository',
#         'choices': ['Existing', 'New'],
#         'filter': lambda val: val.lower()
#     },
#     {
#         'type': 'list',
#         'name': 'repo_status',
#         'message': 'Private or public',
#         'choices': ['Private', 'Public'],
#         'filter': lambda val: val.lower(),
#         'when': lambda answers: answers['repo_type'] == 'new'
#     },
#     {
#         'type': 'input',
#         'name': 'repo_name',
#         'message': 'What is the repos name',
#         'filter': lambda val: val.lower(),
#         'when': lambda answers: answers['repo_type'] == 'existing'
#     },
#     {
#         'type': 'input',
#         'name': 'username',
#         'message': 'Whats your github username'
#     },
#     {
#         'type': 'password',
#         'name': 'password',
#         'message': 'Whats your github password'
#     },

#     {
#         'type': 'input',
#         'name': 'quantity',
#         'message': 'How many commits do you want?',
#         'validate': NumberValidator,
#         'filter': lambda val: int(val)
#     },
#     {
#         'type': 'input',
#         'name': 'comments',
#         'message': 'Any comments on your experience?',
#         'default': 'Nope, all good!'
#     },
#     {
#         'name': 'ending',
#         'message': 'Thanks for leaving a comment!',
#         'when': lambda answers: answers['comments'] != 'Nope, all good!'
#     }
# ]
class ModuleValidator(Validator):
    """"""

    def validate(self, document):
        module_list = ['brute', 'checkin', 'libray',
                       'links', 'meet', 'help', 'modules', 'version']
        ok = document.text in module_list
        if not ok:
            print('\n')
            print('Heres a list of available commands')
            for module in module_list:
                print(module)
            home()
            # raise ValidationError(
            #     message='Please enter a command',
            #     cursor_position=len(document.text))


class NumberValidator(Validator):
    """"""

    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end


class EmailValidator(Validator):
    """"""

    def validate(self, document):
        ok = regex.match(
            '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a email',
                cursor_position=len(document.text))


class ShellModule(object):
    def __init__(self):
        self.key = None

    def banner_logo(self):
        make = """




                                                                           
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
        # banner colors
        banner_colors = [Fore.BLUE, Fore.LIGHTBLUE_EX]
        # banner
        banner = random.choice(banner_colors) + make + Fore.RESET
        print(banner)
        print('\n')

    def welcome(self):
        welcome_emoji_list = ['\U0001F918',
                              '\U0001F44B', '\U0001F5A4', '\U0001F47D', '\U0001F642', '\U0001F601', '\U0001F603', '\U0001F435', '\U0001F40D',
                              '\U0001F996']
        print('Hi, welcome to ms shell' +
              emoji.emojize(random.choice(welcome_emoji_list)) + '\n')

    def ask_module(self):
        modules_prompt = {
            'type': 'input',
            'name': 'module',
            'message': 'Enter a command',
            # 'choices': ['checkin', 'links', 'library', 'brute', 'meet'],
            'filter': lambda val: val.lower(),
            'validate': ModuleValidator
        }
        answers = prompt(modules_prompt, style=style)
        module_choice = answers['module']
        return module_choice

    def checkin_route(self):
        checkin_prompt = [
            {
                'type': 'input',
                'name': 'code',
                'message': 'Please enter checkin code',
                'filter': lambda val: val.lower()
            }
        ]
        answers = prompt(checkin_prompt, style=style)
        code = answers['code']
        c = CheckInModule(code)
        c.run()

    def help(self):
        print(__doc__)

    def modules(self):
        module_list = ['brute', 'checkin', 'libray',
                       'links', 'meet', 'help', 'modules']
        for module in module_list:
            print(module)
        self.home()

    def _version(self):
        print(__version__)
        self.home()

    def home(self):
        module = self.ask_module()
        if module == 'modules':
            self.modules()
        if module == 'help':
            print(__doc__)
            self.home()
        if 'checkin' in module:
            if 'help' in module:
                print(checkin_doc)
                self.home()
            self.checkin_route()
        if 'version' in module:
            self._version()

    def run(self):
        self.banner_logo()
        self.welcome()
        self.home()


if __name__ == "__main__":
    c = ShellModule
    c.run()
