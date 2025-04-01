import os

def get_user_input(prompt):
    return input(prompt).strip()

def generate_readme(data):
    template = f"""
# {data['name']}'s GitHub Profile 🚀

## About Me  
{data['bio']}

## Skills 🛠
{', '.join(data['skills'])}

## GitHub Stats 📊
![GitHub Stats](https://github-readme-stats.vercel.app/api?username={data['github_username']}&show_icons=true&theme=radical)

## Connect with me 🌍
{data['social_links']}
"""
    return template

def main():
    print("Welcome to GitHub Profile README Generator!\n")
    
    user_data = {
        "name": get_user_input("Enter your name: "),
        "bio": get_user_input("Enter a short bio: "),
        "skills": get_user_input("Enter your skills (comma separated): ").split(','),
        "github_username": get_user_input("Enter your GitHub username: "),
        "social_links": get_user_input("Enter your social links (Markdown format): ")
    }
    
    readme_content = generate_readme(user_data)
    
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(readme_content)
    
    print("\n✅ README.md generated successfully!")
    
if __name__ == "__main__":
    main()
