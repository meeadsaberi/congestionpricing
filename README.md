# Congestion pricing in AIMSUN
Implementing congestion pricing in AIMSUN mesoscopic traffic simulation

This repository includes instructions on how to implement congestion pricing in a mesoscopic dynamic traffic model in AIMSUN and the associated python scripts for it.

You may first want to download an already existing meso model in AIMSUN. We encourage you to use the calibrated and validation meso model of Melbourne, either from another repository https://github.com/meeadsaberi/dynamel or directly from https://www.cityxlab.com/dta.html

After having the meso model running with no problem in AIMSUN, first thing you need to consider for congestion pricing is to specify the desired Generalized Cost Function (GCF) for both priced and non-priced links in the network given a particular pricing scheme. Here in "cost_function.py", we provide the GCF for an adavnced pricing sceheme with joint distance and delay toll. For more information on the pricing scheme, see our publication here:
https://www.sciencedirect.com/science/article/pii/S0968090X18300573

In total we introduce four GCFs: intial and dynamic cost functions for non-priced links, and initial and dynamic cost functions for priced links. In AIMSUN, you have to allocate your GCFs to the right groups of links, e.g., the cost functions for priced links should be allocated to the group of links that forms your pricing zone.

Now that the GCFs are specified and allocated to the approrpiate groups of links in the model, you can set up and run the provided "pricing_API.py".

The provided codes are expected to work with no or limited modification with the Melbourne meso model in AIMSUN. However, if you want to use this code for your own model, you need to adjust a few things including the start and end of simulation, simulation time-intervals, etc.

For questions, please contact Ziyuan Gu (ziyuan.gu@unsw.edu.au).
