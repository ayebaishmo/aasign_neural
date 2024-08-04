from model_init import load_model
model, tokenizer = load_model("C:/Users/ISHMO_CT/Downloads/Bloomtech/aasign_neural/distilgpt2")


class StoryBot:
    # constructor "automatically called when the class object is created"
    def __init__(self, model, tokenizer, max_lenght=1000):
        self.model = model
        self.tokenizer = tokenizer
        self.max_length = max_lenght
    
    def __call__(self, user_prompt: str) -> str:
        # The __call__ is pecial method taht allows an instance of the 
        # class to called as if it were a function
        input_ids = self.tokenizer.encode(user_prompt, return_tensors="pt")

        output = self.model.generate(
            input_ids,
            max_length=self.max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            early_stopping=True,
            temperature = 0.7,
            top_k=50,
            top_p=0.95
        )

        # decode the generated story 
        story = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return story
    
    # save the stories in text file
    def save_story(self, story: str, filename: str):
        with open(filename, 'a') as file:
            file.write(story + '\n\n')
    
# Initializer  the storybot 
StoryBot1 = StoryBot(model, tokenizer)

# # Generate the story based on user prompt 
# user_prompt = "Ishmael the great man,"
# story = StoryBot1(user_prompt)
# print(story)

    

