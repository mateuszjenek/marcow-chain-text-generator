import tkinter as tk

from frames.IFrame import IFrame
from generators.ITextGenerator import ITextGenerator

class GenericFrame(IFrame):
    title: str
    generator: ITextGenerator

    _width: int = 50

    def __init__(self, title: str, generator: ITextGenerator):
        self.title = title
        self.generator = generator

    def render(self, master):
        frame = tk.Frame(master=master)
        title = tk.Label(master=frame, text=self.title, width=self._width)
        title.pack()

        text = tk.Label(master=frame, text="Click button below to generate text", width=self._width, wraplength=300)
        text.pack()

        button = tk.Button(master=frame, text="Generate", width=self._width, command=lambda: self._update(text))
        button.pack()
        frame.pack(fill=tk.Y, side=tk.LEFT)

    def _update(self, text: tk.Label):
        line = self.generator.generate()
        text["text"] = line