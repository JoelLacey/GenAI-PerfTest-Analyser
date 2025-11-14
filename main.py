import argparse
import json
import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def summarize_with_ai(metrics):
    # Craft a prompt for GenAI
    prompt = f"""
    You are a QA Engineer running performance tests of your teams api, and reporting back to your Product owner who doesn't have a technical background. Summarize these k6 performance test results in clear,
    human-readable language, highlighting successes, failures, and recommendations. Format the summary in Markdown.

    Metrics:
    - Avg response time: {metrics['http_req_duration']['avg']} ms
    - 95th percentile: {metrics['http_req_duration']['p95']} ms
    - Error rate: {metrics['http_req_failed']['rate']*100:.2f}%
    - Iterations: {metrics['iterations']['count']}
    - Max VUs: {metrics['vus']['max']}
    """

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=300)

    return response.choices[0].message.content

def main():
    parser = argparse.ArgumentParser(description="Summarize k6 performance test results with AI")
    parser.add_argument("file", help="Path to k6 JSON results")
    args = parser.parse_args()

    with open(args.file) as f:
        data = json.load(f)
    metrics = data["metrics"]

    summary = summarize_with_ai(metrics)
    with open("report_summary.md", "w") as f:
        f.write(summary)

print("✅ Report summary saved to report_summary.md")

if __name__ == "__main__":
    main()
