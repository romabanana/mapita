import typer
from map import generate_random_map
from rich.console import Console
from rich.table import Table
from rich.text import Text

# Create a Typer app instance
app = typer.Typer()

# Create a Rich Console instance for pretty output
console = Console()


def display_ascii_map(matrix):
    # Loop through each row in the matrix and print it with advanced styling
    empty = " "
    for row in matrix:
        output_row = Text();
        for char in row:
            if char == 1:
                output_row.append_text(Text(empty, style="on green"))  
            elif char == 0:
                output_row.append_text(Text(empty, style="on blue"))
            else:
                output_row.append_text(empty)       
        # Print the row after joining the parts
        console.print(output_row)       


# Example ASCII map as a 1D list


ascii_map = generate_random_map(40,20) 


@app.command()
def map():
    display_ascii_map(ascii_map)

@app.command()
def greet(name: str):
    """A simple greeting command"""
    console.print(f"[bold green]Hello,{name}[/bold green]!", style="bold cyan")


@app.command()
def show_table():
    """Display a table with rich formatting"""
    table = Table(title="Rich Table Example")

    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta")
    table.add_column("Role", style="yellow")

    table.add_row("1", "Alice", "Developer")
    table.add_row("2", "Bob", "Designer")
    table.add_row("3", "Charlie", "Manager")

    console.print(table)


if __name__ == "__main__":
    app()
