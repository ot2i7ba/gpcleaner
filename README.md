# gpcleaner
A small Python script that cleans a password list generated by Magnet GreyKey based on user input. The script reads a text file (passwords.txt) and writes filtered values to an output file. Filtering is based on a prefix (item value), a minimum password length (default 4) and a maximum password length (default 64). After cleaning up the prefix, the system checks whether a line begins with {" or [". These lines are also not included in the output file. Duplicate entries are also filtered. These filter properties are used to create a good list of possible passwords.

## License
This project is licensed under the **[MIT license](https://github.com/ot2i7ba/gpcleaner/blob/main/LICENSE)**, providing users with flexibility and freedom to use and modify the software according to their needs.

## Disclaimer
This project is provided without warranties. Users are advised to review the accompanying license for more information on the terms of use and limitations of liability.
