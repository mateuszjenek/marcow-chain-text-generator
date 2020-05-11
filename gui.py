import tkinter as tk

from marcow_chains.FirstOrderMarcowChain import FirstOrderMarcowChain
from generators.MotivateTextGenerator import MotivateTextGenerator
from generators.PickUpLinesGenerator import PickUpLinesGenerator
from frames.MotivateFrame import MotivateFrame
from frames.PickUpFrame import PickUpFrame

motivate_generator = MotivateTextGenerator(FirstOrderMarcowChain())
pickup_generator = MotivateTextGenerator(FirstOrderMarcowChain())

motivate_frame = MotivateFrame(motivate_generator)
pickup_frame = PickUpFrame(pickup_generator)

window = tk.Tk()

motivate_frame.render(window)
pickup_frame.render(window)

window.mainloop() 