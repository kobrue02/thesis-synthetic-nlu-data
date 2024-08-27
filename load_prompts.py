import os

def load_prompts():
    prompts = []
    prompt_dir = 'prompts'
    for filename in os.listdir(prompt_dir):
        if filename.endswith(".prompt"):
            with open(os.path.join(prompt_dir, filename), 'r') as file:
                prompt = file.read()
                prompts.append(prompt)
    return prompts


if __name__ == '__main__':
    prompts = load_prompts()
    for prompt in prompts:
        print(prompt.format(number='10', intents=['intent1, intent2']))
        print("-" * 80)
