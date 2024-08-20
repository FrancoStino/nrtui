import time

import mouse
from .mouseinput import MouseInput


class Loop:
    def __init__(self):
        self.stop = False
        self.active = False

        self.ads = False
        self.offset = None
        self.delay = None
        self.horizontal_offset = None  # Nuovo parametro per il movimento orizzontale

        self.mouseinput = MouseInput()

    def start(self):
        while not self.stop:
            if self.active and self.ads:
                if mouse.is_pressed(button="right"):
                    if mouse.is_pressed(button="left"):
                        # Movimento verticale
                        self.mouseinput.move(int(self.offset))

                        # Movimento orizzontale (destra)
                        self.mouseinput.move_horizontal(int(self.horizontal_offset))

                        # Ritardo tra i movimenti
                        time.sleep(float(self.delay) / 100)
            elif self.active:
                if mouse.is_pressed(button="left"):
                    # Movimento verticale
                    self.mouseinput.move(int(self.offset))

                    # Movimento orizzontale (destra)
                    self.mouseinput.move_horizontal(int(self.horizontal_offset))

                    # Ritardo tra i movimenti
                    time.sleep(float(self.delay) / 100)

            # Ritardo per il ciclo while
            time.sleep(0.001)
