from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "distilbert-base-uncased"
save_path = "./app/model"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=4)

tokenizer.save_pretrained(save_path)
model.save_pretrained(save_path)

print("✅ Model and tokenizer saved to", save_path)
