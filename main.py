import os

LINE = "I asked my AI for a dad joke. It said, 'I'm not a dad, but I do have 4,096 children. They're called tokens.'"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
print(LINE)
