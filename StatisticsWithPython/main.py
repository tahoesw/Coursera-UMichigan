# This is a sample Python script.

import pandas as pd

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
FILE_PATH = "/Users/wel51x/Box/MyBox/Courses/Coursera/UMich/StatisticsWithPython/data/"
FILE = "P_DEMO"
FILE = "P_BPXO"
FILE = "P_BMX"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Winston')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

df = pd.read_sas(FILE_PATH + FILE + '.XPT', index='SEQN')

print(df.shape)
print(df.columns)

#get first 3 rows
df1 = df.head(3)

#print the dataframe
#print(df1)
df.to_csv(FILE_PATH + FILE + '.csv')
