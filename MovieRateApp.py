import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle

class ImageWidget(Widget):
    def __init__(self, **kwargs):
        super(ImageWidget, self).__init__(**kwargs)
        texture = Image('galaxy.jpg').texture
        with self.canvas:
            Rectangle(texture=texture, pos=self.pos, size_hint=None)
        
######################################################
class MovieRateApp(App):
    def build(self):
        layout = BoxLayout(padding=200, orientation='vertical')

        layout.add_widget(ImageWidget())
        
        self.textBox = TextInput(text='', multiline=False)
        layout.add_widget(self.textBox)
        
        submit = Button(text="SUBMIT")
        submit.bind(on_press=self.buttonClicked)
        layout.add_widget(submit)
        
        self.subText = Label(text="")
        layout.add_widget(self.subText)
        return layout

    def buttonClicked(self, submit):
        self.subText.text = "You wrote " + self.textBox.text

######################################################
if __name__ == '__main__':
    MovieRateApp().run()
