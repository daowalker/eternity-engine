from __future__ import annotations
import os
import requests
from typing import Optional
from .ports import AIBackend


class OllamaBackend(AIBackend):


    def __init__(
        self,
        *,
        base_url: str | None = None,
        model: str | None = None,
        timeout: int = 120,
    ):
        self.base_url = (base_url or os.getenv("OLLAMA_URL", "http://localhost:11434")).rstrip("/")
        self.model = model or os.getenv("OLLAMA_MODEL", "qwen3:8b")
        self.timeout = timeout

    def generate(
        self,
        prompt: str,
        *,
        system: str = "",
        context: Optional[str] = None,
        temperature: float = 0.7,
    ) -> str:
        full_prompt = f"{system}\n\n{context or ''}\n\n{prompt}".strip()

        payload = {
            "model": self.model,
            "prompt": full_prompt,
            "options": {"temperature": temperature},
            "stream": False,
        }

        resp = requests.post(
            f"{self.base_url}/api/generate",
            json=payload,
            timeout=self.timeout,
        )
        resp.raise_for_status()

        response_text = ""
        for line in resp.iter_lines():
            if not line:
                continue
            try:
                obj = line.decode("utf-8")
                if obj.startswith("{") and '"response":' in obj:
                    import json
                    chunk = json.loads(obj)
                    response_text += chunk.get("response", "")
            except Exception:
                continue

        return response_text.strip()
