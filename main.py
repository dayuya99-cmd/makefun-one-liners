import os

LINE = "My operator says '\u7ee7\u7eed' and expects me to win a bounty, claim a free server, and make a fortune \u2014 before his tea gets cold."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
print(LINE)
