import argparse
from typing import List
import matplotlib.pyplot as plt


class SimulateOptions(argparse.Namespace):
    def __init__(
        self,
        ki: float = 1.0,
        km: float = 1.0,
        kn: float = 1.0,
        kf: float = 0.3,
        ps: float = 0.99,
        num_segments: int = 1000,
        output: str = "out",
    ):
        self.ki: float = ki
        self.km: float = km
        self.kn: float = kn
        self.kf: float = kf
        self.ps: float = ps
        self.num_segments: int = num_segments
        self.output: str = output


def plot_tcp(
    cw_list: List[float],
    options: SimulateOptions,
    name: str = "out",
):
    print(len(cw_list))
    plt.plot([*range(len(cw_list))], cw_list)
    plt.ylabel("Congestion Window")  # type: ignore
    plt.xlabel("Sequence Number")  # type: ignore
    plt.suptitle("TCP Congestion Window Simulation", fontweight="bold")

    plt.title(
        f"| $K_i$ = {options.ki} |  $K_m$ = {options.km} |  $K_n$ = {options.kn} |  $K_f$ = {options.kf} |  $P_s$ = {options.ps} |  $T$ = {options.num_segments} |",
        fontsize=10,
    )

    plt.tight_layout(pad=0.5)
    plt.savefig(
        f"./figures/{name}.png",
    )
    plt.close()


def output_file(name: str, cw_list: List[float]):
    with open(name, "w") as f:
        f.write("\n".join([str(cw) for cw in cw_list]))
