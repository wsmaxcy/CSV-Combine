# CSV Combine

![App Screenshot](https://willmaxcy.com/assets/imgs/CSV-Combine.png)

CSV Combine is a Python program that allows you to combine two CSV files based on a common row name. It provides a simple graphical user interface (GUI) using CustomTkinter to select the CSV files, specify the common row name, and combine the data into a new CSV file.

## Features

- Import and view the content of two CSV files.
- Specify a common row name to match the rows from both CSV files.
- Combine the data from the two CSV files based on the common row name.
- Remove duplicate columns in the combined CSV file.
- Save the combined data to a new CSV file.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- customtkinter package
- CTkMessagebox package

You can install the required packages by running the following command:

```Bash
pip install customtkinter CTkMessagebox
```

or...

```Bash
pip install -r requirements.txt
```

## Usage

1. Run the `combine.py` file to launch the program.
2. Click on "Add CSV 1" to select the first CSV file.
3. Click on "Add CSV 2" to select the second CSV file.
4. Enter a common row name in the provided input field.
5. Click on "Combine CSVs" to combine the CSV files based on the common row name.
6. Choose a location to save the combined CSV file.
7. The combined CSV file will be saved with the selected name and location.

## Contributing

Contributions to CSV Combine are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This program is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).
