## f4OrderParameter
**version 1.00**

This repository contains the Python codes that determine the structural F4 order parameter from MD simulation results




### Prerequisites:
You need Python with the following packages installed:

* Numpy
* Math
* CSV
* Argparse

<span class="icon icon-device-desktop"></span>

### Usage:
Although the code can get many options via different commands, there are only two mandatory inputs for the code to work. First is the address of the .gro file and second is the type of the water model
(a 3-point or 4-point model). After moving to the folder where the f4time.py code exists, the basic command to run the code looks as below:

$ python f4time.py -i input.gro -wm (3 or 4)

The -i flag identifies the input .gro file to be processed by the Python code, and the -wm flag identifies the type of the water-model. The flag -wm can be fed either with an integer 3 or 4, where 3
indicates the three-site water model arranged as OHH in the .gro file, while in the four-site water model the atoms of a water molecule are arranged as OHHM. Where m is the imaginary particle



---------------------------------------------------------------------------------------------------------------------
### Options:

-i  [<.gro>]      (input)
 the .gro trajectory file

-wm <int>   (3 or 4)   (water model)
 the type of the water model (3-point or 4-point model)

-out  [<.csv>]    (output)
 the output [t,F4] data saved as a .csv file. If not assigned, a .csv file will be created with its name duplicated form the input .gro file.

-ws   <string>    (water substrate)
 the name of the water substrate in the .gro file, default="SOL"

-rh   <float>      (nm)
 the threshold radius for hydrogen-bonded molecules

-t    <float>  <float>  <float>   (time-step (fs), dump frequency, stride)
 If this command is ignored, then the code reads the time data from the input .gro file. On the other hand, if user opts to use this flag, he or she needs to provide the time-step, the dumping frequency, and the stride used to generate the .gro trajectory file.
 This is suited well for the .gro files that are exported from VMD but lack time information. The time-step can be found in the simulation data file, the "dump frequency" is also found in the input file to the simulator and indicates the number of time-steps before dumping the trajectory of the atoms, the stride is another filter to the dumped data and is accessible when the user exports the .gro file using VMD.

-tu   <string>    (User defined time units)
 This flag is optional unless you opt to use the flag "-t". Thus, this flag is only required in conjunction with the "-t" flag.


#### Authors:
### Meisam Adibifard, madibi1@lsu.edu, me.adibifard@gmail.com

#### PI:
### Olufemi Olorode, folorode@lsu.edu
