from transformers import AutoTokenizer, AutoModelForCausalLM
from util.prompt import getPrompt, getAccidentPrompt
import torch
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-3B-Instruct")

@torch.inference_mode()
def sync_inflation(region: str, title: str):
    PROMPT = getPrompt(region, title)
    print(title)
    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": title},
    ]
    
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    ).to(model.device)
    
    outputs = model.generate(**inputs, max_new_tokens=6,
                             do_sample = False)
    text = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
    
    import re
    gen_text = re.search(r"[-+]?\d+(\.\d+)?", text)
    return gen_text.group() if gen_text else "0.0"

@torch.inference_mode()
def accident_valuation(region: str, title: str):
    PROMPT = getAccidentPrompt(region, title)
    print(title)
    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": title},
    ]
    
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    ).to(model.device)
    
    outputs = model.generate(**inputs, max_new_tokens=6,
                             do_sample = False)
    text = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
    
    import re
    gen_text = re.search(r"[-+]?\d+(\.\d+)?", text)
    return gen_text.group() if gen_text else "0.0"
