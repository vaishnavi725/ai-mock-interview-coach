# AI Mock Interview Coach

A Streamlit app that runs a mock technical interview for a role you choose, then generates a feedback report at the end.

## How it works

- **Interviewer** — powered by Groq's `openai/gpt-oss-120b`, asks one question at a time based on the role and never repeats a question already asked.
- **Feedback** — powered by OpenAI's `gpt-4o-mini`, reviews the full transcript at the end and produces strengths, areas to improve, and a readiness score out of 10.
- **Memory** — each session's conversation is persisted to a local SQLite database (`data/interview_history.db`) keyed by your name, so an interview can be resumed later.

Built with [LangChain](https://python.langchain.com/) (LCEL chains) and [Streamlit](https://streamlit.io/).

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Create a `.env` file in the project root with your API keys:
   ```
   GROQ_API_KEY=your-groq-key
   OPENAI_API_KEY=your-openai-key
   ```
3. Run the app:
   ```
   streamlit run app.py
   ```

## Usage

Enter your name (used as the session ID) and the role you're interviewing for, then click **Start / Resume Interview**. Answer each question in the chat input. Click **End Interview & Get Feedback** when done to generate your feedback report.
