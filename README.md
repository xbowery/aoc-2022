# Advent of Code 2022
Repository containing my solutions to Advent of Code 2022

You may find my solutions to the various days by clicking into the respective subdirectories. I will attempt to solve the challenges using Python and Java (will try out other languages if time permits.)

## Input File Generator
In the `input_generator` directory, I created [`generate_input.py`](https://github.com/xbowery/aoc-2022/blob/main/input_generator/generate_input.py) that would allow for easy extraction of the inputs required into a text file.

To use the file, create a `.env` file by following the format of the .env.sample file provided.

The cookie can be extracted through the following steps:
When you are logged into the Advent of Code platform > Inspect the platform's webpage > Extract the cookie under the "Application" tab and "Storage" section > Copy the cookie's value and replace the placeholder value in the `.env` file.

Run the following commands:
```bash
pip install -r requirements.txt

python generate_input.py
```

When the file is run, the application will correspondingly ask you to enter which day of Advent Of Code to generate the input file.
