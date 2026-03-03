from transformers import AutoTokenizer, AutoModelForCausalLM
from util.prompt import getPrompt, getAccidentPrompt
import torch
import threading

# inflation 전용
inflation_tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
inflation_model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
_inflation_lock = threading.Lock()

# accident 전용
accident_tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
accident_model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
_accident_lock = threading.Lock()

import re

@torch.inference_mode()
def sync_inflation(region: str, title: str):
    PROMPT = getPrompt(region, title)
    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": title},
    ]
    with _inflation_lock:
        inputs = inflation_tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        ).to(inflation_model.device)
        outputs = inflation_model.generate(**inputs, max_new_tokens=6, do_sample=False)
    text = inflation_tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
    gen_text = re.search(r"[-+]?\d+(\.\d+)?", text)
    return gen_text.group() if gen_text else "0.0"

@torch.inference_mode()
def accident_valuation(region: str, title: str):
    PROMPT = getAccidentPrompt(region, title)
    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": title},
    ]
    with _accident_lock:
        inputs = accident_tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        ).to(accident_model.device)
        outputs = accident_model.generate(**inputs, max_new_tokens=6, do_sample=False)
    text = accident_tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
    gen_text = re.search(r"[-+]?\d+(\.\d+)?", text)
    return gen_text.group() if gen_text else "0.0"