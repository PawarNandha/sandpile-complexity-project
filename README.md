# Sandpile Model – Complexity Science Project

This project demonstrates Self Organized Criticality using the Bak-Tang-Wiesenfeld Sandpile Model.

A 2D grid is used where sand grains are added randomly. When the number of grains at a site reaches a threshold value (4), the site topples and distributes grains to its neighboring cells.

Concepts explored in this project:

Noise:
Random addition of sand grains to the system.

Avalanche:
Chain reaction of toppling events when the threshold is exceeded.

Connectivity:
Each cell interacts with its four nearest neighbors.

Results:
The distribution of avalanche sizes follows a power law behavior, which indicates self-organized criticality.

Files in this project:

sandpile_simulation.py – simulation code
avalanche_data.txt – avalanche size data
report.tex – latex report
report.pdf – final report