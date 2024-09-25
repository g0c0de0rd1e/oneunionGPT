import time
import re
import logging
from transformers import GPT2LMHeadModel, GPT2Tokenizer

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def generate_marketing_text(product_description):
    try:
        model_name = "sberbank-ai/rugpt3medium_based_on_gpt2"
        local_model_path = "./models/rugpt3medium_based_on_gpt2"
        prompt = (
            f"Напишите маркетинговое описание для продукта '{product_description}'. "
            f"Акцентируйтесь на его ключевых преимуществах и способности удовлетворить потребности целевой аудитории. "
            f"Используйте конкретные детали и примеры, демонстрирующие, как этот продукт может улучшить жизнь или бизнес пользователя.\n\n"
            f"Не используйте ссылки и названия других компаний."
            f"Описание: "
        )

        tokenizer = GPT2Tokenizer.from_pretrained(model_name, cache_dir=local_model_path)
        model = GPT2LMHeadModel.from_pretrained(model_name, cache_dir=local_model_path)
        inputs = tokenizer.encode(prompt, return_tensors="pt")

        max_generation_length = 500
        output = inputs
        generated_text = ""

        start_time = time.time()

        outputs = model.generate(
            input_ids=output,
            max_new_tokens=max_generation_length,
            do_sample=True,
            temperature=0.6,
            no_repeat_ngram_size=3,
            repetition_penalty=2.,
            num_return_sequences=1,
            return_dict_in_generate=True,
            output_scores=True,
        )

        generated_text = tokenizer.decode(outputs.sequences[0], skip_special_tokens=True)
        generated_text = re.sub(r'http\S+|www\S+|[^а-яА-ЯёЁa-zA-Z0-9\s.,!?]', '', generated_text)

        sentences = re.split(r'(?<=[.!?]) +', generated_text)
        unique_sentences = []

        for sentence in sentences:
            if sentence.strip() not in unique_sentences:
                unique_sentences.append(sentence.strip())

        final_text = ' '.join(unique_sentences)

        # Удаляем ссылки
        final_text = re.sub(r'http\S+', '', final_text)

        end_time = time.time()
        generation_time = end_time - start_time

        logging.info(f"\nВремя генерации: {generation_time:.2f} секунд")
        return final_text
    except Exception as e:
        logging.error(f"Ошибка при генерации текста: {e}")
        raise
