# FCC ULS Callsign Search

# Author
# Repostistory
# Callsign





import os
import time
from ftplib import FTP
from zipfile import ZipFile


import callsign
import database



# from pathlib import Path
# data_folder = Path("temp/")

# file_to_open = data_folder / "raw_data.txt"
# print(file_to_open)


def get_ULS_Zip():
    print('Downloading Zip')
    ftp = FTP('wirelessftp.fcc.gov')
    #ftp.login(user='username', passwd = 'password')
    ftp.login()
    ftp.cwd('/pub/uls/complete/')
    filename = 'l_amat.zip'
    localfile = open(filename, 'wb')

    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()
    print('Download complete')

def unzip_ULS(filename):
    if os.path.exists("l_amat.zip"):
        print('Unzipping file')
        with ZipFile(filename, 'r') as zipObj:
            zipObj.extractall('temp')
        print('Unzipping complete')

def ULSZipCheck():

    if os.path.exists("l_amat.zip"):
        file_modified = os.path.getmtime('l_amat.zip')
        current_time = time.time()
        time_difference = current_time - file_modified
        if time_difference > 604800: # 604800 one week in seconds
            get_ULS_Zip()
    else:
        print('ULS Zip file not found.')
        get_ULS_Zip()

    unzip_ULS('l_amat.zip')

def print_menu():
    print('FCC ULS Callsign Search')
    print(' 0: Exit')
    print(' 1: Search for Callsign')
    print(' 2: Process callsign_input.txt')
    # print(' 3: SQL Query')
    print('')

def search(db, input):
    rtn = ''
    cs = callsign.Callsign(input)
    rtn += 'Callsign: {}\n'.format(cs.callsign)
    rtn += '==================\n'
    rtn += 'Group: {}, Available To: {} \n\n'.format(cs.group,cs.available_to)

    amateur = db.select_amateur(cs.callsign)
    comments = db.select_comments(cs.callsign)
    entity = db.select_entity(cs.callsign)
    history = db.select_history(cs.callsign)

    if amateur:
        rtn += 'Amateur: \n'
        rtn += '------------------\n'
        rtn += amateur +'\n'
    if comments:
        rtn += 'Comments: \n'
        rtn += '------------------\n'
        rtn += comments +'\n'
    if entity:
        rtn += 'Entity: \n'
        rtn += '------------------\n'
        rtn += entity +'\n'
    if history:
        rtn += 'History: \n'
        rtn += '------------------\n'
        rtn += history +'\n'

    return rtn



def main():
    ULSZipCheck()
   
    db = database.ULSDatabase(':memory:','temp/')

    menu = True
    while menu is not False:
        print_menu()
        option = input("Option:")
        if option == '0':
            menu = False
        if option == '1':
            callsign_input = input("Callsign?: ")
            print()
            print()
            print(search(db,callsign_input))

        if option == '2':
            output_file= open('callsign_output.txt','w')
            with open('callsign_input.txt', 'r') as reader:
                for line in reader.readlines():
                    search_results = search(db,line.upper().strip())
                    print(search_results)
                    output_file.write(search_results)
            output_file.close()
                    # print(line + '>>>>>')
                    # output_file.write(select_callsign(db_con,line.upper().strip())+'\n')
        print()
        print()







    db.close_connection()

if __name__ == "__main__":
    main()