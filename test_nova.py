import boto3

# Create Bedrock client
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Send request to Nova
response = client.converse(
    modelId="amazon.nova-pro-v1:0",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "text": """
                    You are an expert clinical research scientist.

                    Design a clinical trial protocol for a new drug treating hypertension.

                    Include:
                    - Trial Phase
                    - Inclusion criteria
                    - Exclusion criteria
                    - Study design
                    - Primary endpoint
                    - Secondary endpoint
                    - Sample size estimate
                    - Duration
                    - Risk assessment
                    """
                }
            ],
        }
    ],
)

# Print response
print(response["output"]["message"]["content"][0]["text"])