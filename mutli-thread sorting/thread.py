import concurrent.futures
import threading
import time
import random
thread_local = threading.local()

def create_files(n_files):
    for i in range(n_files):
        file_name = 'f' + str(i)
        with open(file_name,'w') as f:
            for i in range (100):
                r = random.randint(1,1000)
                f.write(str(r)+'\n')

def sort_file(file_name):
    with open(file_name,'r') as f:
        nums = []
        raw_numbers = f.readlines()


    for i in range(len(raw_numbers)):
        nums.append(int(raw_numbers[i]))
    # Sort Numbers
    sorted_nums = sorted(nums)

    with open('sorted ' + file_name, "w") as f:
        for i in range(len(sorted_nums)):
            f.write(str(sorted_nums[i])+'\n')

def sort_files(n_files):
    file_names = []
    for i in range(n_files):
        file_names.append('f'+str(i))

    with concurrent.futures.ThreadPoolExecutor(max_workers=n_files) as executor:
        executor.map(sort_file, file_names)
        
if __name__ == "__main__":
    # Create files with random numbers
    n_files = 10
    create_files(n_files)

    start_time = time.time()
    sort_files(n_files)
    duration = time.time() - start_time
    print("sorted",n_files,"files in",duration,"seconds")