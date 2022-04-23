import argparse

from core import simulate
from utils import SimulateOptions, write_to_file_and_save_graph

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="python mytcp.py",
        description="Simulates an MIAD TCP congestion control algorithm based on input parameters as stated below.",
        epilog="The program generates 2 outputs — the image of the graph with the default name 'out.svg' and a text file containing all the congestion window values separated by newlines with the default name 'out.log'. The name, 'out', can be changed by the option '-o' as mentioned.",
    )
    parser.add_argument(
        "-i",
        metavar="Ki",
        dest="ki",
        type=float,
        default=1,
        help="(1.0 ≤ Ki ≤ 4.0) Initial congestion window (CW). Default = 1",
    )
    parser.add_argument(
        "-m",
        metavar="Km",
        dest="km",
        type=float,
        default=1,
        help="(0.5 ≤ Km ≤ 2.0) Multiplier of the congestion window, during the exponential growth phase. Default = 1",
    )
    parser.add_argument(
        "-n",
        metavar="Kn",
        dest="kn",
        type=float,
        default=1,
        help="(0.5 ≤ Kn ≤ 2.0) Multiplier of the congestion window, during the linear growth phase. Default = 1",
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
        metavar="Output filename",
        dest="output",
        type=str,
        default="out",
        help="The file name to output the results to.",
    )

    options = parser.parse_args(namespace=SimulateOptions())
    output_filename = options.output
    options.__delattr__("output")

    cw_values = simulate(**vars(options))
    write_to_file_and_save_graph(cw_values, options, output_filename)
