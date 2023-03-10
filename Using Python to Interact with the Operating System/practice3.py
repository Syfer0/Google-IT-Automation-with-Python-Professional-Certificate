import os
dir_fd = os.open('somedir', os.O_RDONLY)
def opener(path, flags):
    return os.open(path, flags, dir_fd=dir_fd)

with open('spamspam.txt', 'w', opener=opener) as f:
    print('This will be written to somedir/spamspam.txt', file=f)

os.close(dir_fd)  # don't leak a file descriptor