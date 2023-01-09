#Сборка общего решения

import logger as log
import view
import model 

def start():
    candys = 117 
    max_take = 28
    view.welcome_message(candys, max_take)
    mode = view.choose_mode()
    if mode == '1':
        view.people() 
    
    elif mode == '2':
        view.bot()