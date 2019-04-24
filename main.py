import kivy
import db

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
kivy.require('1.10.1')


class AppBoxLayout(BoxLayout):
    def send_greetings(self, name, greeting):
        db.send_greetings(name, greeting)


class GreetingApp(App):

    def build(self):
        Config.set('graphics', 'width', '500')
        Config.set('graphics', 'height', '400')
        Config.write()

        return AppBoxLayout()


if __name__ == '__main__':
    GreetingApp().run()
