import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from controller.GtkController import GtkController

class GtkApplicationWindow(Gtk.Window):
    def __init__(self, controller: GtkController):
        Gtk.Window.__init__(self, title="Generator tekstów")

        source_list_widget = Gtk.ListBox()
        generated_text_widget = Gtk.Label()

        # MENU

        main_column = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        
        top_row = Gtk.Box(spacing=10)
        sources_column = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        sources_column.add(Gtk.Label(label="Źródła danych:"))
        sources_column.add(source_list_widget)
        top_row.add(sources_column)

        buttons_column = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        new_source_button = Gtk.Button(label="Nowe źródło")
        new_source_button.connect("clicked", lambda x: controller.add_source(source_list_widget, self))
        buttons_column.add(new_source_button)

        delete_sources_button = Gtk.Button(label="Usuń wszystkie źródła")
        delete_sources_button.connect("clicked", lambda x: controller.reset_sources(source_list_widget, self))
        buttons_column.add(delete_sources_button)

        generate_button = Gtk.Button(label="Generuj")
        generate_button.connect("clicked", lambda x: controller.generate_sentence(generated_text_widget))
        buttons_column.add(generate_button)

        top_row.add(buttons_column)
        main_column.add(top_row)

        main_column.add(Gtk.Label("Wygenerowany tekst:"))
        main_column.add(generated_text_widget)

        self.add(main_column)
