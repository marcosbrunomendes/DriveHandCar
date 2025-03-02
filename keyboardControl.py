"""
Módulo para simulação de entrada de teclado.

Utiliza o pynput para simular o pressionamento e a liberação de teclas.
"""

from pynput.keyboard import Controller, Key
from typing import Union

# Inicializa o controlador de teclado
keyboard_ctrl: Controller = Controller()


def press_key(key: Union[str, Key]) -> None:
    """
    Simula o pressionamento de uma tecla.

    :param key: A tecla a ser pressionada (ex.: 'a', 'w', 's', 'd' ou Key.xxx).
    """
    keyboard_ctrl.press(key)


def release_key(key: Union[str, Key]) -> None:
    """
    Simula a liberação de uma tecla.

    :param key: A tecla a ser liberada (ex.: 'a', 'w', 's', 'd' ou Key.xxx).
    """
    keyboard_ctrl.release(key)
