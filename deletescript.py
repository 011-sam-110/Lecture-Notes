import os
count = 1

while True:
    os.system(f'del "Chunk {count}.wav"')
    count += 1
    print(f"iteration {count}")