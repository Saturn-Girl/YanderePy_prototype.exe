import openai

# Use your actual API key here (ensure it's not publicly shared)
openai.api_key = "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"

# Prompt entered by the user
prompt = input("Enter your prompt: ")

# Send the prompt to OpenAI API and get the response
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Change to a newer model
    messages=[{"role": "user", "content": prompt}],
    max_tokens=50
)

# Print the response
print("Response:", response['choices'][0]['message']['content'].strip())
input("press any key to exit")
