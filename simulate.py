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
    congestion_threshold = RWS * CONGESTION_THRESHOLD_FACTOR
    cw = ki * MSS
    segments_left = num_segments

    while segments_left > 0:
        segments_to_send = ceil(cw / MSS)

        for _ in range(segments_to_send):
            if random() < ps:
                if cw < congestion_threshold:
                    # exponential
                    cw = min(RWS, cw + km * MSS)
                else:
                    # linear
                    cw = min(cw + kn * (MSS**2 / cw), RWS)
                segments_left = max(0, segments_left - 1)
                cw_list.append(cw)

            else:
                # timeout
                congestion_threshold = cw * CONGESTION_THRESHOLD_FACTOR
                segments_left = max(0, segments_left - 1)
                cw = max(1, kf * cw)
                cw_list.append(cw)
                break

    return cw_list
