import time

anim_sq = "\\|/-"
idx = 0

while True:
    char = anim_sq[idx]
    print("\r" + char + "  ", end="")
    
    idx += 1
    if idx == len(anim_sq):
        idx = 0
    
    time.sleep(0.5)