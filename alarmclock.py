"alarm clock - thats sets an alarm"

import time

print(time.strftime("%H:%M:%S"))
print("This is the Current time and the format of time")
alarm_time = input("Set your alram in format (H:M:S) : ")
print(f"Your alarm has been set to {alarm_time}")


while True:
 current_time = time.strftime("%H:%M:%S")

 if current_time == alarm_time :
    print("Wake up and Work hard.")
    break

 time.sleep(1)

