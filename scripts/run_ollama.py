from core.config import LLMConfig
from llm.ollama_llm import OllamaLLM

config = LLMConfig(
    provider="ollama",
    base_url="http://localhost:11434",
    model_name="qwen2.5:3b",
    temperature=0.1,
    timeout=120
    )

llm = OllamaLLM(config)

response = llm.generate(
    [
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ]
)

print(response)