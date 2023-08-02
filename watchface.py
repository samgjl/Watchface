# Kivy:
import os
import sys
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
LabelBase.register(name='Glitchy', fn_regular='fonts/GlitchGoblin.ttf') # Font

# Helper Functions:
def get_date():
    return date.today().strftime("%d-%m-%Y")
def get_time():
    return datetime.now().strftime("%H-%M-%S")

# Clock Widget that rotates between universes and the current time: 
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
            if self.collide_point(*touch.pos):
                self.num += 1
                self.clear_widgets()

# Clock widget that is just a clock:
class ClockStandalone(Label):
    def update(self, *args):
        self.text = get_time()

class QuitButton(Image):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            # os.system("sudo halt\n")
            quit()

class PowerButton(Image):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
           os.system("sudo halt\n")
           quit()

class WatchWidget(RelativeLayout):
    def __init__(self, **args):
        super(RelativeLayout, self).__init__(**args)
    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Rectangle(source='media/bkgd_vert.png', size=Window.size)
        
        layout = RelativeLayout(size_hint=(.75, .75), pos_hint={'x':0.125, 'y':0.15})
        # layout = RelativeLayout(size=Window.size)
        self.add_widget(layout)

        project_bootleg = Image(source='media/project_bootleg.png', 
                                fit_mode="scale-down", 
                                pos_hint={'x':0.075, 'y':0.375},
                                center_x=0.5,
                                center_y=0.5,
                                size_hint_x=0.85,
                                size_hint_y=0.85)
        layout.add_widget(project_bootleg)

        clock = ClockWidget(size_hint_x=1, size_hint_y=1, font_size=24,
                            font_name="Glitchy", 
                            color=(21/255, 230/255, 250/255, 1),
                            pos_hint={'x':0.1275, 'y':-0.155}, )
        Clock.schedule_interval(clock.update, 1/5)
        layout.add_widget(clock)

        oval = Image(source="media/oval.png",
                     allow_stretch=True,
                     keep_ratio=False,
                     size_hint_x=0.9,
                     size_hint_y=0.66,
                     pos_hint={'x':0.04, 'y':0.0},
                     center=(0.5, 0.5))
        layout.add_widget(oval)
        
        destination = Image(source="media/destination.png", 
                            fit_mode="scale-down",
                            size_hint_x=0.4,
                            size_hint_y=0.4,
                            pos_hint={'x':0.1, 'y':0.15}
                            )
        layout.add_widget(destination)

        flag = Image(source='media/uk_smile.png', 
                     pos_hint={'x':0.4, 'y':0.475},
                     size_hint_x=0.2,
                     size_hint_y=0.2,
                     center_x=0.5,
                     center_y=0.5)
        layout.add_widget(flag)
        
        bottom_smiley = Image(source="media/smile.png",
                              pos_hint={'x':0.45, 'y':-0.35},
                              size_hint_x=0.1,
                              )
        layout.add_widget(bottom_smiley)
        quote_1 = Image(source="media/open_quote.png",
                        pos_hint={'x':0.4125, 'y':-0.325},
                        size_hint_x=0.035)
        quote_2 = Image(source="media/close_quote.png",
                        pos_hint={'x':0.55, 'y':-0.325},
                        size_hint_x=0.035)
        layout.add_widget(quote_1)
        layout.add_widget(quote_2)

        powerbutton = QuitButton(source="media/powerbutton.png", 
                                  pos_hint={'x':0.9, 'y':0.05},
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