
from alarm_clock import Alarm_clock

wake_up = Alarm_clock()
print(wake_up.current_time)
print(wake_up.alarm_on)
print(wake_up.alarm_time)


turn_alarm_on = wake_up.toggle_alarm()
print(wake_up.alarm_on)
print(wake_up.alarm_time)

turn_alarm_off = wake_up.toggle_alarm()
print(wake_up.alarm_on)
print(wake_up.alarm_time)