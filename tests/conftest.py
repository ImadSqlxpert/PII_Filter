# tests/conftest.py
import pytest

def normalize_placeholders(text: str) -> str:
    """Map &lt;TAG&gt; -> <TAG> and &gt;/&lt; sequences so tests don't care about HTML-entities vs raw."""
    if not isinstance(text, str):
        return text
    return text.replace("&lt;", "<").replace("&gt;", ">")

@pytest.fixture
def norm():
    return normalize_placeholders

def has_tag(text: str, tag: str) -> bool:
    return f"<{tag}>" in normalize_placeholders(text)

def count_tag(text: str, tag: str) -> int:
    return normalize_placeholders(text).count(f"<{tag}>")