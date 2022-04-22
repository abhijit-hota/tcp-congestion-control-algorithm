import argparse
from typing import List
import matplotlib.pyplot as plt


class SimulateOptions(argparse.Namespace):
    def __init__(self):
        self.ki: float = 1.0
        self.km: float = 1.0
        self.kn: float = 1.0
        self.kf: float
        self.ps: float
        self.num_segments: int
        self.output: str


def plot_tcp(cw_list: List[float], name: str = "out"):
    print(len(cw_list))
    plt.plot([*range(len(cw_list))], cw_list)
    plt.savefig(f"./figures/{name}.png")
    plt.close()


def output_file(name: str, cw_list: List[float]):
    with open(name, "w") as f:
        f.write("\n".join([str(cw) for cw in cw_list]))
