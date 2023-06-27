from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
import datetime
from datetime import date
from datetime import datetime


def take_date():
        # Today's Date (in )
        current_day = date.today()
        m_d_y = current_day.strftime("%d|%m|%Y")
        return m_d_y
def take_time():
    # Current time (PST)
    pst_time = datetime.now()
    h_m_s = pst_time.strftime("%H-%M-%S")
    return h_m_s

class MainApp(App):
    # Build
    def build(self):
        # Text:
        time = take_time()

        label = Label(text="Destination: " + time,
                      size_hint=(.5, .5),
                      pos_hint={'center_x':.5, 'center_y': .25})
        
        # Image:
        img = Image(source='flag_img.png',
                    size_hint=(1, .5),
                    pos_hint={'center_x':.5, 'center_y':.5})

        # return img

        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()