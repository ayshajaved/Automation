import time
import random
from plyer import notification

'''
The Plyer library is a Python library that provides a platform-independent API to access hardware and platform-specific features of a device, such as notifications, battery status, or sensors, without requiring platform-specific code. It acts as a cross-platform wrapper, allowing developers to write a single codebase that works on Windows, macOS, Linux, Android, and iOS.
'''
#Notification reminder class
class Reminder:
    def send_notification(self,title, message):
        # Send desktop notification
        try:
            notification.notify(
                title=title,
                message=message,
                app_name="Task Reminder",
                timeout=10
            )
        except Exception as e:
            print(f"Error sending notification: {e}")

    def get_random_message(self):
        messages = [
            "Time for a quick break! Stretch and recharge.",
            "You're doing great! Keep tackling those tasks.",
            "Almost there! Finish one more task before a break.",
            "Stay hydrated! Grab some water and keep going.",
        ]
        return random.choice(messages)

#Main class
class Main:
    @staticmethod
    def run():
        obj = Reminder()
        # Get user input
        interval_minutes = float(input("Enter reminder interval (minutes, e.g., 30): "))
        num_reminders = int(input("How many reminders do you want? "))
        
        print(f"Starting reminder system. Notifications every {interval_minutes} minutes.")
        
        for i in range(num_reminders):
            title = f"Reminder #{i+1}"
            message = obj.get_random_message()
            obj.send_notification(title, message)
            print(f"Sent: {title} - {message}")
            time.sleep(interval_minutes * 60)  # Convert to seconds
        
        print("Reminder system finished.")


if __name__ == "__main__":
    Main.run()