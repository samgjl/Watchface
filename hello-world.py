import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.clock import Clock
import datetime
from datetime import date
from datetime import datetime


# Declare window size:
Window.size = (400, 700)

# Helper Functions:
def get_date():
    return date.today().strftime("%d/%m/%Y")
def get_time():
    return datetime.now().strftime("%H-%M-%S")

class ClockWidget(Label):
    num = 0
    def update(self, *args): 
        self.texts = ["Destination: 42", "Destination: 1610", "Destination: " + get_time()]
        self.text = self.texts[self.num % len(self.texts)]
        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.num += 1
            self.clear_widgets()


class HelloWorldApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.ptoject_bootleg = Label(text="Project: Bootleg")
        self.layout.add_widget(self.ptoject_bootleg)

        self.clock = ClockWidget(pos_hint={'x': 0, 'y': 1, 'center_x': .5, 'center_y': .5}, font_size=30)
        Clock.schedule_interval(self.clock.update, 1.0 / 60.0)
        self.layout.add_widget(self.clock)     

        return self.layout
        
if __name__ == "__main__":
    HelloWorldApp().run()