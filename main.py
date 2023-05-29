import sys
#import argparse


# Do not modify these lines
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Add your code after this line





    # TODO: read text from stdin
    
    # TODO: Filter character given as an argument from the text

    # TODO: Print the result to stdout

    # TODO: Print the total number of removed characters to stderr
def main():
    char = str(sys.argv[1])
    counter = 0

    records = sys.stdin.readlines()
    records_new = []
    for record in records:
        record_new = record.replace(char, "")
        records_new.append(record_new)
        counter += record.count(char)
    
    sys.stdout.writelines(records_new)
    sys.stderr.write(str(counter))


if __name__ == "__main__":
    main()
    

        

    

                   
            