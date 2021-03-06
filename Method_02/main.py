from utils import *

import uuid
import pprint

pp = pprint.PrettyPrinter(indent=4)

def main():
    continue_loop = True
    while continue_loop:
        print('1. Add node')
        print('2. Delete node')
        print('3. Fetch node path')
        print('4. Update node name')
        print('5. Print tree')
        print('0. EXIT')
        
        print('Choice : ', end='')
        choice_opted = int(input())
        
        if choice_opted == 0:           # break loop
            continue_loop = False

        elif choice_opted == 1:         # add folder
            print('Enter new Folder Name : ', end='')
            new_folder = str(input())
            print('Enter Path (eg : root/F1/F4/) : ', end='')
            path_ = str(input())
            path_list = list(filter(None, path_.split('/'))) # split path to  list of folders in the same order
            add_folder(new_folder,tree, path_list, str(uuid.uuid4()))

        elif choice_opted == 2:
            print('Enter Path (eg : root/F1/F4/) : ', end='')
            path_ = str(input())
            path_list = list(filter(None, path_.split('/')))
            delete_folder(tree, path_list)

        elif choice_opted == 3:
            print('Enter Node name: ', end='')
            node_name = str(input())
            get_address(tree, node_name, ['root'],[])

        elif choice_opted == 4:
            print('Enter Node Name (OLD): ', end='')
            node_name_old = str(input())
            print('Enter Node Name (NEW): ', end='')
            node_name_new = str(input())
            rename_node(tree, node_name_old, ['root'], node_name_new)


        elif choice_opted == 5:         # print full tree
            print('############################# TREE ##############################')
            pp.pprint(tree)
        else:
            print('you chose the wrong option')
            continue_loop=True
            

main()



    

