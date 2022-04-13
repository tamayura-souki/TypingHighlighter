from pynput import keyboard, mouse
import pygame
from pygame.mixer import Sound

class SoundEffect:
    def __init__(self, config: dict):
        pygame.mixer.init()

        self.key_type_sound: Sound = self._load_sound(config["normal_key_type"])
        self.enter_type_sound: Sound = self._load_sound(config["enter_key_type"])
        self.mouse_click_sound: Sound = self._load_sound(config["mouse_click"])
        self.mouse_wheel_sound: Sound = self._load_sound(config["mouse_wheel"])

        self.key_released = {}

        key_listener = keyboard.Listener(
            on_press=self.key_on_press, on_release=self.key_on_release
        )
        key_listener.start()
        mouse_listener = mouse.Listener(
            on_click=self.mouse_on_click, on_scroll=self.mouse_on_scroll
        )
        mouse_listener.start()

    def _load_sound(self, config_data: dict) -> Sound:
        sound = Sound(config_data["path"])
        sound.set_volume(config_data["volume"])
        return sound

    def key_on_press(self, key: keyboard.KeyCode | keyboard.Key):
        if not self.key_released.get(key, True):
            return None

        if key == keyboard.Key.enter:
            self.enter_type_sound.play()
        else:
            self.key_type_sound.play()

        self.key_released[key] = False

    def key_on_release(self, key: keyboard.KeyCode | keyboard.Key):
        self.key_released[key] = True

    def mouse_on_click(self, x, y, button, pressed):
        if pressed:
            self.mouse_click_sound.play()

    def mouse_on_scroll(self, x, y, dx, dy):
        self.mouse_wheel_sound.stop()
        self.mouse_wheel_sound.play()
