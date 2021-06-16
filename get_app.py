import threading
from utils.lcd_print import lcd_print_main
from utils.buzzer import familymart_ringo
from utils.camera_main import take_photo
from utils.relay_func import relay_run

def get_main_func():
    take_photo()
    threading.Thread(target=lcd_print_main).start()
    threading.Thread(target=familymart_ringo).start()
    threading.Thread(target=relay_run).start()

if __name__ == "__main__":
    get_main_func()