
import logger as log
import view
import model 

def start():
    mode = view.choose_mode()
    if mode == '1':
        contact = view.new_data()
        log.add_data(contact)
    
    elif mode == '2':
        contact = view.search_data()
        #работа с txt
        base = log.get_data_txt()
        view.show_data(model.search_data(contact, base))
        #работа с csv
        base2 = log.get_data_csv()
        view.show_data(model.search_data_CSV(contact, base2))
    

