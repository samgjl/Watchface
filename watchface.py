# Kivy:
import os
os.environ['KIVY_IMAGE'] = 'sdl2, gif'
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.graphics import Rectangle
from kivy.config import Config
# Date/Time
from datetime import date
from datetime import datetime

# Declare window size:
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '320')
# Config.set('graphics', 'resizable', False)
Config.write()
Window.size = (480, 320)
LabelBase.register(name='Glitchy', fn_regular='GlitchGoblin.ttf') # Font

# Helper Functions:
def get_date():
    return date.today().strftime("%d-%m-%Y")
def get_time():
    return datetime.now().strftime("%H-%M-%S")

class ClockWidget(Label):
    num = 0
    def update(self, *args):
        self.texts = [" -" + get_time(),
                      "-1218      ", 
                      "-1610      ", 
                      "-42        ", 
                      "-65        "]
        self.text = self.texts[self.num % len(self.texts)]

    def on_touch_down(self, touch):
            if True or self.collide_point(*touch.pos):
                self.num += 1
                self.clear_widgets()

class ClockStandalone(Label):
    def update(self, *args):
        self.text = get_time()

class PowerButton(Image):
    def on_touch_down(self, touch):
        if True or self.collide_point(*touch.pos):
            quit()



class WatchWidget(RelativeLayout):
    def __init__(self, **args):
        super(RelativeLayout, self).__init__(**args)
    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Rectangle(source='bkgd_test.png', size=Window.size)
        
        layout = RelativeLayout(size=Window.size)
        self.add_widget(layout)

        project_bootleg = Image(source='project_bootleg.png', 
                                fit_mode="scale-down", 
                                pos_hint={'x':0, 'y':0.334})
        layout.add_widget(project_bootleg)

        flag = Image(source='IMG_6934.png', 
                     pos_hint={'x':0, 'y':0.1},)
        layout.add_widget(flag)

        sublayout = RelativeLayout(pos_hint={'x':0, 'y':0.0})

        clock = ClockWidget(size_hint_x=1, size_hint_y=1, font_size=30,
                            font_name="Glitchy", 
                            color=(21/255, 230/255, 250/255, 1),
                            pos_hint={'x':0.1275, 'y':-0.1})
        Clock.schedule_interval(clock.update, 1/5)
        sublayout.add_widget(clock)

        destination = Image(source="destination.png", 
                            fit_mode="scale-down",
                            size_hint_x=0.4,
                            size_hint_y=0.4,
                            pos_hint={'x':0.1, 'y':0.2}
                            )
        sublayout.add_widget(destination)

        layout.add_widget(sublayout)
        
        bottom_smiley = Label(text='":smile:"', pos_hint={'x':0.0, 'y':-0.25})
        layout.add_widget(bottom_smiley)

        powerbutton = PowerButton(source="powerbutton.png", 
                                  pos_hint={'x':0.9, 'y':0.9},
                                  size_hint_x=0.1,
                                  size_hint_y=0.1,
                                  )
        layout.add_widget(powerbutton)


class Watchface(App):
    def build(self):
        self.layout = WatchWidget()
        return self.layout
        
if __name__ == "__main__":
    Watchface().run()