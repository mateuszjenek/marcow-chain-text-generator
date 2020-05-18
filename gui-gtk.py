import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from view.GtkApplicationWindow import GtkApplicationWindow
from controller.GtkController import GtkController
from model.FirstOrderMarcowChain import FirstOrderMarcowChain

marcow_chain = FirstOrderMarcowChain()

controller = GtkController(marcow_chain)

window = GtkApplicationWindow(controller)
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()