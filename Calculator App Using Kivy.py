from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorGrid(GridLayout):
    def __init__(self, **kwargs):
        super(CalculatorGrid, self).__init__(**kwargs)
        self.cols = 4

        self.result = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        self.add_widget(self.result)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+'
        ]

        for button in buttons:
            self.add_widget(Button(text=button, font_size=24, on_press=self.on_button_press))

        self.add_widget(Button(text="C", font_size=24, on_press=self.clear_result))

    def on_button_press(self, instance):
        current_text = self.result.text
        button_text = instance.text

        if button_text == "=":
            try:
                self.result.text = str(eval(current_text))
            except Exception:
                self.result.text = "Error"
        else:
            if current_text == "Error":
                self.result.text = button_text
            else:
                self.result.text += button_text

    def clear_result(self, instance):
        self.result.text = ""

class CalculatorApp(App):
    def build(self):
        return CalculatorGrid()

if __name__ == '__main__':
    CalculatorApp().run()
