def student_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_profile(name="Sara", age=20, grade="B+")
