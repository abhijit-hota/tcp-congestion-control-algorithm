import argparse

from simulate import simulate
from utils import SimulateOptions, output_file, plot_tcp

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i",
        metavar="Ki",
        dest="ki",
        type=float,
        default=1,
        help="(1.0 ≤ Ki ≤ 4.0) Initial congestion window (CW)",
    )
    parser.add_argument(
        "-m",
        metavar="Km",
        dest="km",
        type=float,
        default=1,
        help="(0.5 ≤ Km ≤ 2.0) Multiplier of the congestion window, during the exponential growth phase.",
    )
    parser.add_argument(
        "-n",
        metavar="Kn",
        dest="kn",
        type=float,
        default=1,
        help="(0.5 ≤ Kn ≤ 2.0) Multiplier of the congestion window, during the linear growth phase.",
    )
    parser.add_argument(
        "-f",
        metavar="Kf",
        dest="kf",
        type=float,
        required=True,
        help="(0.1 ≤ Kf ≤ 0.5) Multiplier when a timeout occurs",
    )
    parser.add_argument(
        "-s",
        metavar="Ps",
        dest="ps",
        type=float,
        required=True,
        help="(0.0 < Ps < 1.0) Probability of receiving the ACK packet for a given segment before its timeout occurs.",
    )
    parser.add_argument(
        "-T",
        metavar="Total",
        dest="num_segments",
        type=int,
        required=True,
        help="Total number of segments to be sent before the emulation stops",
    )
    parser.add_argument(
        "-o",
        metavar="Output File",
        dest="output",
        type=str,
        default="out.log",
        help="The filepath to write the results to",
    )

    options = parser.parse_args(namespace=SimulateOptions())
    output = options.output
    options.__delattr__("output")

    cw_list = simulate(**vars(options))

    output_file(output, cw_list)
    with open(output, "w") as f:
        f.write("\n".join([str(cw) for cw in cw_list]))

    plot_tcp(cw_list)
