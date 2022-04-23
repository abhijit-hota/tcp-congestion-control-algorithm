## Simulation of the TCP Congestion Control Algorithm

----

## File Structure
This repository consists of 4 Python files:

- **`myctcp.py`**  
    This is the entry point for the simulator CLI application. The program accepts a number of parameters, calls the required functions that handle the simulation and outputs a graph of the congestion windows vs. sequence numbers. The detailed usage and options are [given below](#usage).

    [`argparse`](https://docs.python.org/3/library/argparse.html) from the standard library is used to parse and document the arguments. 

- **`core.py`**  
  This file consists of one function called `simulate` which is contains the actual simulation code. The `simulate` function takes all the parameters which are required for the simulation and returns a sequential list of congestion windows to be used for plotting or logging.
  
  The algorithm is documented in the form of comments.

- **`utils.py`**   
  This file contains a helper function that take the congestion window values as input and outputs a graph and writes them to a file.

  It also contains a helper class which basically adds abstraction and typings for the options to be passed around.
  
- **`simulate_from_parameters.py`**  
  This file is an independent file which calls the `simulate` function with all the different variables mentioned in the problem statement and outputs log and image files to a `figures` folder.

## Usage

- **`mytcp.py`**

    ```
    usage: python mytcp.py [-h] [-i Ki] [-m Km] [-n Kn] -f Kf -s Ps -T Total
                           [-o Output filename]

    Simulates an MIAD TCP congestion control algorithm based on input parameters
    as stated below.

    optional arguments:
      -h, --help          show this help message and exit
      -i Ki               (1.0 ≤ Ki ≤ 4.0) Initial congestion window (CW). Default
                          = 1
      -m Km               (0.5 ≤ Km ≤ 2.0) Multiplier of the congestion window,
                          during the exponential growth phase. Default = 1
      -n Kn               (0.5 ≤ Kn ≤ 2.0) Multiplier of the congestion window,
                          during the linear growth phase. Default = 1
      -f Kf               (0.1 ≤ Kf ≤ 0.5) Multiplier when a timeout occurs
      -s Ps               (0.0 < Ps < 1.0) Probability of receiving the ACK packet
                          for a given segment before its timeout occurs.
      -T Total            Total number of segments to be sent before the emulation
                          stops
      -o Output filename  The file name to output the results to.

    The program generates 2 outputs — the image of the graph with the default name
    'out.svg' and a text file containing all the congestion window values
    separated by newlines with the default name 'out.log'. The name, 'out', can be
    changed by the option '-o' as mentioned.
    ```
- **`simulate_from_parameters.py`**
  ```sh
  python simulate_from_parameters.py <T>
  ```
  where T is a optional argument which denotes the number of segments. Its 1000 by default.

## Report 

The report analyzing the factors responsible for the graphs can be found as `CE19B033_Assgn4_Report.pdf`.

---- 

**Abhijit Hota**  
**CE19B033**
