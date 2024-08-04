from transformers import GPT2LMHeadModel, GPT2Tokenizer

# A function to load the model 

def load_model(model_path):
    model = GPT2LMHeadModel.from_pretrained(model_path)
    tokenizer = GPT2Tokenizer.from_pretrained(model_path)
    return model, tokenizer

