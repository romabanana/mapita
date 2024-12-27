import typer
from map import generate_random_map
from rich.console import Console
from rich.table import Table
from rich.text import Text

# Create a Typer app instance
app = typer.Typer()

# Create a Rich Console instance for pretty output
console = Console()

 


def layer1():
    return Text(" ", style="on blue")

def layer2():
    return Text(" ", style="on cyan")

def layer3():
    return Text(" ", style="on bright_yellow")

def layer4():
    return Text(" ", style="on green")

def layer5():
    return Text(" ", style="on dark_green")


# Case dictionary


case_dispatcher = {
    -2: layer1,
    -1: layer2,
    0: layer3,
    1: layer4,
    2: layer5
}



def display_ascii_map(matrix):
    # Loop through each row in the matrix and print it with advanced styling
   for row in matrix:
        output_row = Text();
        for char in row:
           output_row.append_text(case_dispatcher.get(char,layer5)())

        # Print the row after joining the parts
        console.print(output_row)       


ascii_map = generate_random_map(100,40) 


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
