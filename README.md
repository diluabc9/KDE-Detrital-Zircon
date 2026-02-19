The script is run and tested in Jupyter notebook using Anaconda software.

# KDE Script for Detrital Zircon Age Distributions

This Python script generates Kernel Density Estimates (KDE) and 
density-normalized histograms for detrital zircon U–Pb age datasets.

## Methodology
- Gaussian kernel
- Silverman bandwidth (1986)
- Custom bandwidth sharpening (/3 factor)

## Requirements
- Python 3.x
- numpy
- pandas
- matplotlib

Install dependencies:

pip install -r requirements.txt

## Usage

Place your CSV file in the same directory.

Run:

python kde_detrital_zircon.py input.csv

Output will be saved as:
KDE_output.jpeg

## Author
R Dileepkumar Reddy

## Version
1.0 (2026)

References:
1.	Van Rossum, G., & Drake, F. L. (2009), Python 3 Reference Manual, CreateSpace, Scotts Valley, CA.
2.	Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., Wieser, E., Taylor, J., Berg, S., Smith, N. J., Kern, R., Picus, M., Hoyer, S., van Kerkwijk, M. H., Brett, M., Haldane, A., Del Río, J. F., Wiebe, M., Peterson, P., Gérard-Marchant, P., Sheppard, K., Reddy, T., Weckesser, W., Abbasi, H., Gohlke, C., & Oliphant, T. E. (2020), Array programming with NumPy, Nature, 585, 357–362. https://doi.org/10.1038/s41586-020-2649-2.
3.	Hunter, J. D. (2007), Matplotlib: A 2D graphics environment, Computing in Science & Engineering, 9(3), 90–95, https://doi.org/10.1109/MCSE.2007.55.
4.	McKinney, W. (2010), Data structures for statistical computing in Python, Proceedings of the 9th Python in Science Conference, SciPy 2010, pp. 51–56.
5.	Kluyver, T., Ragan-Kelley, B., Pérez, F., et al., 2016, Jupyter Notebooks – a publishing format for reproducible computational workflows, Positioning and Power in Academic Publishing: Players, Agents and Agendas, 87–90.
6. Anaconda, Inc., 2020. Anaconda Software Distribution, https://anaconda.com.


## License
This project is licensed under the MIT License.

