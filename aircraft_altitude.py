from aircraft import Aircraft

model= input("Enter aircraft model:\n")
aircraft= Aircraft(model)

while True:
    command=input("Enter command (A for ascent, D for descent, X to exit):\n")

    if command =="X":
        break

    parts=command.split()
    action= parts[0]
    value=int(parts[1])

    if action=="A":
        aircraft.ascend(value)
    elif action == "D":
        aircraft.descend(value)

print(f"Final altitude: {aircraft.altitude} feet")