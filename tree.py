import os


def walk(dirname, logging_file):
    #list all items in directory
    items = os.listdir(dirname)
    
    #check every item to see if its path is a file (dead end) or a directory
    for item in items:
        path = os.path.join(dirname, item)

        #if path is a file it ends and wrights to file
        if os.path.isfile(path):
            logging_file.write(path+"\n")

        #else path is another directory enter the directory recursively
        else:
            walk(path, logging_file)


if __name__ == '__main__':
    #selecting file to log to
    with open("TEST_log.txt", "w") as logging_file:
        #selecting directory to start scaning
        walk(".", logging_file)
