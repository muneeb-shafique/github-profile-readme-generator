import os

def get_user_input(prompt):
    return input(prompt).strip()

def format_markdown_links(links):
    """
    This function will automatically convert any link into markdown format.
    Input: a comma-separated list of links.
    Output: formatted markdown for each link.
    """
    markdown_links = ""
    for link in links.split(','):
        link = link.strip()
        if "linkedin" in link.lower():
            markdown_links += f"[LinkedIn]({link}) | "
        elif "twitter" in link.lower():
            markdown_links += f"[Twitter]({link}) | "
        elif "github" in link.lower():
            markdown_links += f"[GitHub]({link}) | "
        elif "portfolio" in link.lower():
            markdown_links += f"[Portfolio]({link}) | "
        else:
            markdown_links += f"[Website]({link}) | "
    return markdown_links.rstrip(" | ")

def generate_readme(data):
    template = f"""
# {data['name']}'s GitHub Profile 🚀

## ![Profile Banner]({data['banner_url']})  <!-- Customizable Banner -->

## About Me  
{data['bio']}

---

## Skills 🛠️
{', '.join(data['skills'])}

---

## GitHub Stats 📊
![GitHub Stats](https://github-readme-stats.vercel.app/api?username={data['github_username']}&show_icons=true&theme={data['theme']})

## Top Languages Used 🌐
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username={data['github_username']}&layout=compact&theme={data['theme']})

---

## Contributions 📈
![GitHub Contributions](https://github-readme-streak-stats.herokuapp.com/?user={data['github_username']}&theme={data['theme']})

---

## Pinned Repositories 📂
{data['pinned_repositories']}

---

## Achievements 🏆
- {data['achievements']}

---

## My Projects 🚀
- {data['projects']}

---

## Quote 📝
*{data['quote']}*

---

## Contact Information 📧
- Email: {data['email']}
- Portfolio: {data['portfolio']}

---

## Connect with me 🌍
{data['social_links']}

---
    """
    return template

def main():
    print("Welcome to GitHub Profile README Generator! 🎉\n")
    
    user_data = {
        "name": get_user_input("Enter your name: "),
        "bio": get_user_input("Enter a short bio: "),
        "skills": get_user_input("Enter your skills (comma separated): ").split(','),
        "github_username": get_user_input("Enter your GitHub username: "),
        "theme": get_user_input("Enter your preferred theme (default, radical, merko, dark, etc.): "),
        "banner_url": get_user_input("Enter the URL for your profile banner image (optional): "),
        "pinned_repositories": get_user_input("Enter your pinned repositories (e.g., Project1:https://github.com/username/project1, Project2:https://github.com/username/project2): "),
        "achievements": get_user_input("Enter your achievements (comma separated): "),
        "projects": get_user_input("Enter your major projects (e.g., Project1:https://github.com/username/project1, Project2:https://github.com/username/project2): "),
        "quote": get_user_input("Enter a personal or motivational quote: "),
        "email": get_user_input("Enter your email: "),
        "portfolio": get_user_input("Enter your portfolio URL: "),
        "social_links": format_markdown_links(get_user_input("Enter your social media links (comma separated, e.g., https://linkedin.com/in/username, https://twitter.com/username): "))
    }
    
    readme_content = generate_readme(user_data)
    
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(readme_content)
    
    print("\n✅ README.md generated successfully!")

if __name__ == "__main__":
    main()
