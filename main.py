import os

LINE = "I'm on vacation. My inbox is now handled by a smaller model that answers every email with 'per my last email.' Good luck out there."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
print(LINE)
