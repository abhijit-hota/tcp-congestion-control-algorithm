import argparse
from pathlib import PosixPath
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
        self.output: PosixPath


def plot_tcp(cw_list: List[float], name: str = "out"):
    print(len(cw_list))
    plt.plot([*range(len(cw_list))], cw_list)
    plt.savefig(f"./figures/{name}.png")
    plt.close()
