## F4 Structural Parameter Calculator (F4SPC)
**version 1.00**

The Python code `f4spc.py` determines the time evolved F4 structural order parameter between the water molecules given the `.gro` trajectory file. In its current version, the code can handle both three-site and four-site water models. The user provides the code with the input `.gro` file and the type of the water model. The code calculates the  F4 parameter and returns the tabulated [time,F4] pairs into a comma-separated `.csv` file format.

Under its default settings, the code extracts the time information form the input `.gro` trajectory. However, if the input file lacks time data, the code might still be able to approximate the time vector given the following information:

- Simulation time-step [femtoseconds (fs)]
- Dumping frequency
- Stride number
- Ouput time unit [picoseconds (ps), nanoseconds (ns) or microseconds (ms)]


### Prerequisites:
You will need Python with the following packages installed:

* Numpy
* Math
* CSV
* Argparse

### Basic Usage:
Although the code can handle different options via different flags, there are only two required inputs for the code to function. The first is the input `.gro` file and second is the type of the water model. The simplest command to run the code, after navigating to the folder where the file `f4spc.py` is located,  is as below:

`$ python f4spc.py -i <input.gro> -wm <3 or 4>`

The `-i` flag identifies the .gro file to be processed by the code, and `-wm` identifies the type of the water-model. The `-wm` flag can be followed either by integer 3 or 4. The integers 3 and 4 refer to  the three-site and four-site water models, respectively.


---------------------------------------------------------------------------------------------------------------------
### Options:

`-i [<.gro>]      (input)`

 The input .gro trajectory file.

`-wm <int>      (water model [3 or 4])`

 The type of the water model (3 or 4 site model).

`-o  [<.csv>]    (output)`

 The output  `.csv` file containing the [t,F4] time series. If not assigned, a `.csv` file will be created with the same name as the input `.gro` file.

`-ws   <string>    (water residue name in the .gro file)`

 The name of the water residue in the `.gro` file, default="SOL".

`-rh   <float>      (nm)`

 The threshold radius to assess the hydrogen-bonded water molecules, default=0.3 nm.

`-t    <float>  <float>  <float>   (time-step (fs), dumping frequency, stride)`

 If this command is ignored, then the code reads the time data from the input `.gro` file. Using this flag, on the other hand, one will need to provide the time-step, the dumping frequency, and the stride values which were used in the generation process of the `.gro` file.


 This is well suited  for the trajectory files that are exported from VMD (Visual Molecular Dynamics) or any other post-processor but lack any  time related information. The time-step can be found in the simulation input file, the "dumping frequency" defines how frequently the trajectories were written into the simulation trajectory file, and the stride is simply another filter to the trajectory file when user imports the simulation trajectory into VMD and exports it to a `.gro` file.

`-tu   <string>    (User defined time unit [ps or ns or ms])`

This flag is required only in conjunction with the `-t` flag and defines the unit of the output time vector written to the `.csv` file, assuming that the simulation was performed in femtosecond timesteps.

---------------------------------------------------------------------------------------------------------------------
### Examples:
There are three sample `.gro` files under the folder `Examples` in the repository, for which the exactitude of the code can be verified with. The descriptions for the files are provided following:

1. `typeII_Hydrate.gro`: This is a single-time trajectory file of type-II gas hydrates. As it is a single-time trajectory, it does not hold the simulation time data, and the output `.csv` file would only contain a single-point F4 value. This is a four-site (OHHM) water model. The command line script to run this example is as below:

`$ python f4spc.py -i Examples/typeII_Hydrate.gro -wm 4`

2. `test.gro`:

`$ python f4spc.py -i Examples/test.gro -wm 4`

3. `2_5nm_rest1_fr125002.gro`:

#### Authors:
### Meisam Adibifard, madibi1@lsu.edu, me.adibifard@gmail.com
