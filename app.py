from dotenv import load_dotenv
import os
import praw

from generate_persona import generate_persona_with_ollama, save_output


load_dotenv()

#print("Client Id:", os.getenv('Reddit_client_id'))
#print("secret:", os.getenv('REDDIT_CLIENT_SECRET'))
#print("User-Agent:", os.getenv("USER_AGENT"))

reddit=praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT")
)


def extract_username_from_url(url):
    url = url.rstrip('/')
    parts = url.split('/')
    if "user" in parts:
        return parts[parts.index("user") + 1]
    else:
        raise ValueError("Invalid Reddit user URL")


def fetch_user_data(profile_url):
    username=extract_username_from_url(profile_url)
    redditor=reddit.redditor(username)
    posts=[]
    print(f'fetching submissions by u/{username}')
    for submission in redditor.submissions.new(limit=5):
        posts.append(f'Title :{submission.title}\nText:{submission.selftext}\n')
        
        comments=[]
        print(f'fetching comments by u/{username}')
        
        return posts, comments
    
profile_url="https://www.reddit.com/user/kojied/comments/"
posts,comments=fetch_user_data(profile_url)

print('\n-=-posts--')
for i in posts:
    print(i)
    
print('\n --comments--')
for c in comments:
    print(c)
    
    
if __name__ == "__main__":
    profile_url = "https://www.reddit.com/user/Hungry-Move-6603/"
    username = extract_username_from_url(profile_url)
    posts, comments = fetch_user_data(profile_url)
    
    persona_text = generate_persona_with_ollama(username, posts, comments)
    save_output(username, persona_text)