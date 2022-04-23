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


def write_to_file_and_save_graph(
    cw_list: List[float],
    options: SimulateOptions,
    name: str = "out",
):
    print("Simulated for following parameters:")
    print(
        f"Ki = {options.ki}, Km = {options.km}, Kn = {options.kn}, Kf = {options.kf}, Ps = {options.ps}, T = {options.num_segments}"
    )

    # Plot
    plt.plot([*range(len(cw_list))], cw_list)
    plt.ylabel("Congestion Window (in MSS)", labelpad=8, fontweight="bold")
    plt.xlabel("Sequence Number", labelpad=10, fontweight="bold")
    plt.title(
        f"$K_i$ = {options.ki} $│$ $K_m$ = {options.km} $│$ $K_n$ = {options.kn} $│$ $K_f$ = {options.kf} $│$ $P_s$ = {options.ps} $│$ $T$ = {options.num_segments}",
        fontsize=10,
        fontweight="bold",
        y=1.02,
    )

    plt.tight_layout()
    plt.savefig(f"{name}.svg")
    plt.close()

    # Write values to file
    with open(name + ".log", "w") as f:
        f.write("\n".join([str(cw) for cw in cw_list]))

    print("Saved log file and graph.")
    print("----------------------------------------------------------------")
