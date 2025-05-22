import boto3
import json

bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1")

messages = []

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": user_input
            }
        ]
    })

    kwargs = {
        "modelId": "anthropic.claude-3-haiku-20240307-v1:0",
        "contentType": "application/json",
        "accept": "application/json",
        "body": json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "messages": messages
        })
    }

    response = bedrock_runtime.invoke_model(**kwargs)
    body = json.loads(response["body"].read())
    bot_reply = body["content"][0]["text"]
    print("Bot:", bot_reply)

    # Add bot reply to conversation history
    messages.append({
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": bot_reply
            }
        ]
    })