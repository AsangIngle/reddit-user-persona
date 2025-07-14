from ollama import chat
import datetime

def build_prompt(username, posts, comments):
    content = '\n\n'.join([
        "### POSTS\n" + "\n".join(f"- {p.strip()}" for p in posts),
        "### COMMENTS\n" + "\n".join(f"- {c.strip()}" for c in comments)
    ])
    
    prompt = f"""
Given the following Reddit activity of user **{username}**, build a complete **User Persona** similar to the structure below:

---Format---
Name: {username}
Age: (guess if possible)
Occupation:
Status:
Location:
Tier:
Archetype:

### Traits
- Practical / Adaptable / Spontaneous / etc.

### Motivations
Convenience:
Wellness:
Speed:
Preferences:
Comfort:
Dietary Needs:

### Behaviour & Habits
(List insights here...)

### Frustrations
(List pain points...)

### Goals & Needs
(List 3–4 user goals...)

### Personality (Estimate levels)
Introvert ←→ Extrovert:
Intuition ←→ Sensing:
Feeling ←→ Thinking:
Perceiving ←→ Judging:

### Direct Quotes or Habits (Cite source)
Include citation for each insight as: [Post: "...text..."] or [Comment: "...text..."]

---

Now, based on the user's posts and comments below, build this full profile:

{content}
"""
    return prompt.strip()


def generate_persona_with_ollama(username, posts, comments, model='llama3'):
    prompt = build_prompt(username, posts, comments)
    
    response = chat(
        model=model,
        messages=[{'role': 'user', 'content': prompt}]
    )
    
    return response['message']['content']


def save_output(username, persona_text):
    filename = f'persona_{username}.txt'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(persona_text)
    print(f' Persona saved to: {filename}')
