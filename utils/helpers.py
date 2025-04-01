import re

def clear_json_tags(text: str) -> str:
    text = re.sub(r'```json\s*([\s\S]*?)```', r'\1', text)
    text = re.sub(r'```{\s*([\s\S]*?)\s*}```', r'\1', text)
    return text.strip()
