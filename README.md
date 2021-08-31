## f4OrderParameter
**version 1.00**
This repository contains the Python codes that determine the structural F4 order parameter from MD simulation results




### Prerequisites:
You need Python with the following packages installed:

* Numpy
* Math
* CSV
* Argparse


### Usage: 
Although the code can get many options via different commands, there are only two mandatory inputs for the code to work. First is the address of the .gro file and second is the type of the water model
(a 3-point or 4-point model). After moving to the folder where the f4time.py code exists, the basic command to run the code looks as below:

$ python f4time.py -i input.gro -wm <int>

The -i flag identifies the input .gro file to be processed by the Python code, and the -wm flag identifies the type of the water-model. The flag -wm can be fed either with an integer 3 or 4, where 3 
indicates the three-site water model arranged as OHH in the .gro file, while in the four-site water model the atoms of a water molecule are arranged as OHHM. Where m is the imaginary particle 




### Options:

-i  [<.gro>]      (input)

-wm <int>   (3 or 4)   (water model)

-out  [<.csv>]    (output)

-ws   <string>    (water substrate)

-rh   <float>      (nm)

-t    <float>  <float>  <float>   (time-step, dump frequency, stride)

-tu   <string>    (User defined time units)



#### Authors: 
### Meisam Adibifard, madibi1@lsu.edu, me.adibifard@gmail.com

#### PI:
### Olufemi Olorode, folorode@lsu.edu