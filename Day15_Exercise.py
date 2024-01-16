

# Morning 5 am to 12 pm (noon)
# Afternoon 12 pm to 5 pm.
# Evening 5 pm to 9 pm.
# Night 9 pm to 4 am.
import time
name = input("Enter you name, Sir\n")
tm = int(time.strftime("%H"))
if 5 <= tm < 12:
    print("Good morning,", name)
elif 12 <= tm < 17:
    print("Good Afternoon,", name)
elif 17 <= tm < 21:
    print("Good evening,", name)
else:
    print("Good night,", name)