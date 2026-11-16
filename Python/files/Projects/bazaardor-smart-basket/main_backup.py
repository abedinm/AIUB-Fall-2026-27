"""BazarDor Smart Basket: run this file to start the app (python main.py)."""

import os
import tkinter as tk
from tkinter import ttk

from gui_basket import BasketTab
from manager import BazaarManager
from storage import PRICES_FILE, load_records


class App:
    def __init__(self, root):
        self.root = root
        root.title("BazarDor Smart Basket")
        root.geometry("1000x650")

        self.status = ttk.Label(root, padding=(10, 4), anchor="w")
        self.status.pack(side="bottom", fill="x")

        self.manager = BazaarManager(load_records())
        self.tabs = ttk.Notebook(root)
        self.tabs.pack(fill="both", expand=True)
        BasketTab(self, self.tabs)

        count = len(self.manager.records)
        if count:
            self.say(f"Loaded {count} price records from {PRICES_FILE}.")
        else:
            self.say(f"No price records found in {PRICES_FILE}.")

    def say(self, text):
        """Show a message in the status bar at the bottom of the window."""
        self.status.config(text=text)


if __name__ == "__main__":
    # data/prices.json is a relative path, so run from this file's folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    root = tk.Tk()
    App(root)
    root.mainloop()
