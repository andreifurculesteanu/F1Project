from src.menu.menu import Menu
import sys

is_dev = len(sys.argv) == 2

menu = Menu(is_dev)
menu.menu()
