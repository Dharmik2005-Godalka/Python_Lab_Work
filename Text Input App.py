from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input = TextInput(hint_text="Type something here", multiline=False, font_size=20)
        layout.add_widget(self.input)

        self.label = Label(text="", font_size=30)
        layout.add_widget(self.label)

        btn = Button(text="Show Text", font_size=24)
        btn.bind(on_press=self.show_text)
        layout.add_widget(btn)

        return layout

    def show_text(self, instance):
        self.label.text = self.input.text

if __name__ == '__main__':
    TextInputApp().run()
