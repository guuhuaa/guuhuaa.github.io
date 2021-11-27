import os

path = "/home/kun/Documents/web/guuhuaa.github.io/专栏/"

def RNAME(path):
    for name in os.listdir(path):
        child = os.path.join(path, name)
        if os.path.isdir(child):
            continue
        else:
            if (name.endswith(".md")):
                os.rename(child, child.replace(".md", ".html"))


for name in os.listdir(path):
    child = os.path.join(path, name)
    if os.path.isdir(child):
        RNAME(child)
