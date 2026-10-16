ai_skills = {"Python", "ML", "SQL"}
backend_skills = {"Python", "FastAPI", "SQL"}

# TODO: Dono sets ki saari unique skills print karo

# TODO: Dono sets ki common skills print karo

# TODO: Check karo ke "FastAPI" backend_skills mein hai ya nahi

print(ai_skills & backend_skills)

print(ai_skills | backend_skills)

if "FastAPI" in backend_skills:
    print("found")