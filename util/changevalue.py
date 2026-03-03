from transformers import AutoTokenizer, AutoModelForCausalLM
from util.prompt import getPrompt, getAccidentPrompt
import torch
import threading
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# inflation 전용
inflation_tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
inflation_model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
_inflation_lock = threading.Lock()
logger.debug("inflation 모델생성완")

# accident 전용
accident_tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
accident_model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
_accident_lock = threading.Lock()
logger.debug("accident 모델생성완")
import re

@torch.inference_mode()
def sync_inflation(region: str, title: str):
    PROMPT = getPrompt(region, title)
    logger.debug("프롬프트 불러오기 완")
    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": title},
    ]
    
    with _inflation_lock:
        logger.debug("인풋 전")
        inputs = inflation_tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        ).to(inflation_model.device)
        logger.debug("인풋 후 및 아웃풋 전")
        outputs = inflation_model.generate(**inputs, max_new_tokens=6, do_sample=False)
        logger.debug("아웃풋 완")
    text = inflation_tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
    logger.debug("후처리 전")
    gen_text = re.search(r"[-+]?\d+(\.\d+)?", text)
    logger.debug("후처리 후")
    return gen_text.group() if gen_text else "0.0"

@torch.inference_mode()
def accident_valuation(region: str, title: str):
    PROMPT = getAccidentPrompt(region, title)
    logger.debug("프롬프트 불러오기 완")
    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": title},
    ]
    with _accident_lock:
        logger.debug("인풋 전")
        inputs = inflation_tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        ).to(inflation_model.device)
        logger.debug("인풋 후 및 아웃풋 전")
        outputs = inflation_model.generate(**inputs, max_new_tokens=6, do_sample=False)
        logger.debug("아웃풋 완")
    text = inflation_tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
    logger.debug("후처리 전")
    gen_text = re.search(r"[-+]?\d+(\.\d+)?", text)
    logger.debug("후처리 후")
    return gen_text.group() if gen_text else "0.0"
