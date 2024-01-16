def add_time(start_time, duration, *current_day):
    start_time_splitting = start_time.split(" ")
    s_am_or_pm = start_time_splitting[1]
    start_h_m = start_time_splitting[0].split(":")
    s_hours = int(start_h_m[0])
    s_minutes = int(start_h_m[1])
    given_duration_splitting_h_m = duration.split(":")
    g_hours = int(given_duration_splitting_h_m[0])
    g_minutes = g_hours * 60 + int(given_duration_splitting_h_m[1])
    name_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    new_day = 0
    final_time = ""
    if len(current_day) > 1 or (current_day != () and current_day[0].title() not in name_of_days):
        return "Error"
    while True:

        if s_minutes >= 60:
            s_minutes -= 60
            s_hours += 1
        if s_hours > 11 and s_am_or_pm == "AM":
            s_hours -= 12
            s_am_or_pm = "PM"
        if s_hours > 11 and s_am_or_pm == "PM":
            s_hours -= 12
            s_am_or_pm = "AM"
            new_day += 1
        if g_minutes == 0:
            if (current_day != ()) and (current_day[0].title() in name_of_days):
                for i in range(0, len(name_of_days)):
                    if current_day[0].lower() == name_of_days[i].lower():
                        temp = new_day
                        while temp >= 6:
                            temp -= 7
                        final_time += f", {name_of_days[temp + i]}"
            if new_day > 1:
                final_time += f" ({new_day} Days Later)"
            elif new_day == 1:
                final_time += " (next day)"
            break
        s_minutes += 1
        g_minutes -= 1

    if s_hours == 0:
        s_hours = 12

    return f"{s_hours:02d}:{s_minutes:02d} {s_am_or_pm}{final_time}"


# print( add_time("11:55 AM", "3:12"), "3:07 PM")
# print(3 add_time("9:15 PM", "5:30"), "2:45 AM (next day)")
# print(4, add_time("11:40 AM", "0:25"), "12:05 AM (next day)")
# print(5, add_time("11:59 PM", "24:05"), "12:04 AM (2 days later)")
# print(6, add_time("8:16 PM", "466:02"), "6:18 AM (20 days later)")
# print(7, add_time("5:01 AM", "0:00"), "5:01 AM")
# print(8, add_time("3:30 PM", "2:12", "Monday"), "5:42 PM, Monday")
# print(9, add_time("2:59 AM", "24:00", "saturDay"), "2:59 AM, Sunday (next day)")
# print(10, add_time("11:59 PM", "24:05", "Wednesday"), "12:04 AM, Friday (2 days later)")
# print(11, add_time("8:16 PM", "466:02", "tuesday"), "6:18 AM, Monday (20 days later)")