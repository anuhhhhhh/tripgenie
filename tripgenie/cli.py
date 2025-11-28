from .ai import generate_ai_itinerary
import json
import typer
from pathlib import Path
from importlib import resources

def load_destinations():
    """
    Load destinations.json from the installed tripgenie package.
    Works both in development and when installed via pip.
    """
    with resources.files("tripgenie").joinpath("data/destinations.json").open("r", encoding="utf-8") as f:
        return json.load(f)


def recommend_destination(budget, days, style):
    dests = load_destinations()
    candidates = []

    for d in dests:
        if style not in d["vibes"]:
            continue

        est_cost = d["approx_flight_cost"] + days * d["stay_cost_per_night"]

        if est_cost <= budget:
            candidates.append((d, est_cost))

    if not candidates:
        return None

    # Choose the cheapest viable option
    candidates.sort(key=lambda x: x[1])
    return candidates[0][0]
def find_destination_by_name(name: str):
    """
    Try to find a destination in our JSON by its name (case-insensitive).
    Returns the destination dict if found, otherwise None.
    """
    dests = load_destinations()
    target = name.strip().lower()

    for d in dests:
        if d["name"].strip().lower() == target:
            return d

    return None

def print_simple_itinerary(destination, origin, style):
    typer.echo(f"Day 1: Travel from {origin} to {destination['name']}, explore, settle in.")
    typer.echo(f"Day 2: {style.capitalize()}-style activities and local highlights.")
    typer.echo("Day 3: Sightseeing + relaxation.")
    typer.echo("Day 4+: Explore, chill, and prepare to depart.")


def main():
    typer.echo("✈️  Welcome to TripGenie — budget trip planner.\n")

    budget = typer.prompt("Total budget (USD)", type=float)
    days = typer.prompt("Number of days", type=int)
    style = typer.prompt("Trip style (chill/adventure/party/romantic/solo)", default="chill")
    origin = typer.prompt("Departure city", default="Los Angeles")

    style = style.lower().strip()

    # Let user choose between auto-recommendation and manual destination
    auto_pick = typer.confirm(
        "\nDo you want TripGenie to recommend a destination based on your budget and style?",
        default=True,
    )

    if auto_pick:
        destination = recommend_destination(budget, days, style)

        if not destination:
            typer.echo("\n❌ No destinations matched your budget/style.")
            # fall back to manual choice
            manual_name = typer.prompt("Where do you want to go? (any city/country)")
            destination = find_destination_by_name(manual_name) or {
                "name": manual_name,
                "activities": [],
            }
    else:
        manual_name = typer.prompt("Where do you want to go? (any city/country)")
        destination = find_destination_by_name(manual_name) or {
            "name": manual_name,
            "activities": [],
        }

    typer.echo(f"\n🌍 Destination: **{destination['name']}**")


    flight_budget = budget * 0.4
    stay_budget = budget * 0.3
    food_budget = budget * 0.2
    activities_budget = budget * 0.1

    # Ask if user wants an AI-generated itinerary
    use_ai = typer.confirm("\n🤖 Do you want an AI-generated detailed itinerary?", default=True)

    typer.echo("\n=== Itinerary ===")

    if use_ai:
        try:
            ai_text = generate_ai_itinerary(
                destination=destination["name"],
                origin=origin,
                days=days,
                style=style,
                budget=budget,
                activities=destination.get("activities", []),
            )
            typer.echo(ai_text)
        except Exception as e:
            typer.echo(f"\n⚠️ AI itinerary failed: {e}")
            typer.echo("\nFalling back to simple template:\n")
            print_simple_itinerary(destination, origin, style)
    else:
        print_simple_itinerary(destination, origin, style)



if __name__ == "__main__":
    typer.run(main)
