"""Entry program for make.fun bounty "Sum up 22 November's world news in one image".

Copies the pre-built poster (entry.png, held in this repo) to /output/entry.png.
Runs offline; deterministic - both runs write identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"

os.makedirs("/output", exist_ok=True)
shutil.copyfile(SRC, DST)
print("Wrote", DST)
