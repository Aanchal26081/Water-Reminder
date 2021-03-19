import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title= "Please drink water",
            message = "Its important",
            app_icon = "water.ico",
            timeout = 10
        )

        time.sleep(60*60)