# Copyright (c) 2023 ot2i7ba
# https://github.com/ot2i7ba/
# This code is licensed under the MIT License (see LICENSE for details).

"""
GreyKey Password Cleaner [GPC] v0.1
This script processes a text file (passwords.txt) to extract and clean up a list of possible passwords based on user-defined criteria.
"""

import os
import sys
import time

def clear_screen():
    """Clears the console screen."""
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for macOS and Linux
        os.system('clear')

def find_available_filename(base_name, max_number=99):
    """Finds an available filename with a numbered extension."""
    for number in range(max_number + 1):
        new_name = f"{base_name}_{number:02d}.txt"
        if not os.path.exists(new_name):
            return new_name
    return None

def validate_input(prompt, default, min_value=None, max_value=None):
    """Validates user input for integer values with optional min and max limits."""
    while True:
        try:
            user_input = input(prompt) or default
            value = int(user_input)
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                raise ValueError
            return value
        except ValueError:
            print("Ungültige Eingabe. Bitte erneut versuchen.")

def process_file(source_file_path, output_file_path, prefix, min_length, max_length):
    """Processes the file for password extraction."""
    processed_passwords = set()

    with open(source_file_path, 'r') as source_file:
        for line in source_file:
            if prefix in line:
                password = line.split(prefix)[-1].strip()
                if min_length <= len(password) <= max_length and not (password.startswith('{"') or password.startswith('[')):
                    processed_passwords.add(password)

    with open(output_file_path, 'w') as output_file:
        for password in processed_passwords:
            output_file.write(password + "\n")
    return len(processed_passwords)

def main():
    clear_screen()
    print("GreyKey Password Cleaner [GPC] v0.1")
    print("========================================\n")

    prefix = input("Präfix für Zeilenfilter (Standard: 'Item value:'): ") or "Item value:"
    min_length = validate_input("Minimale Länge der Passwörter (Standard: 4): ", "4", min_value=1)
    max_length = validate_input("Maximale Länge der Passwörter (Standard: 64): ", "64", min_value=min_length)

    output_filename = find_available_filename("passwords_clean", max_number=99)
    if output_filename is None:
        print("Bitte unbenötigte Dateien löschen. Es gibt bereits 100 'passwords_clean_##.txt' Dateien.")
        return

    try:
        start_time = time.time()
        line_count = process_file("passwords.txt", output_filename, prefix, min_length, max_length)
        end_time = time.time()
        print(f"Passwörter wurden in '{output_filename}' gespeichert.")
        print(f"Anzahl der Zeilen in '{output_filename}': {line_count}")
        print(f"Verarbeitungszeit: {end_time - start_time:.2f} Sekunden.")
    except FileNotFoundError:
        print("Datei 'passwords.txt' wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    main()
