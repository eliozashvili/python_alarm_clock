
# Python alarm clock
import pygame
import datetime
import time


def set_alarm_clock(alarm_time):
    print(f"Alarm set for {alarm_time}")
    alarm_sound = "spaceship_alarm.mp3"

    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("\nWAKE UP!\n")

            pygame.mixer.init()
            pygame.mixer.music.load(alarm_sound)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("\nSet the alarm time in 24 hour format (HH:MM:SS): ")

    set_alarm_clock(alarm_time)
