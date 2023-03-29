from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Define the number of days in a week
DAYS_IN_WEEK = 7

# Initialize an empty list to store sleep data
sleep_data = []

# Prompt the user to input their sleep data for each day of the week
for i in range(DAYS_IN_WEEK):
    # Prompt the user to enter the date of the sleep data
    date_str = input(f"Enter the date for day {i+1} (YYYY-MM-DD): ")
    date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Prompt the user to enter the number of hours of sleep
    hours = float(input(f"Enter the number of hours of sleep for day {i+1}: "))
    
    # Prompt the user to enter how they felt before going to bed
    pre_sleep_mood = input(f"Enter how you felt before going to bed on day {i+1}: ")
    
    # Prompt the user to enter how they felt after waking up
    post_sleep_mood = input(f"Enter how you felt after waking up on day {i+1}: ")
    
    # Append the sleep data as a tuple to the sleep_data list
    sleep_data.append((date, hours, pre_sleep_mood, post_sleep_mood))

# Calculate the total hours of sleep for the week
total_hours = sum(hours for date, hours, pre_sleep_mood, post_sleep_mood in sleep_data)

# Calculate the average hours of sleep for the week
average_hours = total_hours / DAYS_IN_WEEK

# Print the sleep data for the week
print(f"\nSleep data for the week:\n{'Date':<12}{'Hours of sleep':<16}{'Pre-sleep mood':<16}{'Post-sleep mood':<16}")
for date, hours, pre_sleep_mood, post_sleep_mood in sleep_data:
    print(f"{date.strftime('%Y-%m-%d'):<12}{hours:<16.2f}{pre_sleep_mood:<16}{post_sleep_mood:<16}")
print(f"Total hours of sleep: {total_hours:.2f}")
print(f"Average hours of sleep: {average_hours:.2f}")

# Extract the dates and hours of sleep from the sleep_data list
dates = [date.strftime('%Y-%m-%d') for date, _, _, _ in sleep_data]
hours_of_sleep = [hours for _, hours, _, _ in sleep_data]

# Create a figure and axis for the line graph
fig, ax = plt.subplots()

# Plot the hours of sleep as a line graph
ax.plot(dates, hours_of_sleep, marker='o')

# Set the axis labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Hours of Sleep')
ax.set_title('Sleep Data for the Week')

# Display the line graph
plt.show()
