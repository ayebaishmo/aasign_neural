from storybot import StoryBot1
prompts = [
    "In a small village at the edge of a forest,",
    "Long ago, in a kingdom far away,",
    "Beneath the waves of the great ocean,",
]

for i, prompt in enumerate(prompts, 1):
    story = StoryBot1(prompt)
    filename = 'generated_stories.text'
    StoryBot1.save_story(story, filename)
    print(f"Story {i} saved to {filename}")