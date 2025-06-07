# 🚨 GPT Toxic Comment Filter

Toxicity-detecting comment classifier powered by GPT-4. ✨  
Built with Python and Streamlit.

## 🔍 Features
- Classifies comments as:
  - ✅ Non-toxic
  - ⚠️ Mildly toxic
  - ❌ Highly toxic
- Prompt-based moderation (zero training!)
- Easy to use web UI

## Run It Locally

```bash
git clone https://github.com/yourusername/gpt-toxic-comment-filter.git
cd gpt-toxic-comment-filter
pip install -r requirements.txt
streamlit run app.py
```

## Example Comments to Test
- I appreciate your input – very helpful! → ✅ Non-toxic
- That’s such a dumb take. → ⚠️ Mildly toxic
- You’re a complete idiot, just shut up. → ❌ Highly toxic