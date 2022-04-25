---
documentclass: article
fontsize: 12pt
geometry: "a4paper,left=20mm,top=20mm"
output: pdf_document
---
\setcounter{page}{3}

# Results

## \boldmath $P_s = 0.99$

When the probability is 0.99, we see that we get the expected sawtooth behavior from the graphs. We go over the graphs one by one:

![](figures/ki_1-km_1-kn_0.5-kf_0.1-ps_0.99.svg)

Here, we see that the highest CW value is low $\approx 24$. This can be the result of a lower $K_f$ value. A low $K_f$ value decreases the CW by a 90% and throws it back into slow start, every time a timeout occurs. 

Also, notice the near-prefect sawtooth shape from sequence number $\approx 600$ to the end. The CW falls back to the same value every timeout.

![](figures/ki_1-km_1-kn_0.5-kf_0.3-ps_0.99.svg)

While we saw a few near perfect sawtooth shape in the previous graph, this graph tells a different story. This has bigger sawtooth shapes followed by smaller ones lasting for lesser sequences. This process repeats from sequence number $\approx 160$ to $300$ and starts again from there to $700$. Ths can be attributed to a higher $K_f$ value which decreases the CW value by $70\%$. 

We also see a higher maximum CW value of $\approx 68$.

![](figures/ki_1-km_1-kn_1-kf_0.1-ps_0.99.svg)

Here, we increase $K_n$ to 1 and observe that the graphs becomes more steeper (higher slope) during the phase when they are more than the congestion threshold. This is inline with the formula given for the linear growth phase.

Also, observe the clean sawtooth shape towards the end.

![](figures/ki_1-km_1-kn_1-kf_0.3-ps_0.99.svg)

This tells the same story of higher valued slopes owing to a higher $K_n$ value and smaller sawteeth following the larger ones which are a result of a higher $K_f$ value.

![](figures/ki_1-km_1.5-kn_0.5-kf_0.1-ps_0.99.svg)

The maximum value of the CW in this graph is rather high. The high $K_m$ value is responsible for this.

This graph is observed to have a very flat slope in the linear phase. It owes it to the low $K_n$ value and the initial maxima of CW.

![](figures/ki_1-km_1.5-kn_0.5-kf_0.3-ps_0.99.svg)

Similar observation as above can be made to this graph.

![](figures/ki_1-km_1.5-kn_1-kf_0.1-ps_0.99.svg)

This graph is an interesting case of chance. Notice how the slopes looks steep but they are actually not if you calculate the actual slope value. The reason being the highest CW values is very low.

This graph (and a couple of other graphs below) tell us that the shape is dependent on the initial bump of the CW value. Here, the timeout occurs at an early stage which hinders the growth of CW and gives this shape to the graph.

![](figures/ki_1-km_1.5-kn_1-kf_0.3-ps_0.99.svg)

This graph has a high initial CW bump and capped peaks, owing to the high $K_f$ value. The CW doesn't go all the way down and hence the slow start can go higher up to the threshold without getting timed out quickly.

For the following graphs, similar qualitative analytics can be made. The $K_i$ is made higher in the following graphs which make it more probable to have higher CW values.

![](figures/ki_4-km_1.5-kn_0.5-kf_0.1-ps_0.99.svg)
![](figures/ki_4-km_1.5-kn_0.5-kf_0.3-ps_0.99.svg)
![](figures/ki_4-km_1.5-kn_1-kf_0.1-ps_0.99.svg)
![](figures/ki_4-km_1.5-kn_1-kf_0.3-ps_0.99.svg)
![](figures/ki_4-km_1-kn_0.5-kf_0.1-ps_0.99.svg)
![](figures/ki_4-km_1-kn_0.5-kf_0.3-ps_0.99.svg)
![](figures/ki_4-km_1-kn_1-kf_0.1-ps_0.99.svg)
![](figures/ki_4-km_1-kn_1-kf_0.3-ps_0.99.svg)

## \boldmath $P_s = 0.9999$

When we set the probability of a successful send to $0.9999$, we get very bland graphs. For almost all the parameters, we see that the graph goes linearly (additive increase) up to the congestion threshold $(RSS / 2 = 512 kB)$ and then becomes constant at that.

A timeout doesn't occur/rarely occurs in this case.

![](figures/ki_1-km_1.5-kn_0.5-kf_0.1-ps_0.9999.svg)
![](figures/ki_1-km_1.5-kn_0.5-kf_0.3-ps_0.9999.svg)
![](figures/ki_1-km_1.5-kn_1-kf_0.1-ps_0.9999.svg)
![](figures/ki_1-km_1.5-kn_1-kf_0.3-ps_0.9999.svg)
![](figures/ki_1-km_1-kn_0.5-kf_0.1-ps_0.9999.svg)
![](figures/ki_1-km_1-kn_0.5-kf_0.3-ps_0.9999.svg)
![](figures/ki_1-km_1-kn_1-kf_0.1-ps_0.9999.svg)
![](figures/ki_1-km_1-kn_1-kf_0.3-ps_0.9999.svg)

![](figures/ki_4-km_1.5-kn_0.5-kf_0.1-ps_0.9999.svg)
![](figures/ki_4-km_1.5-kn_0.5-kf_0.3-ps_0.9999.svg)
![](figures/ki_4-km_1.5-kn_1-kf_0.1-ps_0.9999.svg)
![](figures/ki_4-km_1.5-kn_1-kf_0.3-ps_0.9999.svg)
![](figures/ki_4-km_1-kn_0.5-kf_0.1-ps_0.9999.svg)
![](figures/ki_4-km_1-kn_0.5-kf_0.3-ps_0.9999.svg)
![](figures/ki_4-km_1-kn_1-kf_0.1-ps_0.9999.svg)
![](figures/ki_4-km_1-kn_1-kf_0.3-ps_0.9999.svg)
