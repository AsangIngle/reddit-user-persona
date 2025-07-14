Reddit User Persona Extractor
This project was made as part of the AI/LLM Engineer Internship assignment at BeyondChats.

The goal of this tool is to take a Reddit user's profile link, collect their recent posts and comments, and then use an LLM (via Ollama) to generate a well-structured User Persona. The persona includes traits, motivations, behavior, goals, and personality estimations — all backed by quotes or comments from the user's profile.

What This Script Does
Accepts a Reddit profile URL (like https://www.reddit.com/user/kojied/)

Scrapes their recent posts and comments

Uses an LLM (LLaMA 3 from Ollama) to analyze their personality and habits

Saves the final profile as a .txt file in the current directory

Mentions exactly which post or comment each insight came from

Tools Used
Python

PRAW (for accessing Reddit API)

Ollama (LLaMA 3)

python-dotenv (to securely load API keys)

How to Use It
Clone the project and open the folder

Make sure Python is installed and create a virtual environment

Install dependencies using the requirements.txt file

Set up your .env file with Reddit API credentials

Make sure Ollama is installed and the LLaMA 3 model is running

Run app.py and provide a Reddit user URL when prompted

After it runs, you'll get a text file like persona_kojied.txt in your folder

Example Output
For a user like Hungry-Move-6603, the script generated a profile with details like:

Traits: Time-efficient, Practical

Motivations: Self-care, Productivity

Frustrations: Overwhelm, lack of structure

Includes direct quotes from their posts and comments

This makes it easy to understand the person behind the profile in a detailed and structured way.

About the Author
Asang Triratna Ingle
Machine Learning Engineer | IIIT Nagpur
Email: asangingle@email.com
LinkedIn: linkedin.com/in/your-link