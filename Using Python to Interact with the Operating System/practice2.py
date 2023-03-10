def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
     if event.machine not in machines:
         machines[event.machine] = set()
     if   event.type == "login":
         machines[event.machine].add(event.user)
     elif event.type == "logout":
        machines[event.machine].remove(evvent.user)
    return machines

def genrate_report(machines):
    for machine, users in machines.item():
        if len(users) > 0:
            user_list =", ".join(users)
            print("{}: {}".format(machine, user_list))   