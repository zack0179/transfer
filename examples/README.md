# Example notebooks

## Getting started

### Basic setup

- cd into external and run the script "cd external && ./install"
- Source the script i.e  "source setup.bash(csh)"
- Create a workspace folder, e.g. "mkdir analyzes". This folder can be 
  created anywhere in your system. We surges to place it at the root of the repo
- cp any of the examples notebooks inside the work i.e "cp examples/xyz.ipynb analyzes"
- From the same terminal you sourced the setup.bash(csh), start jupyter
  i.e. "jupyter-notebook". The jupyter control panel will open in your browser
- Open the notebook that you just copy into the analyzes directory and execute the
  the cells
- You can also run the notebook without starting a jupyter server. From the commandline 
  you can run "run_notebook <name-of-notebook>.ipynb".  The script "run_notebook" 
  is inside the bin folder. All it does is to convert the notebook into python 
  script and run the script. This is useful for long MC runs.



