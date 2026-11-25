"""Copy the pre-written advice line into the grader's output directory."""

import os
import shutil


def main():
    # The advice line lives in entry.txt, written before grading began.
    # This step only carries it into the output folder untouched.
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copyfile(
        os.path.join(here, "entry.txt"),
        os.path.join(out_dir, "entry.txt"),
    )


if __name__ == "__main__":
    main()
