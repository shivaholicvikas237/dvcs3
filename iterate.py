import os

from dvc.api import make_checkpoint

while True:
    try:
        if os.path.exists("int.txt"):
            with open("int.txt", "r") as fd:
                i_ = int(fd.read()) + 1
        else:
            i_ = 0

        # ... do something meaningful

        with open("int.txt", "w") as fd:
            fd.write(f"{i_}")

        if i_ % 100 == 0:
            make_checkpoint()

    except KeyboardInterrupt:
        exit()