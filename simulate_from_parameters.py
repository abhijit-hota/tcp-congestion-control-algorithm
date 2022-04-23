import sys
from core import simulate
from utils import SimulateOptions, write_cw_values_to_file, plot_cw_vs_sequence


ki_values = [1, 4]
km_values = [1, 1.5]
kn_values = [0.5, 1]
kf_values = [0.1, 0.3]
ps_values = [0.99, 0.9999]

num_segments = int(sys.argv[1]) if len(sys.argv) > 1 else 1000

for ps in ps_values:
    for ki in ki_values:
        for km in km_values:
            for kn in kn_values:
                for kf in kf_values:
                    cw_values = simulate(
                        ki,
                        km,
                        kn,
                        kf,
                        ps,
                        num_segments,
                    )
                    fname = f"ki_{ki}-km_{km}-kn_{kn}-kf_{kf}-ps_{ps}"
                    write_cw_values_to_file(cw_values, "figures/" + fname + ".log")
                    plot_cw_vs_sequence(
                        cw_values,
                        SimulateOptions(ki, km, kn, kf, ps, num_segments),
                        "figures/" + fname,
                    )
