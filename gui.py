import tkinter as tk

from marcow_chains.FirstOrderMarcowChain import FirstOrderMarcowChain
from generators.MotivateTextGenerator import MotivateTextGenerator
from generators.PickUpLinesGenerator import PickUpLinesGenerator
from frames.GenericFrame import GenericFrame

motivate_marcow_chain = FirstOrderMarcowChain()
pickup_marcow_chain = FirstOrderMarcowChain()

motivate_generator = MotivateTextGenerator(motivate_marcow_chain)
pickup_generator = PickUpLinesGenerator(pickup_marcow_chain)

motivate_frame = GenericFrame("Motivate text generator", motivate_generator)
pickup_frame = GenericFrame("Pick-up line generator", pickup_generator)

window = tk.Tk()

motivate_frame.render(window)
pickup_frame.render(window)

window.mainloop() 