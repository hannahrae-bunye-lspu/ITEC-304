from kivy.app import App
from kivy.lang import Builder
 
root = Builder.load_string('''
FloatLayout:
    canvas.before:
        Color:
            rgba: 0, 230, 255, 0.3
        Rectangle:
            # self here refers to the widget i.e FloatLayout
            pos: self.pos
            size: self.size
    Button:
        text: 'Hello World!!'
        size_hint: .2, .2
        pos_hint: {'center_x':.5, 'center_y': .5}
''')
 
class Button(App):
 
    def build(self):
        return root
 
if __name__ == '__main__':
    Button().run()
