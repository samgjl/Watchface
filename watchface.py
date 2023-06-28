# Kivy:
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.text import FontContextManager as FCM
from kivy.lang import Builder
from kivy.graphics import *
from kivy.config import Config
# Date/Time
from datetime import date
from datetime import datetime


# CONSIDER USING RelativeWindow!
# Consider USING RelativeLayout!


# Declare window size:
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '480')
Config.set('graphics', 'resizable', False)
Config.write()
# Window.size = (320, 480)
LabelBase.register(name='Glitchy', fn_regular='GlitchGoblin.ttf') # Font

# Helper Functions:
def get_date():
    return date.today().strftime("%d-%m-%Y")
def get_time():
    return datetime.now().strftime("%H-%M-%S")

class ClockWidget(Label):
    num = 0
    def update(self, *args):
        self.texts = ["-1218             ", 
                      "-1610             ", 
                      "-42               ", 
                      "-65               ", 
                      "-" + get_time() + "       "]
        self.text = self.texts[self.num % len(self.texts)]

    def on_touch_down(self, touch):
            if True or self.collide_point(*touch.pos):
                self.num += 1
                self.clear_widgets()
        
    

class ClockStandalone(Label):
    def update(self, *args):
        self.text = get_time()

class WatchFace(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Rectangle(source='bgkd_test.png', size=Window.size)
        
        layout = BoxLayout(orientation="vertical", size=Window.size)
        self.add_widget(layout)

        # project_bootleg = Label(text="Project: Bootleg", 
        #                              color=(21/255, 230/255, 250/255, 1), 
        #                              font_size=30,
        #                              font_name="Glitchy")
        project_bootleg = Image(source='project_bootleg.png', fit_mode="scale-down")
        layout.add_widget(project_bootleg)

        image = Image(source='IMG_6934.png')
        # image = Image(source='flag__img.png')
        layout.add_widget(image)

        clock = ClockWidget(pos_hint={'x': 0, 'y': 0, 'center_x': 0.0}, 
                                 font_size=28, 
                                 color=(21/255, 230/255, 250/255, 1),
                                 font_name="Glitchy",
                                 )
        Clock.schedule_interval(clock.update, 1.0 / 5.0)         
        mini = BoxLayout(orientation="horizontal", pos_hint={'x':0.05, 'y':0})
        destination = Image(source="destination.png", 
                            fit_mode="scale-down",
                            )
        mini.add_widget(destination)
        mini.add_widget(clock)
        layout.add_widget(mini)
        
        bottom_smiley = Label(text='":smile:"')
        layout.add_widget(bottom_smiley)


class HelloWorldApp(App):
    def build(self):
        self.layout = WatchFace(orientation='vertical')
        # self.lower_layout = BoxLayout(orientation="horizontal")

        # self.project_bootleg = Label(text="Project: Bootleg", 
        #                              color=(21/255, 230/255, 250/255, 1), 
        #                              font_size=30,
        #                              font_name="Glitchy")
        # self.layout.add_widget(self.project_bootleg)

        # self.image = Image(source='flag_img.png')
        # self.layout.add_widget(self.image)

        # self.clock = ClockWidget(pos_hint={'x': 0.5, 'y': 1, 'center_x': 0, 'center_y': .5}, 
        #                          font_size=30, 
        #                          color=(21/255, 230/255, 250/255, 1),
        #                          font_name="Glitchy"
        #                          ) # background_color=(0,0,0,1) <-- For Button
        # Clock.schedule_interval(self.clock.update, 1.0 / 60.0)
        # self.layout.add_widget(self.clock)  

        # self.layout.add_widget(self.lower_layout)
        # self.lower_layout.add_widget(Label(text="DESTINATION", font_name="Glitchy"))  
        # self.lower_layout.add_widget(Label(text="q2"))  

        

        # self.bottom_smiley = Button(text='":smile:"', background_color=(0,0,0, 1))
        # # self.layout.add_widget(self.bottom_smiley)

        return self.layout
        
if __name__ == "__main__":
    HelloWorldApp().run()