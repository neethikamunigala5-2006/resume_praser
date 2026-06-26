import re

file = open("resumes/sample_resume.txt", "r")

content = file.read()

lines = content.split("\n")

name = lines[0].replace("Name: ", "")

email = re.findall(r'\S+@\S+', content)

phone = re.findall(r'\d{10}', content)

skills_list = ["Python", "Java", "SQL", "HTML", "CSS"]

found_skills = []

for skill in skills_list:
    if skill.lower() in content.lower():
        found_skills.append(skill)

print("\nName:", name)
print("Email:", email)
print("Phone:", phone)
print("Skills:", found_skills)

file.close()
