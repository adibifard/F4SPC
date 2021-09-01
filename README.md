## F4 Structural Parameter Calculator (F4SPC)
**version 1.00**

The Python code `f4spc.py` calculates the F4 structural order parameter between the water molecules giving the `.gro` trajectory file as its input. In its current version, the code can run with both three-site and four-site water models. The user provides the input `.gro` file and the type of the water model. Subsequently, the output (time,F4) data are written into a comma-separated `.csv` file. In its default settings, the code also elicits the time data form the input `.gro` file. However, if the input file lacks the information regarding the simulation time, the code might still be able to approximate the time series given the following parameters:

- Simulation time-step [femtoseconds (fs)]
- Dumping frequency
- Stride
- Ouput time unit [picoseconds (ps), nanoseconds (ns) or microseconds (ms)]


### Prerequisites:
You will need Python with the following packages installed:

* Numpy
* Math
* CSV
* Argparse

### Usage:
Although the code can handle many options via different flags, there are only two mandatory inputs for the code. The first is the input `.gro` file and second is the type of the water model
(either a 3-point or 4-point). After moving to the folder where the f4spc.py code is located, the basic command to run the code comes like following:

`$ python f4spc.py -i input.gro -wm (3 or 4)`

The `-i` flag identifies the .gro file to be processed by the code, and the `-wm` flag identifies the type of the water-model. The `-wm` flag can be followed by the integers 3 or 4. The integer 3 refers  the three-site water model arranged as OHH in the .gro file, while in the four-site water model the atoms of a water molecule are arranged as OHHM. Where m is the imaginary particle



---------------------------------------------------------------------------------------------------------------------
### Options:

`-i [<.gro>]      (input)`

 The input .gro trajectory file.

`-wm <int>      (water model [3 or 4])`

 The type of the water model (3-point or 4-point model).

`-out  [<.csv>]    (output)`

 The output  `.csv` file holding the tabulated [t,F4] data. If not assigned, a `.csv` file will be created with the same name as the input `.gro` file.

`-ws   <string>    (water residue name in the .gro file)`

 The name of the water residue in the `.gro` file, default="SOL".

`-rh   <float>      (nm)`

 The threshold radius for hydrogen-bonded molecules, default=0.3 nm.

`-t    <float>  <float>  <float>   (time-step (fs), dumping frequency, stride)`

 If this command is ignored, then the code reads the time data from the input `.gro` file. On the other hand, utilizing this flag, one will need to provide the time-step, the dumping frequency, and the stride values used in the generation process of the `.gro` file.


 This is well suited  for the `.gro` files that are exported from VMD (Visual Molecular Dynamics) post-processor but lack the time data. The time-step can be found in the simulation input file, and the "dumping frequency" defines how frequently the trajectories are written into the simulation output file. Stride is another filter to the trajectory file when user imports the simulation trajectory into VMD and exports it to a `.gro` file.

`-tu   <string>    (User defined time unit [ps or ns or ms])`

This flag is only required in conjunction with the `-t` flag, and defines the unit of the output time vector written to the `.csv` file, assuming that the simulation was performed in femtosecond timesteps.

---------------------------------------------------------------------------------------------------------------------
### Examples:
There are three

#### Authors:
### Meisam Adibifard, madibi1@lsu.edu, me.adibifard@gmail.com

#### PI:
### Olufemi Olorode, folorode@lsu.edu
