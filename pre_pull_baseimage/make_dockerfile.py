import os
import sys

def main(version):

    path = "Dockerfile"
    if (os.path.isfile(path)):
        return
    
    with open("Dockerfile", mode="w", encoding="utf-8") as f:
        f.write(f"FROM python:{version}-bookworm")