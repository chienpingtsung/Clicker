import random
import time

from pynput import keyboard, mouse


class Clicker:
    def __init__(self, shortcut, interval, elastic=0):
        self.shortcut = shortcut
        self.interval = interval
        self.elastic = elastic

        self.click = False
        self.exit = False

        self.mouse = mouse.Controller()

    def on_press(self, key):
        if key == self.shortcut:
            if self.click:
                self.click = False
                print('Stop clicking.')
            else:
                self.click = True
                print('Start clicking.')
            return

        if key == keyboard.Key.esc:
            self.exit = True
            print('Quit clicker.')
            return

    def run(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        while True:
            time.sleep((self.interval + random.uniform(-self.elastic, self.elastic)) / 1000)

            if self.exit:
                return

            if self.click:
                self.mouse.click(mouse.Button.left)


if __name__ == '__main__':
    clicker = Clicker(keyboard.Key.shift_r, 200, 10)
    clicker.run()
