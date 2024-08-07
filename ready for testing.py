import random
import pandas as pd
import os
import openpyxl

class job:
    def __init__(self, index, level, work_center, processing_time):
        self.index = index
        self.level = level
        self.work_center = work_center
        self.processing_time = processing_time
        self.children = []
        self.parents = []

def generate_random_tree(num_levels, max_children, num_jobs, num_work_centers, max_parents):
    num_levels += 1
    jobs = []
    start = job(index=1, level=1, work_center=1, processing_time=round(random.uniform(1, 10)))
    jobs.append(start)
    for level in range(1, num_levels):
        new_node = job(index=len(jobs)+1, level=level, work_center=random.randint(1, num_work_centers), processing_time=round(random.uniform(1, 10)))
        new_node.parents.append(level)
        jobs.append(new_node)
        jobs[level - 1].children.append(new_node)

    while len(jobs) < num_jobs-1:
        new_job = job(index=len(jobs)+1, level=random.randint(1, num_levels - 1), work_center=random.randint(1, num_work_centers), processing_time=round(random.uniform(1, 10)))
        #select all possible jobs which can be parent
        potential_parents = [job for job in jobs if len(job.children) < max_children]
        for x in potential_parents:
            if x.index == 1:
                potential_parents.remove(x)
        if not potential_parents:
            break  
        #select random parents
        num_parents = random.randint(1, min(max_parents, len(potential_parents)))
        selected_parents = random.sample(potential_parents, num_parents)
        for parent in selected_parents:
            parent.children.append(new_job)
            new_job.parents.append(parent.index)
        jobs.append(new_job)
    
    last_job = job(index=len(jobs)+1, level=num_levels, work_center=random.randint(1, num_work_centers), processing_time=0)
    
    tamen = [job.index for job in jobs if job.level == num_levels -1]
    last_job.parents.append(", ".join(map(str, tamen)))


    no_child = [job.index for job in jobs if job.children == []]
    if 13 in no_child:
        no_child.remove(13)
    last_job.parents.append(", ".join(map(str, no_child)))  

    jobs.append(last_job)
    return jobs

def convert_to_matrix(jobs):
    matrix = []
    for job in jobs:
        parents_str = ','.join(map(str, job.parents)) if job.parents!='' else ' '
        matrix.append([job.index, job.level, job.work_center, job.processing_time, parents_str])

    return matrix

def print_matrix(matrix):
    df = pd.DataFrame(matrix, columns=['Node Index', 'Level', 'Work Center', 'Processing Time', 'Predecessors'])
    del df['Work Center']
    this =  max(df['Predecessors'].apply(lambda x : len(x.split(','))))
    if this == max_parents:
        print(df)
    else:
        print_matrix

def save_matrix_to_csv(matrix, filename):
    df = pd.DataFrame(matrix, columns=['Node Index', 'Level', 'Work Center', 'Processing Time', 'Predecessors'])
    del df['Work Center']
    this =  max(df['Predecessors'].apply(lambda x : len(x.split(','))))
    if this == max_parents:
        pass
    #print(df)
    else:
        save_matrix_to_csv
    # df.to_csv(filename, index=False)
    df.to_excel(filename, sheet_name='Sheet1', index=False)



    

# num_levels = 4
# max_children = 3
# num_jobs = 8
# num_work_centers = 5
# max_parents = 3

num_levels = 9
max_parents = 9
num_jobs = 50


num_work_centers = 5
max_children = 100

random_tree = generate_random_tree(num_levels, max_children, num_jobs, num_work_centers, max_parents)
matrix = convert_to_matrix(random_tree)
save_matrix_to_csv(matrix, 'testing.xlsx')

random_tree = generate_random_tree(num_levels, max_children, num_jobs, num_work_centers, max_parents)
matrix = convert_to_matrix(random_tree)
save_matrix_to_csv(matrix, 'testing2.xlsx')

random_tree = generate_random_tree(num_levels, max_children, num_jobs, num_work_centers, max_parents)
matrix = convert_to_matrix(random_tree)
save_matrix_to_csv(matrix, 'testing3.xlsx')



