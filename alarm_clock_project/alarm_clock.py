
class Alarm_clock:
    def __init__(self):
      self.current_time = "11:11pm"
      self.alarm_on = False
      self.alarm_time = "OFF"


    def toggle_alarm(self):
      on_or_off = input("Turn the alarm ON or keep OFF? ON or OFF:  ")
      answered_correctly = False
      
      while answered_correctly == False:
            if on_or_off.lower() == 'on':
              answered_correctly = True
              self.alarm_time = input('What time would you like to be alarmed? "6:45am"?  ')
              self.alarm_on = True
              print("---------------------------------")
              print(f"Great your alarm is set to {self.alarm_time}")
              print("---------------------------------")
              print(f"It is currently {self.current_time}")
              print("---------------------")
              print("Alarm ON")
              print("--------")
            elif on_or_off.lower() == "off":
              answered_correctly =True
              self.alarm_on = False
              self.alarm_time = "OFF"
              print("--------")
              print("Alarm OFF")
              print("--------")
            else:
              print("Try a different answer")
              on_or_off = input("Turn the alarm ON or keep OFF? ON or OFF:  ")
