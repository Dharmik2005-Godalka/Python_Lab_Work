from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text='Click Me', on_press=lambda x: print("Hello, Kivy!"))

MyApp().run()
