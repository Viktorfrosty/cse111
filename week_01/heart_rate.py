"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
user_age=int(input("what is your age: "))
heart_rate = 220 - user_age
min_heart_rate = heart_rate * 0.65
max_heart_rate = heart_rate * 0.85
print(F"Your maximun heart rate is: {heart_rate:.0f} beats per minute, the minimun required to strengthen your heart is: {min_heart_rate:.0f} beats per minute, and the maximun recommended is: {max_heart_rate:.0f} beats per minute.")