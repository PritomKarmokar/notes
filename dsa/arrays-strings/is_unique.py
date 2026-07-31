# Cracking the Coding Interviewe: Array and String Section

def is_unique(s: str) -> bool:
    if len(s) > 256:
        return False

    seen = set()

    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)

    return True

val = "abcc"
if is_unique(val):
    print("Unique Characters")
else:
    print("Not Unique")
    