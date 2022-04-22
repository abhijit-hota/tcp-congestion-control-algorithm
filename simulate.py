from math import ceil

from random import random
from typing import List


# Declaring constants (in kBs)
MSS = 1
RWS = 1 * 1024
CONGESTION_THRESHOLD_FACTOR = 0.5


def simulate(
    ki: float,
    km: float,
    kn: float,
    kf: float,
    ps: float,
    num_segments: int,
) -> List[float]:
    cw_list: List[float] = []
    cw = ki * MSS
    congestion_threshold = CONGESTION_THRESHOLD_FACTOR * RWS

    segments_left = num_segments

    while segments_left > 0:
        if random() < ps:
            segments_sent = ceil(cw / MSS)
            segments_left = max(segments_left - segments_sent, 0)

            if cw < congestion_threshold:
                # exponential
                cw = min(RWS, cw + km * MSS)
            else:
                # linear
                cw = min(cw + kn * (MSS**2 / cw), RWS)

        else:
            # timeout
            congestion_threshold = cw * CONGESTION_THRESHOLD_FACTOR
            cw = max(1, kf * cw)
        cw_list.append(cw)

    return cw_list
