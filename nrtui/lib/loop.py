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
        self.horizontal_offset = None
        self.invert_horizontal = False

        self.mouseinput = MouseInput()

    def start(self):
        while not self.stop:
            if self.active and self.ads:
                if mouse.is_pressed(button="right"):
                    if mouse.is_pressed(button="left"):
                        # Determina la direzione dell'offset orizzontale
                        horizontal_movement = (
                            -int(float(self.horizontal_offset))
                            if self.invert_horizontal
                            else int(float(self.horizontal_offset))
                        )

                        # Muove il mouse sia in verticale che in orizzontale
                        self.mouseinput.move(
                            int(float(self.offset)), horizontal_movement
                        )

                        # Ritardo tra i movimenti
                        time.sleep(float(self.delay) / 100)
            elif self.active:
                if mouse.is_pressed(button="left"):
                    # Determina la direzione dell'offset orizzontale
                    horizontal_movement = (
                        -int(float(self.horizontal_offset))
                        if self.invert_horizontal
                        else int(float(self.horizontal_offset))
                    )

                    # Muove il mouse sia in verticale che in orizzontale
                    self.mouseinput.move(int(float(self.offset)), horizontal_movement)

                    # Ritardo tra i movimenti
                    time.sleep(float(self.delay) / 100)

            # Ritardo per il ciclo while
            time.sleep(0.001)
