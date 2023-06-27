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