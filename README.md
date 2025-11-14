# k6 Performance Test Summarizer with OpenAI

This project provides a simple CLI tool (`main.py`) that takes the JSON output from a [k6](https://k6.io/) performance test and generates a **human-readable Markdown summary** using OpenAI’s GPT models.  

The summary is written in clear, non-technical language so that Product Owners or stakeholders can quickly understand the results, including successes, failures, and recommendations.

The prompt and max tokens used to summarise the results can be modified to suit any specific needs of the user.

---

## ✨ Features
- Parses k6 JSON output and extracts key metrics:
  - Average response time
  - 95th percentile latency
  - Error rate
  - Iterations
  - Max virtual users (VUs)
- Sends metrics to OpenAI for summarization
- Outputs a Markdown report (`report_summary.md`) with:
  - Clear summary of test results
  - Highlights of successes and failures
  - Recommendations for improvement

---

## 🔑 Requirements
- Python 3.9+
- OpenAI Python SDK (`pip install openai`)
- An OpenAI API key

---

## 🔒 Setup API Key
You need to create an OpenAI API key from the [OpenAI dashboard](https://platform.openai.com/account/api-keys) and save it as an environment variable named: OPENAI_API_KEY

---

## ▶️ How to run
To run the summary script, you will need to pass in your performance test results as a parameter in json format. 
### Bash:
``` 
k6 run --out json=- load_test.js | python main.py /dev/stdin
```
### Powershell:
```
k6 run --out json=results.json load_test.js
python main.py results.json
```
---

## ⚠️ Warning About Usage

This project uses the OpenAI API. While the free tier allows limited usage, **excessive requests or large outputs may exceed free limits and incur charges** on your OpenAI account.  

To avoid unexpected costs:
- Use the **gpt-4o-mini** model (default in this script) for efficiency.  
- Keep prompts concise and limit output length (`max_tokens`).  
- Monitor your usage in the [OpenAI dashboard](https://platform.openai.com/).  