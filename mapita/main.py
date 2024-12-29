import typer

import map as mp


from rich.console import Console
from rich.table import Table
from rich.text import Text

# Create a Typer app instance
app = typer.Typer()

# Create a Rich Console instance for pretty output
console = Console()


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


def display_ascii_map(matrix):
    # Loop through each row in the matrix
    for row in matrix:
        output_row = Text()
        for char in row:
            style = case_dispatcher.get(int(char), "on #3f8f32")
            output_row.append(Text(" ", style=style))

        # Print the row after joining the parts
        console.print(output_row)


@app.command()
def map(width = None, height = None, rivers = None, debug = None):
    if(width == height == rivers == debug):
        ascii_map = mp.map()
    else:        
        ascii_map = mp.map(int(width), int(height), int(rivers), bool(debug))
    display_ascii_map(ascii_map)

# old stuff


@app.command()
def greet(name: str):
    """A simple greeting command"""
    console.print(f"[bold green]Hello,{name}[/bold green]!", style="bold cyan")


@app.command()
def show_table():
    """Display a table with rich formatting"""
    table = Table(title="Rich Table Example")

    table.add_column("ID", justify="right", style="cyan on red", no_wrap=True)
    table.add_column("Name", style="magenta")
    table.add_column("Role", style="yellow")

    table.add_row("1", "Alice", "Developer")
    table.add_row("2", "Bob", "Designer")
    table.add_row("3", "Charlie", "Manager")

    console.print(table)


if __name__ == "__main__":
    app()
