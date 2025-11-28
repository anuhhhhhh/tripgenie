# ✈️ TripGenie — AI Travel Planner (CLI)

TripGenie is an interactive **AI-powered travel planner** that builds complete trip itineraries from the command line.  
Enter **any destination in the world**, get a budget breakdown, and optionally generate a **detailed multi-day itinerary** using OpenAI.

---

## 🚀 Features

### 🧭 Destination Selection  
Choose between:

- **Smart recommendation** (TripGenie analyzes your budget + trip style)  
- **Manual selection** (type any city or country: *Tokyo*, *Orlando, Florida*, *Paris*, *Goa*, etc.)  

---

### 💰 Budget Breakdown  
TripGenie automatically allocates your budget into:

- Flights  
- Stay  
- Food  
- Activities  

---

### 🤖 AI-Generated Itineraries  
If enabled, TripGenie uses OpenAI to create a detailed daily schedule including:

- Morning / afternoon / evening plans  
- Activity suggestions  
- Sightseeing  
- Food spots  
- Realistic pacing  

---

### 🌍 Expandable Destination Database  
Includes sample destinations such as:

- San Diego  
- Las Vegas  
- Hawaii  
- Costa Rica  

Each destination supports:

- Cost estimation  
- Trip vibes (chill, adventure, party, family, romantic)  
- Activity suggestions  

You can add unlimited destinations via `data/destinations.json`.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/anuhhhhhh/tripgenie.git
cd tripgenie
```

Create and activate your virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```


Install dependencies:

```bash
pip install -r requirements.txt
```

### 🔑 Environment Variables

TripGenie uses OpenAI for generating AI itineraries.

Create a .env file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

### ⚠️ Do NOT commit your .env file.
It is already included in .gitignore.

### ▶️ Running TripGenie

Start the CLI:

```bash
python -m tripgenie.cli
```

Follow the interactive prompts:

- Budget
- Number of days
- Trip style
- Departure city
- Auto-recommendation or manual destination
- AI itinerary (yes/no)

## 📁 Project Structure

```text
tripgenie/
├── tripgenie/
│   ├── cli.py          # Main CLI logic
│   ├── ai.py           # OpenAI itinerary generator
│   └── __init__.py
├── data/
│   └── destinations.json
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 🛠 Future Enhancements

- Streamlit UI
- Export itineraries to Markdown/PDF
- Larger destination database (+ continent packs)
- Advanced scoring system for recommendations
- “Surprise me” random destination mode
- Packing lists
- Local weather integration
- Flight cost API integration
- Publish as pip install tripgenie

## 👤 Author

Created by Anush Harish
Built with Python, Typer, and OpenAI.