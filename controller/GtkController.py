import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from model.IMarcowChain import IMarcowChain

class GtkController():
    def __init__(self, marcow_chain: IMarcowChain):
        self.__marcow_chain = marcow_chain

    def add_source(self, source_list_widget: Gtk.ListBox, window: Gtk.Window):
        dialog = Gtk.FileChooserDialog(
            "Wybierz plik z przykładowymi tekstami",
            window,
            Gtk.FileChooserAction.OPEN,
            (
                Gtk.STOCK_CANCEL,
                Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OPEN,
                Gtk.ResponseType.OK,
            ),
        )

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print(dialog.get_filename())
            lines = open(dialog.get_filename(), encoding='utf8').read().splitlines()
            self.__marcow_chain.feed(lines)
            source_list_widget.add(Gtk.Label(dialog.get_filename()))
            window.show_all()
        dialog.destroy()

    def reset_sources(self, source_list_widget: Gtk.ListBox, window: Gtk.Window):
        self.__marcow_chain.reset()
        source_list_widget.foreach(lambda widget: source_list_widget.remove(widget))
        pass

    def generate_sentence(self, generated_text_widget: Gtk.Label):
        text = self.__marcow_chain.generate()
        generated_text_widget.set_text(text)
