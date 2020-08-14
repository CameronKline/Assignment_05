#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (CKline, 8/11/20, 8:35PM Started Assignment)
# Change Log: (CKline, 8/12/20, 6:30AM Still Hacking)
# DBiesinger, 2030-Jan-01, Created File
#------------------------------------------#
# Pseudocode
# Ensure that lstTbl receives a dictionary instead of nested list
# Load existing data for 'l'
# Delete an entry for 'd' | Consider rewriting file to delete single option
import pprint
# -- DATA -- #
# Declare Variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data | be sure to make this a list of dicts
# TODO replace list of lists with list of dicts
dictRow = {}
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        lstTbl.clear() # Clear everything from table in memory
        objFile = open(strFileName, 'r') # Opens the txt file with permission to write
        for row in objFile: # Works through each row in the file
            lstRow = row.strip().split(',') # Split each row with a comma
            print(*lstRow) # Print the unpacked row
            lstTbl.append(lstRow) # Append the list of list with the information assigned to lstRow from file
        objFile.close() # Closes the file
        print(lstTbl)        
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        print()
        intID = int(strID)
        dictRow = {'id':intID, 'title':strTitle, 'artist':strArtist}
        lstTbl.append(dictRow) # Now a list of dicts
        for row in lstTbl:
            print('Added to Inventory')
            print('ID, CD Title, Artist')
            print('{} {} {}'.format(row['id'], row['artist'], row['title']))
            print()
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        # print(lstTbl, sep=', ')
        for row in lstTbl:
            print('Unpacking:', row)
            for key, val in row.items():
                print(key, val)
        print()

    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        strChoice = input('1 - Clear last\n2 - Clear all\n --> ')
        if strChoice == '1':
            lstRow.clear()
            print('Deleted last entry')
            print(lstRow)
        elif strChoice == '2':
            lstTbl.clear()
            print('Deleted all entries')
            # print(lstTbl)

    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        strRow = ''
        print(lstTbl)
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
        objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

