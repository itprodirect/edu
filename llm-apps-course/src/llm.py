import os
from openai import OpenAI

client = OpenAI()

def respond(text: str, model: str | None = None, **kwargs) -> str:
    model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    r = client.responses.create(
        model=model,
        input=text,
        **kwargs,  # e.g., max_output_tokens=300
    )
    return r.output_text
