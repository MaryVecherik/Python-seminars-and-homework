
import logger as log
import view
import model  

def run():
    mode = view.choose_mode()
    if mode == '1':
        contact = view.new_data()
        log.add_data(contact)
    
    elif mode == '2':
        contact = view.search_data()
        base = log.get_data()
        result = model.search_data(contact, base)
        view.show_data(result)
