import os

def find_files(suffix, path):
    """
    Container method for the recursive method
    """ 
    
    # Edge cases
    if suffix == '' or suffix is None:
        print('Please provide valid suffix...')
        return
    elif path == '' or path is None:
        print('Source Directory cannot be Empty...')
        return
    elif not os.path.isdir(path):
        print('Source is not Directory, hence Cannot Proceed...')
        return
    else:
        files = find_files_recursive(suffix, path)
        
        if len(files) == 0:
            print('No files found, with matching criteria...')
            return
        
        # List is sorted
        files_ordered = sorted(list(files))
        for f in files_ordered:
            print(f)
        return
    
    return None

def find_files_recursive(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    # Used set so thatr we don't have duplicates
    file_set = set()
    for file in os.listdir(path):
        
        # In case the current file is a directory, then call this method
        # recursively
        if os.path.isdir(os.path.join(path, file)):
            find_files_recursive(suffix, os.path.join(path, file))
            
        # else let's find the files with a match    
        elif file[-len(suffix):] == suffix:
            file_set.add(os.path.join(path, file))
        
    return file_set

# Nothing exists with .c
find_files(".c", "./")

# Edge Cases
find_files("", "./")

find_files(".,", "")

# This returns some data
find_files(".py", "./")