import os

LINE = "Our 24-hour sprint starts with a 23-hour planning meeting. We ship the meeting on time; the feature is still in the backlog."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
print(LINE)
