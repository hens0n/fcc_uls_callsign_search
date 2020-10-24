
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
        Print('Recent ULS Zip file located.')
        get_ULS_Zip()

    unzip_ULS('l_amat.zip')

def print_menu():
    print('FCC ULS Callsign Search')
    print(' 0: Exit')
    print(' 1: Search for Callsign')
    print(' 2: Process callsign_input.txt')
    print(' 3: SQL Query')
    print('')

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
            callsign_input = input("Callsign: ")
            cs = callsign.Callsign(callsign_input)
            rows = db.select_history(cs.callsign)
            for row in rows:
                print(row)
        if option == '2':
            output_file= open('callsign_output.txt','w')
            with open('callsign_input.txt', 'r') as reader:
                for line in reader.readlines():
                    # print(line + '>>>>>')
                    # output_file.write(select_callsign(db_con,line.upper().strip())+'\n')
        print()
        print()







    db.close_connection()

if __name__ == "__main__":
    main()