#pip install schedule


import schedule 
import time


def greet():
    print("Hello")

schedule.every(3).seconds.do(greet)
schedule.every(5).minutes.do(greet)
schedule.every(10).hours.do(greet)
schedule.every().day.at("12:00").do(greet)
schedule.every().monday.do(greet)
schedule.every().wednesday.at("13:15").do(greet)



while True:
    schedule.run_pending()
    time.sleep(1)
