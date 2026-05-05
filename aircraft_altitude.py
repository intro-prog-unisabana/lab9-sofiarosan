from aircraft import Aircraft

def main():
    model = input().strip()  # ⚠️ SIN mensaje (los tests no esperan texto)
    aircraft = Aircraft(model)

    while True:
        command = input().strip()

        if command == "X":
            break

        parts = command.split()

        # Validar entrada
        if len(parts) != 2:
            continue

        action, value = parts

        # Validar número
        if not value.isdigit():
            continue

        value = int(value)

        if action == "A":
            aircraft.ascend(value)
        elif action == "D":
            aircraft.descend(value)

    print(f"Final altitude: {aircraft.altitude} feet")


if __name__ == "__main__":
    main()