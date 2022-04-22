import argparse
from pathlib import PosixPath
from random import random


class SimulateOptions(argparse.Namespace):
    def __init__(self):
        self.ki: float = 1.0
        self.km: float = 1.0
        self.kn: float = 1.0
        self.kf: float
        self.ps: float
        self.num_segments: int
        self.output: PosixPath


# Declaring constants (in kBs)
MSS = 1
RWS = 1 * 1024
CONGESTION_THRESHOLD = 0.5


def simulate(options: SimulateOptions):
    cw = options.ki * MSS
    ssthresh = CONGESTION_THRESHOLD * RWS

    for _ in range(options.num_segments):
        if random() < options.ps:
            if cw < ssthresh:
                # exponential
                cw = min(RWS, cw + options.km * MSS)
            else:
                # linear
                cw = min(cw + options.kn * (MSS**2 / cw), RWS)

        else:
            # timeout
            ssthresh = cw / 2
            cw = max(1, options.kf * cw)

        print(cw)

