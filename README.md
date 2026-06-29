# GenPark Search Autocomplete & Intent Expansion Skill

This repository contains the **GenPark Search Autocomplete & Intent Expansion Skill** — an agent configuration skill config (`skill.json`), a production-ready Python SDK client (`suggest_agent.py`), and executable verification tests. It is designed to generate search autocomplete suggestions matching prefix constraints and map keywords to expanded synonym arrays.

---

## 🚀 Capabilities

* **Keyword Prefix Match:** Searches mock indexes to return list completions.
* **Semantic Expansion:** Maps core words (like "headphones", "wireless") to rich synonym arrays to maximize search yield.
* **Limit Boundaries:** Automatically respects constraints to prevent payload bloating.

---

## 🛠️ Setup & Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 SDK Usage Reference

```python
from suggest_agent import SearchSuggestClient

client = SearchSuggestClient()

result = client.get_suggestions("speaker", limit=3)
print(result["suggestions"])
print(result["query_expansion"]["expanded_terms"])
```

---

## 📜 License
This project is licensed under the MIT License.
