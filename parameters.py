from simulate import simulate
from utils import output_file, plot_tcp


ki_values = [1, 4]
km_values = [1, 1.5]
kn_values = [0.5, 1]
kf_values = [0.1, 0.3]
ps_values = [0.99, 0.9999]

for ps in ps_values:
    for ki in ki_values:
        for km in km_values:
            for kn in kn_values:
                for kf in kf_values:
                    cw_values = simulate(ki, km, kn, kf, ps, num_segments=1000000)
                    fname = f"{ki}_{km}_{kn}_{kf}_{ps}"
                    output_file(fname, cw_values)
                    plot_tcp(cw_values, fname)
