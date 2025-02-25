name = "Thanuja"
age = 21
height = 1.5
study = True

print(type(name))
print(type(age))
print(type(height))
print(type(study))

print(float(age))
print(int(height))
print(list(name))

ai_topics = ["Machine Learning", "Neural Networks", "Natural Language Processing", "Computer Vision"]
ai_topics.append("Reinforcement Learning")
print(ai_topics)
ai_topics.remove("Natural Language Processing")
print(ai_topics)
print(ai_topics[1])
print("------------------Dict---------------")
ai_skills = {"Machine Learning" : "intermediate", "Neural Networks": "advanced"}
ai_skills.update({"Reinforcement Learning": "beginner"})
ai_skills.update({"Machine Learning": "advanced"})
print(ai_skills)
print(ai_skills.keys())

students = [
    {"name":"John", "age":20, "height":1.5}, 
    {"name":"Mary", "age":40, "height":2.5}, 
    {"name":"Stella", "age":15, "height":4.4}
    ]

print(students[0].get("age"))




