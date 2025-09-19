from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CounterApp(App):
    def build(self):
        self.count = 0

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text="Count: 0", font_size=30)
        layout.add_widget(self.label)

        btn = Button(text="Increment", font_size=24)
        btn.bind(on_press=self.increment_count)
        layout.add_widget(btn)

        return layout

    def increment_count(self, instance):
        self.count += 1
        self.label.text = f"Count: {self.count}"

if __name__ == '__main__':
    CounterApp().run()
