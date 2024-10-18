import numpy as np
import math
def main():
    print(f"{'x':<10} {'sin(x)':<10}")
    steps = np.linspace(0, 2, 1000)
    for step in steps:
        print(f"{step:<10.4f} {math.sin(step):<10.4f}")
if __name__ == "__main__":
    main()