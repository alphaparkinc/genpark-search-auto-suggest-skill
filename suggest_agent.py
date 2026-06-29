import os
from typing import List, Dict, Any, Optional

class SearchSuggestClient:
    """
    Production-grade query auto-suggest and semantic expansion client.
    Performs prefix dictionary filtering and maps synonyms to maximize matching indexes.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("SUGGEST_API_KEY")

    def get_suggestions(self, prefix: str, limit: int = 5) -> Dict[str, Any]:
        """
        Calculates suggestions matching the search prefix and returns expanded query terms.
        """
        prefix_clean = prefix.lower().strip()
        
        # Mock database of indexed search terms
        search_index = [
            "zenith speaker pro", "zenith wireless headphones", "zenith chargers",
            "bluetooth adapter zenith", "smart speaker assistant", "home hub device",
            "audio amplifiers", "accessories for zenith", "zenith specifications"
        ]

        # 1. Autocomplete match
        matches = []
        for term in search_index:
            if term.startswith(prefix_clean) or any(word.startswith(prefix_clean) for word in term.split()):
                matches.append(term)
                
        matches = list(set(matches))[:limit]

        # 2. Semantic query expansion rules
        synonym_map = {
            "speaker": ["audio", "sound system", "loudspeaker", "smart speaker"],
            "wireless": ["bluetooth", "cordless", "portable"],
            "headphones": ["earphones", "headset", "earbuds"]
        }

        expanded_terms = [prefix_clean]
        for word in prefix_clean.split():
            if word in synonym_map:
                expanded_terms.extend(synonym_map[word])

        return {
            "suggestions": matches,
            "query_expansion": {
                "original_query": prefix,
                "expanded_terms": list(set(expanded_terms))
            }
        }
