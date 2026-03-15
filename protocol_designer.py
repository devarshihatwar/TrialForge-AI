import boto3

# Create Bedrock client
client = boto3.client("bedrock-runtime", region_name="us-east-1")

print("=== Autonomous Clinical Trial Protocol Designer ===\n")

# Take user input
drug = input("Enter Drug Name: ")
disease = input("Enter Disease Name: ")
phase = input("Enter Trial Phase (Phase I/II/III): ")

# Create intelligent prompt
prompt = f"""
You are an expert clinical research scientist.

Design a complete clinical trial protocol for:

Drug: {drug}
Disease: {disease}
Trial Phase: {phase}

Include:

- Trial rationale
- Inclusion criteria
- Exclusion criteria
- Study design
- Primary endpoint
- Secondary endpoints
- Sample size estimate
- Duration
- Risk assessment
- Success probability estimation
"""

# Send to Nova
response = client.converse(
    modelId="amazon.nova-pro-v1:0",
    messages=[
        {
            "role": "user",
            "content": [{"text": prompt}],
        }
    ],
)

# Print protocol
result = response["output"]["message"]["content"][0]["text"]

print("\n=== Generated Clinical Trial Protocol ===\n")
print(result)