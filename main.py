import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty

import db

Builder.load_file('greeting.kv')
kivy.require('1.10.1')


class GreetingLayout(BoxLayout):
    author = StringProperty()
    greeting = StringProperty()

    def __init__(self, **kwargs):
        super(GreetingLayout, self).__init__(**kwargs)
        self.author = kwargs['author']
        self.greeting = kwargs['greeting']


class SendGreetingsScreen(Screen):
    @staticmethod
    def send_greetings(name, greeting):
        db.send_greetings(name, greeting)

    def open_popup(self):
        pass


class ViewGreetingsScreen(Screen):
    layout_content = ObjectProperty(None)
    page = 1

    def __init__(self, **kwargs):
        super(ViewGreetingsScreen, self).__init__(**kwargs)
        self.layout_content.bind(minimum_height=self.layout_content.setter('height'))

        for greeting in range(100):
            self.layout_content.add_widget(GreetingLayout(author="Dupa", greeting="DUpa"))


screenManager = ScreenManager()
screenManager.add_widget(SendGreetingsScreen(name="sendScreen"))
screenManager.add_widget(ViewGreetingsScreen(name="viewScreen"))


class GreetingApp(App):

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        Config.set('graphics', 'width', '500')
        Config.set('graphics', 'height', '400')
        Config.write()

        return screenManager


if __name__ == '__main__':
    GreetingApp().run()
