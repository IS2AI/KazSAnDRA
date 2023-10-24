from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
from transformers import TextClassificationPipeline

output_dir = "models/2023.10.24_14.16.47_bert-base-multilingual-uncased_pc_rus"

model = AutoModelForSequenceClassification.from_pretrained(f"{output_dir}/model")
tokenizer = AutoTokenizer.from_pretrained(f"{output_dir}/model")

pipe = TextClassificationPipeline(model = model, tokenizer = tokenizer)

reviews = ["Бұл бейнефильм маған түк ұнамады.", "Осы кітап қызық сияқты."]

for review in reviews:
    print(pipe(review))