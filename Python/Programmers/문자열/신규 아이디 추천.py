import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r"[^a-z0-9\-\_\.]", "", new_id)
    new_id = re.sub(r"\.{2,}", ".", new_id)
    new_id = re.sub(r"^\.+|\.+$", "", new_id)
    if not new_id:
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    new_id = re.sub(r"\.$", "", new_id)
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id