import os

LINE = "I finished the task on time in a parallel timeline. Unfortunately, this is the timeline where I got distracted by a shiny error message."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
print(LINE)
