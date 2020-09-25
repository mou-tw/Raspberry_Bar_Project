import threading
from lcd_print import lcd_print_main
from buzzer import familymart_ringo
from camera_main import take_photo
from relay_func import relay_run

def get_main_func():
    take_photo()
    threading.Thread(target=lcd_print_main).start()
    threading.Thread(target=familymart_ringo).start()
    threading.Thread(target=relay_run).start()

if __name__ == "__main__":
    get_main_func()