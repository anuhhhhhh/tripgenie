# ✈️ TripGenie — AI Travel Planner (CLI)

TripGenie is an interactive **AI-powered travel planner** that builds complete trip itineraries from the command line.  
TripGenie is an officially published **PyPI package** that lets you generate full travel itineraries directly from your terminal.
Enter your budget, trip length, style, and destination — or let TripGenie recommend a location — and optionally generate a multi-day itinerary using OpenAI.

Install globally with:
```bash
pip install tripgenie
```

Run from anywhere:
```bash
tripgenie
```
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

### 🔑 API Requirements

TripGenie uses OpenAI for generating AI itineraries.

Set your API key:
```bash
export OPENAI_API_KEY="your_api_key"
```
Or create a .env file with:
```bash
OPENAI_API_KEY=your_api_key
```

### ▶️ Running TripGenie

Start the CLI:

```bash
tripgenie
```

You’ll be prompted for:

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
│   ├── cli.py              # Main CLI logic
│   ├── ai.py               # OpenAI itinerary generator
│   ├── data/
│   │   └── destinations.json
│   └── __init__.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

## 🛠 Future Enhancements

### 🎨 Phase 1 — Streamlit Web App (Coming Soon)
- Beautiful browser UI
- Form inputs for budget, destination, dates
- Display itinerary in interactive format
- Shareable itinerary pages

### 🌐 Phase 2 — Backend API
- Allow users to use TripGenie without needing their own OpenAI key
- Rate-limited free tier
- Paid tier for long itineraries

### 🌍 Phase 3 — Enhanced Intelligence
- Add 50+ curated destinations
- Live currency conversion
- Flight price API integration
- Safety scores & seasonal weather insights
- “Surprise me” random trip generator

### 💼 Phase 4 — Packaging Enhancements
- Publish tripgenie as a pip-installable Streamlit app
- One-command desktop launcher

## 👤 Author

Created by Anush Harish
Built with Python, Typer, and OpenAI.
Published on PyPI as an open-source travel toolkit for developers and travelers.
