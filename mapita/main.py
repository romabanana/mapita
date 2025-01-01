import typer

from map import map

from rich.console import Console
from rich.text import Text


# Create a Typer app instance
app = typer.Typer()

# Create a Rich Console instance for pretty output
console = Console()

# Create dictionary with the colors of the cells
case_dispatcher = {
    -2: "on #3198c4",  # Deep Sea
    -1: "on #43dedb",  # Sea
    0: "on #dceb6a",  # Shore (Sand)
    1: "on #51c43f",  # Plain
    2: "on #3f8f32",  # Higher Plain
    3: "on #3c523e",  # Mountain
    4: "on #DDDDDD",  # Snow or other
    10: "on #bbaa3a",
    11: "on #fcfb5a"
}


# Prints in console
def display_ascii_map(matrix):
    # Loop through each row in the matrix
    for row in matrix:
        output_row = Text()
        for char in row:
            style = case_dispatcher.get(int(char), "on #3f8f32")
            output_row.append(Text(" ", style=style))

        # Print the row after joining the parts
        console.print(output_row)


# Main
@app.command()
def main(width=25, height=50, rivers=3, debug: bool = False):
    print(height)
    ascii_map = map(int(width), int(height), int(rivers), bool(debug))
    display_ascii_map(ascii_map)


if __name__ == "__main__":
    app()
