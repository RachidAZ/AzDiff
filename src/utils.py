from tabulate import tabulate
import textwrap
import csv




def print_with_color(string, color):
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        
    colorCode = bcolors.ENDC  # Default color code

    if color == "red":
        colorCode = bcolors.FAIL
    elif color == "yellow":
        colorCode = bcolors.WARNING
    elif color == "green":
        colorCode = bcolors.OKGREEN


    returnedString=colorCode + string + bcolors.ENDC
    return returnedString




def dict_to_csv(object1 : dict, object2 : dict, target: str):  
    # Specify the CSV file path
    csv_file_path = target
    header = ["Property", "Resource 1", "Resource 2"]

    # Write the dictionary to the CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')

        # Write the header
        csv_writer.writerow(header)

        # Write the data
        for key in object1.keys():            
            csv_writer.writerow([key, object1.get(key, '') , object2.get(key, '')])

    logging.info(f'Data written to {csv_file_path}')



def print_dict(object1, object2, terminal_width):
    # Transform dictionaries into a list of tuples
    properties_list = []

    for key in object1.keys():
        value1 = object1[key]
        value2 = object2[key]


        # todo: for dict value, print in lines
        if isinstance(value1, list) and isinstance(value2, list):
            # Join list values with a delimiter
            value1_str = ', \n '.join(map(str, value1))
            value2_str = ', \n'.join(map(str, value2))
        if isinstance(value1, dict) and isinstance(value2, list):
            value1_str=''
            value2_str=''
            for key, value in value1.items():
                value1_str=value1_str + "{key}: {value} \n"

            for key, value in value2.items():
                value2_str=value1_str + "{key}: {value} \n"

        else:
            value1_str = str(value1)
            value2_str = str(value2)

        if(value1_str != value2_str):
            value2_str=print_with_color("[?] ", "red" ) + value2_str

        width = terminal_width // 3            
        properties_list.append((key, textwrap.fill(value1_str, width=width) , textwrap.fill(value2_str, width=width)))

    
    # Print the properties using tabulate
    print(tabulate(properties_list, headers=["Property", "Resource 1", "Resource 2"], showindex="always" ,  tablefmt="grid", colalign=("left", "left", "left")))




    