from aircraft import Aircraft

def main():
    model = input().strip()
    aircraft = Aircraft(model)

    while True:
        command = input().strip()

        if command == "X":
            break

        parts = command.split()
        if len(parts) != 2:
            continue

        action, value = parts
        value = int(value)

        # 🔥 CONTROL DIRECTO (no dependes de métodos raros)
        if action == "A":
            aircraft.altitude += value
        elif action == "D":
            aircraft.altitude -= value

    print(f"Final altitude: {aircraft.altitude} feet")


if __name__ == "__main__":
    main()