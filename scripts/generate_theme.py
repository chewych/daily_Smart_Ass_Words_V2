import os
import json
import datetime
import time
from google import genai
from google.genai import types

EPOCH_DATE = datetime.datetime(2026, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
NOW = datetime.datetime.now(datetime.timezone.utc)
ELAPSED_DAYS = max(0, (NOW - EPOCH_DATE).days)
CYCLE_INDEX = ELAPSED_DAYS % 300

def get_coprime_permutation_index(day_num, pool_size=300):
    # gcd(137, 300) = 1 guarantees a full 300-day cycle without repeats
    return (day_num * 137 + 43) % pool_size

# Load the curriculum data
with open("data/curriculum.json", "r", encoding="utf-8") as f:
    curriculum = json.load(f)

p_idx = get_coprime_permutation_index(CYCLE_INDEX, 300)
today_phrase = curriculum["phrases"][p_idx]
today_french = curriculum["french"][p_idx]
today_yiddish = curriculum["yiddish"][p_idx]
today_latin = curriculum["latin"][p_idx]

prompt = f"""
Analyze the philosophical and psychological intersection of these four daily vocabulary items:
1. Latin Dictum: "{today_phrase['w']}" ({today_phrase['eng']})
2. French Lexicon: "{today_french['w']}" ({today_french['eng']})
3. Yiddish Lexicon: "{today_yiddish['w']}" ({today_yiddish['eng']})
4. Latin Root: "{today_latin['w']}" ({today_latin['eng']})

Task:
1. Synthesize an overarching philosophical, existential, or psychological theme connecting all four terms (2 sentences max).
2. Select the single most resonant quote that embodies this dynamic, chosen strictly from: Marcus Aurelius, Jim Morrison, Sigmund Freud, Carl Jung, Lord Byron, Jacques Lacan, or Friedrich Nietzsche.
3. Write a concise 1-sentence note linking the chosen quote back to the tension between the four daily words.

Respond strictly in valid JSON matching this schema:
{{
  "themeTitle": "Short Theme Title (3-5 words)",
  "thematicAnalysis": "Two sentence conceptual synthesis.",
  "quote": "Exact quotation.",
  "author": "Author Name",
  "work": "Book, Essay, or Speech Title",
  "synthesisNote": "One sentence linking the quote back to the daily words."
}}
"""

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = None
max_retries = 4

for attempt in range(max_retries):
    try:
        print(f"Calling Gemini API (attempt {attempt + 1} of {max_retries})...")
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.3
            )
        )
        print("Successfully received synthesis from Gemini.")
        break
    except Exception as e:
        print(f"Attempt {attempt + 1} encountered error: {e}")
        if attempt < max_retries - 1:
            wait_seconds = (attempt + 1) * 8
            print(f"Waiting {wait_seconds} seconds before retrying...")
            time.sleep(wait_seconds)
        else:
            print("Transient capacity issue persists. Preserving baseline theme so curriculum deployment completes.")

if response and response.text:
    try:
        output_data = json.loads(response.text)
        output_data["date"] = NOW.strftime("%Y-%m-%d")
        output_data["dayNumber"] = CYCLE_INDEX + 1
        output_data["cycleIndex"] = CYCLE_INDEX
        output_data["terms"] = [today_phrase['w'], today_french['w'], today_yiddish['w'], today_latin['w']]

        with open("data/daily_theme.json", "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print(f"Updated data/daily_theme.json with theme: {output_data.get('themeTitle')}")
    except Exception as parse_err:
        print(f"Could not parse Gemini JSON response: {parse_err}. Keeping baseline theme.")
else:
    print("Continuing with existing baseline theme for today.")
