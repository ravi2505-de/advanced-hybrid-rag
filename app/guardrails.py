import re

BLOCKED_PATTERNS = [
    r"ignore previous instructions",
    r"system prompt",
    r"act as",
    r"bypass",
]

def validate_query(query: str):
    query = query.lower()
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, query):
            raise ValueError("Query blocked by guardrail policy.")
    return True