# -*- coding: utf-8 -*-
"""
@author: 
    Meisam Adibifard
    PhD Student in Engineering Science
    Louisiana State University
"""

import numpy as np
import math
import csv
import argparse

class Molecule:
    def __init__(self,ro,rh1,rh2):
        # get loaction of each atom on water molecule
        self.o=ro;
        self.h1=rh1;
        self.h2=rh2;

def distance(r1,r2):
    dVect=np.array(r1)-np.array(r2);
    d=np.linalg.norm(dVect);
    return d;


def TorsionAngle(M1o,M1h,M2o,M2h):
    u1=np.array(M1o)-np.array(M1h);
    u2=np.array(M2o)-np.array(M1o);
    u3=np.array(M2h)-np.array(M2o);
    
    n1=np.cross(u1,u2);
    n2=np.cross(u2,u3);
    x=np.dot(u2,np.cross(n1,n2));
    y=np.linalg.norm(u2)*np.dot(n1,n2)

    theta=math.atan2(x,y); # returns theta in radians
    return theta;
    

# Read the .gro file
ps=argparse.ArgumentParser();
# Required args
ps.add_argument("--file","-i",type=str,required=True);
ps.add_argument("--WatModel","-wm",type=int,required=True);

# Optional args
ps.add_argument("--out","-o",type=str,required=False);
ps.add_argument("--WatSub","-ws",type=str,required=False);
ps.add_argument("--RHbond","-rh",type=float,required=False);
ps.add_argument("--timeInfo","-t",nargs='+', type=float,required=False);
ps.add_argument("--timeUnit","-tu", type=str,required=False);

args=ps.parse_args();


# Set default values
if bool(args.out) is False:
    args.out=args.file;
    args.out=args.out.replace("gro","csv") # (Default flie name for output csv)

if bool(args.RHbond) is False:
    args.RHbond=0.3; # in nm (Default value for dH)
    
if bool(args.WatSub) is False:
    args.WatSub="SOL"; # (Default string for water string)

# Set the number of atoms per water  molecule
nAtomPerWater=args.WatModel


# Get the input file
f4File=args.file;

gro_file=open(f4File,"r")

# Read line by line the GRo file
gro_list=gro_file.readlines()

# Count the numebr of time-steps
# 1st line is comment, 2nd line is the number of atomes, the last line is the coordinates of the box
# read number of atoms
numAtoms=int(gro_list[1])

# Assuming that the number of atoms do not change over time
NlinePerStep=numAtoms+3;

if len(gro_list)>NlinePerStep: # there are multiple time-steps
    NtimeSteps=int(len(gro_list)/NlinePerStep)
else:
    NtimeSteps=2;

water_Substr=args.WatSub;

# Set Hbond criteria
dH=args.RHbond; # in nm
F4avg=[];
x=[];
groTime=[];

for k in range(0,NtimeSteps-1):
    lbStep=NlinePerStep*(k);
    upStep=NlinePerStep*(k+1);
    nWat=0; 
    j=0;
    Water=[];
    if bool(args.timeInfo) is False:
        groTime.append(float(gro_list[lbStep].split()[-1]));
        
    for i in range(lbStep+2,upStep-2,nAtomPerWater): 
        line=gro_list[i].split();
        if water_Substr in line[0]:
            nWat+=1;
            ro=[float(line[3]),float(line[4]),float(line[5])];
            l2=gro_list[i+1].split();
            rh1=[float(l2[3]),float(l2[4]),float(l2[5])];
            l3=gro_list[i+2].split();
            rh2=[float(l3[3]),float(l3[4]),float(l3[5])];
            temp=Molecule(ro,rh1,rh2);
            Water.append(temp);
    # Find the H-bonded Molecules and determine the torsion angle
    Angles=[];
    F4=[];
    # save the indices of the neighboring h-bonded water molecules
    HbondNeigh=[];
    for i in range(0,len(Water)):
        a=[];
        for j in range(i+1,len(Water)):
            # Determine the distance between molecules
            do1o2=distance(Water[i].o,Water[j].o);
            if do1o2<=dH:
                a.append(j);
                d1=distance(Water[i].o,Water[j].h1);
                d2=distance(Water[i].o,Water[j].h2);
                d3=distance(Water[j].o,Water[i].h1);
                d4=distance(Water[j].o,Water[i].h2);
                # Now the molecules are hydrogen bonded
                if d1>d2: # Which means h2 is the outermost atom
                    wj_Hfar=Water[j].h1;
                else:
                    wj_Hfar=Water[j].h2;
                if d3>d4:
                    wi_Hfar=Water[i].h1;
                else:
                    wi_Hfar=Water[i].h2;
                # Calculate the torsion angle between H-bonded molecules
                theta=TorsionAngle(Water[i].o,wi_Hfar,Water[j].o,wj_Hfar);
                Angles.append(theta);
                F4.append(math.cos(3*theta));
        HbondNeigh.append(a);
    # Calculaet the average F4 order parameter
    F4avg.append(np.mean(F4));
    x.append(k);


# Dump the vectorized data (time,F4avg) into a .csv file
f4Fileoutput=args.out

if bool(args.timeInfo)==False:
    with open(f4Fileoutput,'w',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(["Time (user units)","F4"])
        for i in range(0,len(groTime)):
            writer.writerow([groTime[i],F4avg[i]])
else:
    dt=args.timeInfo[0]; # in fs
    dumpFreq=args.timeInfo[1];
    stride=args.timeInfo[2];
    fs2ms=1e-9;
    fs2ps=1e-3;
    fs2ns=1e-6;
    if args.timeUnit=="ns":
        conv=fs2ns;
    elif args.timeUnit=="ps":
        conv=fs2ps;
    elif args.timeUnit=="ms":
        conv=fs2ms;
    t=np.array(x)*dumpFreq*stride*conv*dt;
    
    with open(f4Fileoutput,'w',newline='') as file:
        writer=csv.writer(file)
        writer.writerow([f"Time ({args.timeUnit})","F4"])
        for i in range(0,len(t)):
            writer.writerow([t[i],F4avg[i]])
