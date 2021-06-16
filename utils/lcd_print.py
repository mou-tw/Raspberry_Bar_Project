# -*- coding: utf-8 -*-
import sys
from lcd_board_time import main
import time
import smbus2


def lcd_print_main():
    sys.modules['smbus'] = smbus2

    from RPLCD.i2c import CharLCD

    lcd = CharLCD('PCF8574', address=0x27, port=1, backlight_enabled=True)

    try:
        print('lcd printing')
        lcd.clear()
        while 1:
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Whiskey")
            lcd.cursor_pos = (1, 0)
            lcd.write_string("is coming......")
            time.sleep(5)
            break
            # main()
        # lcd.clear()
    except KeyboardInterrupt:
        print('closing')
    finally:
        lcd.clear()


if __name__ == "__main__":
    lcd_print_main()