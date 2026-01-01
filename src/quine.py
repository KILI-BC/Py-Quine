# ASSETS:
newline = "\n"
backslash = "\\"
s = """f.writelines("# ASSETS:" + newline)
f.writelines('newline = "' + backslash + 'n"' + newline)
f.writelines('backslash = "' + backslash + backslash + '"' + newline)
f.writelines("s = " + '"' * 3)
f.writelines(s)
f.writelines('"' * 3 + newline)
f.writelines("# CODE:" + newline)
f.writelines('with open("quine_cpy.py", "wt") as f:' + newline)
for l in s.splitlines():
    f.writelines("    " + l + newline)
"""
# CODE:
with open("quine_cpy.py", "wt") as f:
    f.writelines("# ASSETS:" + newline)
    f.writelines('newline = "' + backslash + 'n"' + newline)
    f.writelines('backslash = "' + backslash + backslash + '"' + newline)
    f.writelines("s = " + '"' * 3)
    f.writelines(s)
    f.writelines('"' * 3 + newline)
    f.writelines("# CODE:" + newline)
    f.writelines('with open("quine_cpy.py", "wt") as f:' + newline)
    for l in s.splitlines():
        f.writelines("    " + l + newline)
