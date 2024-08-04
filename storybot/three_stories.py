from storybot import StoryBot1
prompt = "In a small village at the edge of a forest,",

story = StoryBot1(prompt)
filename = 'story.txt'
StoryBot1.save_story(story, filename)
print(f"Story saved to {filename}")