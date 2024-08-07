# Operations Scheduling 

**Julia Code for ESA and MSO Project**  
Using Gurobi optimiser to create a small dimension (<50 jobs) operations scheduling optimiser. 

- inputs:
    
    - variables:
        - Job id 
        - Job name 
        - Job duration 
        - Number of jobs 
        - Job predecessor-successor pairs 
        - Number of work centers  
        - Number of machines 
        - Final job(s) id (otherwise assumed to be last job) 
        - Due date for final job(s) 
- outputs:
    - Gantt chart  
        - Start and end times of each job and machine assignment 
    - Bar chart 
        - Distribution of machine assignment

This code is designed to take in two types of input files, applied use cases and test cases. Applied use cases tend to be more linear in nature,  and contain more details such as job names and specific machinery, in addition, there might be long processing times (in days/months). Test case data is used to explore the extreme cases of the scheduling program, it often has more complex input BOM trees, but smaller and more uniform processing times.

Use case notes: the time frame of the scheduler inherently has no units, thus it can be adapted as needed for short/long processes.

Note on files in this folder:  
*'ready for testing.py'* -> this file is used to create test data, using a specified m, n and number of jobs.
*'final_code.ipynb'* -> this file is run in Julia version 1.1, using Gurobi Academic License  
*'pressure_tank.xlsx'* -> data file containing the BOM for a real use case, data sourced by our group.  
*'testing.xlsx'* -> test case example, produced by the *'ready for testing.py'* file. This is a 9x9 BOM with 50 jobs.
*'BOM combined.xlsx'* -> integration with GROUP 4's BOM, using randomised duration times.  
*'LETSA Hueristic model.ipynb'* -> check against LETSA heuristic to determine accuracy and optimality of Julia MILP




**ES02 Group 5**  
