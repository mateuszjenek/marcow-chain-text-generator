import tkinter as tk

from marcow_chains.FirstOrderMarcowChain import FirstOrderMarcowChain
from generators.MotivateTextGenerator import MotivateTextGenerator
from generators.PickUpLinesGenerator import PickUpLinesGenerator
from frames.GenericFrame import GenericFrame

motivate_generator = MotivateTextGenerator(FirstOrderMarcowChain())
pickup_generator = PickUpLinesGenerator(FirstOrderMarcowChain())

motivate_frame = GenericFrame("Motivate text generator", motivate_generator)
pickup_frame = GenericFrame("Pick-up line generator", pickup_generator)

window = tk.Tk()

motivate_frame.render(window)
pickup_frame.render(window)

window.mainloop() 