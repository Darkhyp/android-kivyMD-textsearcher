import timeit

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window

from kivymd.app import MDApp

from ggnumber import PHRASE_FOR_SEARCH, SAMPLE_TEXT_FOR_BENCH, count_occurences_in_text
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class SearchTextNavigationDrawer(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('main.kv')
        # Window.bind(on_keyboard=self.events)
        # self.manager_open = False
        # self.file_manager = MDFileManager(
        #     exit_manager=self.exit_manager,
        #     select_path=self.select_path,
        #     previous=True,
        # )

    def build(self):
        # return Builder.load_string(KV)
        # return Builder.load_file()

        # self.screen.ids.onSearch.on_release = self.on_search
        # self.screen.ids.file_manager.on_release = self.file_manager_open

        # load defaulting text into MDTextField with id var1
        self.screen.ids.var1.text = SAMPLE_TEXT_FOR_BENCH
        # load defaulting searching phrase into MDTextField with id var2
        self.screen.ids.var2.text = PHRASE_FOR_SEARCH
        # self.screen.ids.text_field_error.bind(
        #     on_text_validate=self.set_error_message,
        #     on_focus=self.set_error_message,
        # )
        return self.screen

    def on_search(self):
        # var1 = self.screen.ids.var1.text
        var1 = self.screen.ids.var1.text
        var2 = self.screen.ids.var2.text

        execution_time = timeit.default_timer() # in nanoseconds
        ncount = count_occurences_in_text(var2, var1)
        execution_time = timeit.default_timer() - execution_time

        self.screen.ids.out.text = f"There is(are) {ncount} occurence(s). Execution time = {execution_time*1e6:.2f} ms";

    # def file_manager_open(self):
    #     self.file_manager.show('/')  # output manager to the screen
    #     self.manager_open = True
    #
    # def select_path(self, path):
    #     '''It will be called when you click on the file name
    #     or the catalog selection button.
    #
    #     :type path: str;
    #     :param path: path to the selected directory or file;
    #     '''
    #
    #     self.exit_manager()
    #     toast(path)
    #
    # def exit_manager(self, *args):
    #     '''Called when the user reaches the root of the directory tree.'''
    #
    #     self.manager_open = False
    #     self.file_manager.close()
    #
    # def events(self, instance, keyboard, keycode, text, modifiers):
    #     '''Called when buttons are pressed on the mobile device.'''
    #
    #     if keyboard in (1001, 27):
    #         if self.manager_open:
    #             self.file_manager.back()
    #     return True


SearchTextNavigationDrawer().run()
