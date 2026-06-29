import sys
import json
from suggest_agent import SearchSuggestClient

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    print("=== GenPark Search Autocomplete & Suggest Verification ===")
    client = SearchSuggestClient()

    # Prefix A
    prefix_a = "zeni"
    print(f"\n[Test A] Autocomplete Prefix: '{prefix_a}'")
    result_a = client.get_suggestions(prefix_a, limit=5)
    print(json.dumps(result_a, indent=2))

    # Prefix B
    prefix_b = "wireless speaker"
    print(f"\n[Test B] Autocomplete Prefix: '{prefix_b}'")
    result_b = client.get_suggestions(prefix_b, limit=5)
    print(json.dumps(result_b, indent=2))

if __name__ == "__main__":
    main()
