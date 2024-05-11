def add_time(start_time, duration, day=None):
  # Initial Variables
  result = ""
  start_hours = int(start_time.split()[0].split(":")[0])
  start_minutes = int(start_time.split()[0].split(":")[1])
  start_amORpm = start_time.split()[1]
  elapsed_hours = int(duration.split(":")[0])
  elapsed_minutes = int(duration.split(":")[1])

  # Convert Start Time to 24h
  if start_amORpm == "PM" and start_hours != 12:
    start_hours += 12
  elif start_amORpm == "AM" and start_hours == 12:
    start_hours = 0
  
  # Calculate End Time
  total_hours = start_hours + elapsed_hours
  total_minutes = start_minutes + elapsed_minutes
  if total_minutes >= 60:
    total_hours += 1
  end_hours = total_hours % 24
  end_minutes = total_minutes % 60

  # Calculate Days
  days_passed = total_hours // 24

  # Convert End Time back to 12h
  if end_hours < 12:
    end_amORpm = "AM"
  else:
    end_amORpm = "PM"
  if end_hours == 0:
    end_hours = 12
  if end_hours > 12:
    end_hours -= 12
  
  # Display End Time
  if end_minutes < 10:
    end_time = "{}:0{}".format(end_hours, end_minutes)
  else:
    end_time = "{}:{}".format(end_hours, end_minutes)
  result += end_time + " " + end_amORpm

  # Display Day of the Week if Wanted
  if day is not None:
    day_list = ["monday", "tuesday", "wednesday", "thursday", "friday",
    "saturday", "sunday"]
    day_index = day_list.index(day.lower())
    new_day_index = (day_index + days_passed) % 7
    new_day = day_list[new_day_index]
    result += ", " + new_day.capitalize()
  
  # Display Days Passed
  if days_passed == 1:
    result += " (next day)"
  elif days_passed > 1:
    result += " ({} days later)".format(days_passed)

  return result
 