# Miro API Configurations
ACCESS_TOKEN = "eyJtaXJvLm9yaWdpbiI6ImV1MDEifQ_nWyxOkXLlhPIg-WIxIK7DkA67tw"
BOARD_ID = "create a new board"  

# Miro API Endpoints
BASE_URL = "https://api.miro.com/v1"

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def create_board():
    url = f"{BASE_URL}/boards"
    payload = {
        "name": "Gesturalism Conceptual Framework"
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    return response.json().get("id")

def create_sticky_note(board_id, text, x, y, color="light_blue"):
    url = f"{BASE_URL}/boards/{board_id}/widgets"
    payload = {
        "type": "sticky_note",
        "data": {"content": text},
        "position": {"x": x, "y": y},
        "style": {"fillColor": color}
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    return response.json().get("id")

# Function to create a connection (line between nodes)
def create_line(board_id, start_id, end_id):
    url = f"{BASE_URL}/boards/{board_id}/widgets"
    payload = {
        "type": "line",
        "startWidget": {"id": start_id},
        "endWidget": {"id": end_id},
        "style": {"lineColor": "black"}
    }
    requests.post(url, headers=HEADERS, json=payload)

# Main Execution
def main():
    global BOARD_ID
    if not BOARD_ID:
        BOARD_ID = create_board()
        print(f"Created new board: {BOARD_ID}")

    time.sleep(2)  # Allow Miro to process board creation

    # Positioning Variables (For Layout)
    x_start, y_start = 0, 0
    x_step, y_step = 400, 250

    # Define Nodes
    nodes = {
        "Language": {"x": x_start, "y": y_start, "color": "red"},
        "Mysticism": {"x": x_start + x_step, "y": y_start, "color": "yellow"},
        "Subjectivity": {"x": x_start + (x_step * 2), "y": y_start, "color": "green"},
        "Deconstruction (Derrida)": {"x": x_start, "y": y_start - y_step},
        "Semiotics (Barthes, Eco)": {"x": x_start, "y": y_start - (2 * y_step)},
        "Interpretation (Eco)": {"x": x_start, "y": y_start - (3 * y_step)},
        "Signs and Symbols": {"x": x_start, "y": y_start - (4 * y_step)},
        "The Oulipo (Playful Constraints)": {"x": x_start, "y": y_start - (5 * y_step)},
        "The Sublime": {"x": x_start + x_step, "y": y_start - y_step},
        "Transcendence": {"x": x_start + x_step, "y": y_start - (2 * y_step)},
        "Phenomenology (Merleau-Ponty)": {"x": x_start + x_step, "y": y_start - (3 * y_step)},
        "Faith and Awe (Critchley)": {"x": x_start + x_step, "y": y_start - (4 * y_step)},
        "Artistic Transcendence (Kandinsky, Blake)": {"x": x_start + x_step, "y": y_start - (5 * y_step)},
        "Form and Function": {"x": x_start + x_step, "y": y_start - (6 * y_step)},
        "Fragmentation (Levinas)": {"x": x_start + (2 * x_step), "y": y_start - y_step},
        "Temporality and Relativity (Badiou)": {"x": x_start + (2 * x_step), "y": y_start - (2 * y_step)},
        "Liminality": {"x": x_start + (2 * x_step), "y": y_start - (3 * y_step)},
        "Absence": {"x": x_start + (2 * x_step), "y": y_start - (4 * y_step)},
        "Labyrinths (Borges)": {"x": x_start + (2 * x_step), "y": y_start - (5 * y_step)},
        "The Situationists (Sociopolitical Art)": {"x": x_start + (2 * x_step), "y": y_start - (6 * y_step)},
        "Art vs. Entertainment": {"x": x_start + (x_step // 2), "y": y_start - (7 * y_step)},
        "Necessity of the Arts": {"x": x_start + (x_step // 2), "y": y_start - (8 * y_step)}
    }

    widget_ids = {}

    # Create Nodes (Sticky Notes)
    for name, data in nodes.items():
        widget_ids[name] = create_sticky_note(BOARD_ID, name, data["x"], data["y"], color=data.get("color", "light_blue"))
        time.sleep(0.5)  # Prevent API rate limits

    # Define Connections
    connections = [
        ("Language", "Deconstruction (Derrida)"),
        ("Language", "Semiotics (Barthes, Eco)"),
        ("Language", "Interpretation (Eco)"),
        ("Language", "Signs and Symbols"),
        ("Language", "The Oulipo (Playful Constraints)"),
        ("Mysticism", "The Sublime"),
        ("Mysticism", "Transcendence"),
        ("Mysticism", "Phenomenology (Merleau-Ponty)"),
        ("Mysticism", "Faith and Awe (Critchley)"),
        ("Mysticism", "Artistic Transcendence (Kandinsky, Blake)"),
        ("Mysticism", "Form and Function"),
        ("Subjectivity", "Fragmentation (Levinas)"),
        ("Subjectivity", "Temporality and Relativity (Badiou)"),
        ("Subjectivity", "Liminality"),
        ("Subjectivity", "Absence"),
        ("Subjectivity", "Labyrinths (Borges)"),
        ("Subjectivity", "The Situationists (Sociopolitical Art)"),
        ("Mysticism", "Art vs. Entertainment"),
        ("Subjectivity", "Art vs. Entertainment"),
        ("Language", "Necessity of the Arts"),
        ("Mysticism", "Necessity of the Arts"),
        ("Subjectivity", "Necessity of the Arts")
    ]

    # Create Connections
    for start, end in connections:
        create_line(BOARD_ID, widget_ids[start], widget_ids[end])
        time.sleep(0.5)  # Prevent API rate limits

    print("Miro board updated successfully!")

if __name__ == "__main__":
    main()
