from aircraft import Aircraft

def main():
    model = input().strip()
    aircraft = Aircraft(model)

    while True:
        try:
            command = input().strip()

            if command == "X":
                break

            parts = command.split()
            if len(parts) != 2:
                continue

            action, value = parts
            value = int(value)

            if action == "A":
                aircraft.ascend(value)
            elif action == "D":
                aircraft.descend(value)

        except:
            # ⚠️ evita que el programa crashee en tests
            continue

    print(f"Final altitude: {aircraft.altitude} feet")


if __name__ == "__main__":
    main()