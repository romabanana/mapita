import typer

from map import map

from rich.console import Console
from rich.text import Text

import json

# Create a Typer app instance
app = typer.Typer()

# Create a Rich Console instance for pretty output
console = Console()

# Load themes from JSON file
with open("themes.json", "r") as f:
    themes = json.load(f)

# Convert keys to integers (since JSON stores them as strings)
themes = {k: {int(key): value for key, value in v.items()} for k, v in themes.items()}

# Theme Selection

def select_theme(theme_name):
    return themes.get(theme_name, themes["earth"]) 

# Prints in console
def display_ascii_map(matrix, selected_theme):
    # Loop through each row in the matrix
    for row in matrix:
        output_row = Text()
        for char in row:
            style = selected_theme.get(int(char), "on #3f8f32")
            output_row.append(Text(" ", style=style))

        # Print the row after joining the parts
        console.print(output_row)


# Main
@app.command()
def main(width=25, height=50, rivers=3, theme="earth", debug: bool = False):
    ascii_map = map(int(width), int(height), int(rivers), bool(debug))
   
    selected_theme = select_theme(theme) 
    display_ascii_map(ascii_map, selected_theme)


if __name__ == "__main__":
    app()
