from adventure.utils import read_events_from_file
import random
from rich import print


default_message = "You stand still, unsure what to do. The forest swallows you."

def step(choice: str, events):
    """Decide the story's next step based on the player's choice."""
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[dim]You stand still, unsure what to do. The forest swallows you...[/dim]"


def left_path(event: str) -> str:
    """Narration for the left path."""
    return f"[green]You walk left.[/green] {event}"


def right_path(event: str) -> str:
    """Narration for the right path."""
    return f"[blue]You walk right.[/blue] {event}"


def main():
    """Main game loop."""
    events = read_events_from_file("events.txt")

    print("[bold bright_green]You wake up in a dark forest...[/bold bright_green]")
    print("[italic bright_black]You can go [green]left[/green] or [blue]right[/blue].[/italic bright_black]")

    while True:
        print("[bold]Which direction do you choose?[/bold] ([green]left[/green]/[blue]right[/blue]/[red]exit[/red]): ", end="")
        choice = input().strip().lower()
        if choice == "exit":
            print("[red]You decide to leave the forest before the darkness reaches you. Farewell, wanderer.[/red]")
            break

        print(step(choice, events))
        


if __name__ == "__main__":
    main()