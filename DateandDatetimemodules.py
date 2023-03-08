"""datetime and date separate modules"""
import datetime

current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

# # Get the date only
current_date = current_datetime.date()
print("Current date:", current_date)

# # Get the time only
current_time = current_datetime.time()
print("Current time:", current_time)

# # Create a datetime object for a specific date and time
new_datetime = datetime.datetime(2022, 3, 1,6, 30, 0)
print("New datetime:", new_datetime)


# # Format a datetime object as a string
date_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime string:", date_string)


# # Parse a string into a datetime object
parsed_datetime = datetime.datetime.strptime("2022-03-01 12:30:00", "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed_datetime)

   #date module.
import time

current_time = time.time()
print("\n Current timestamp:", current_time)

# Wait for 2 seconds
time.sleep(4)
print("Waited for 4 seconds")

current_time = time.time()
print("Current timestamp:", current_time)