import argparse
from math import ceil
from pathlib import PosixPath
from random import random
from typing import List


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
CONGESTION_THRESHOLD_FACTOR = 0.5


def simulate(options: SimulateOptions) -> List[float]:
    cw_list: List[float] = []
    cw = options.ki * MSS
    congestion_threshold = CONGESTION_THRESHOLD_FACTOR * RWS

    segments_left = options.num_segments

    while segments_left > 0:
        if random() < options.ps:
            segments_sent = ceil(cw / MSS)
            segments_left = max(segments_left - segments_sent, 0)

            if cw < congestion_threshold:
                # exponential
                cw = min(RWS, cw + options.km * MSS)
            else:
                # linear
                cw = min(cw + options.kn * (MSS**2 / cw), RWS)

        else:
            # timeout
            congestion_threshold = cw / 2
            cw = max(1, options.kf * cw)

        cw_list.append(cw)

    return cw_list
