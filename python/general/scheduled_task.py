# The objective is to be able to execute a task regularly.
#
# Install : pip install APScheduler
# APScheduler page : https://pypi.org/project/APScheduler/

# Library to do something on shut down.
import atexit

# The APScheduler we installed earlier
from apscheduler.schedulers.background import BackgroundScheduler

# Task to execute on a regular basis
def method_to_excute():
    print("Hello world!")

# Create the scheduler
scheduler = BackgroundScheduler()
# --- Define all the jobs, their trigger and their interval
scheduler.add_job(func=method_to_excute, trigger="interval", seconds=3)
# --- Start the scheduler
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())





