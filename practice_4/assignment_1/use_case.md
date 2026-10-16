# Practice 4 — Assignment 1: Your function, in English and in Python

## Use Case 1: Retrieve a specific fact

Input: A user's question asking for a specific fact, value, requirement, definition, or assumption.
Output: An English answer with relevant conditions, source references, limitations, and a verification reminder, or an explicit message that no reliable answer was found.
Process: Search a local collection of fictional documents by keyword, send matching excerpts to an AI API, and extract and return the answer using only that evidence.

## Python implementation

- `answer_fact.py`: contains the main function `answer_fact(question)` and a local retrieval helper, `retrieve(question)`.
- `fictional_documents.json`: fictional source records used instead of a retrieval API.
- `requirements.txt`: required Python packages.
- `.env.example`: placeholder for the API key; copy to `.env` and add your key locally. Never submit the real key.

The program runs locally in the terminal and has no web interface. It sends retrieved fictional excerpts to the OpenAI API for answer generation. The local keyword search is a teaching placeholder, not a full document retrieval system.

## Run locally

Open a terminal in this folder, then run:

```powershell
python -m pip install -r requirements.txt
Copy-Item .env.example .env
# Add your OpenAI API key to .env before continuing.
python answer_fact.py
```

If `.env` already exists, use it instead of copying over it.

Example question: What is the difference between cumulative noise and combined noise?

## Validation

Python syntax and local retrieval checks passed for noise, ventilation, and an unrelated question with no match. The live AI API call has not been tested.
