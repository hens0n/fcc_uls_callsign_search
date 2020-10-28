import csv, sqlite3
# https://www.fcc.gov/wireless/data/public-access-files-database-downloads
# AM – Amateur
# CO - Comments
# EN – Entity
# HD - Application License/Header
# HS – History
# LA – License Attachment
# SC – License Level Canned Special Conditions
# SF – License Level Free Form Special Conditions


columns_am = 'record_type, unique_system_identifier,\
        uls_file_num,ebf_number,callsign,operator_class,group_code,\
        region_code,trustee_callsign,trustee_indicator,\
        physician_certification,ve_signature,systematic_callsign_change,\
        vanity_callsign_change,vanity_relationship,previous_callsign,\
        previous_operator_class,trustee_name'
columns_co ='record_type,unique_system_identifier,uls_file_num,callsign,\
        comment_date,description,status_code,status_date'
columns_en ='record_type,unique_system_identifier,uls_file_number,ebf_number,\
        call_sign,entity_type,licensee_id,entity_name,first_name,mi,last_name,\
        suffix,phone,fax,email,street_address,city,state,zip_code,po_box,\
        attention_line,sgin,frn,applicant_type_code,applicant_type_other,\
        status_code,status_date'
columns_hd = 'record_type,unique_system_identifier,uls_file_number,ebf_number,\
        call_sign,license_status,radio_service_code,grant_date,expired_date,\
        cancellation_date,eligibility_rule_num,applicant_type_code_reserved,alien,\
        alien_government,alien_corporation,alien_officer,alien_control,revoked,\
        convicted,adjudged,involved_reserved,common_carrier,non_common_carrier,\
        private_comm,fixed,mobile,radiolocation,satellite,developmental_or_sta,\
        interconnected_service,certifier_first_name,certifier_mi,certifier_last_name,\
        certifier_suffix,certifier_title,gender,african_american,native_american,\
        hawaiian,asian,white,ethnicity,effective_date,last_action_date,auction_id,\
        reg_stat_broad_serv,band_manager,type_serv_broad_serv,alien_ruling,\
        licensee_name_change'
columns_hs = 'record_type,unique_system_identifier,uls_file_number,callsign,\
    log_date,code'
columns_la = 'record_type,unique_system_identifier,callsign,attachment_code,\
        attachment_desc,attachment_date,attachment_filename,action_performed'
columns_sc = 'record_type,unique_system_identifier,uls_file_number,ebf_number,\
        callsign,special_condition_type,special_condition_code,status_code,\
        status_date'
columns_sf = 'record_type,unique_system_identifier,uls_file_number,ebf_number,\
        callsign,special_condition_type,special_condition_code,status_code,\
        status_date'


class ULSDatabase(object):
    """docstring for ULSDatabase"""
    def __init__(self, database,dat_file_path):
        super(ULSDatabase, self).__init__()
        self.db_connection = sqlite3.connect(database)
        self.dat_file_path = dat_file_path

        self.create_tables()
        self.ingest_dat_files()

    def close_connection(self):
        self.db_connection.close()
        
    def create_tables(self):
        self.create_table('AM', columns_am)
        self.create_table('CO', columns_co)
        self.create_table('EN', columns_en)
        self.create_table('HD', columns_hd)
        self.create_table('HS', columns_hs)
        self.create_table('LA', columns_la)
        self.create_table('SC', columns_sc)
        self.create_table('SF', columns_sf)

    def create_table(self,table_name,columns):
        db_cursor = self.db_connection.cursor()
        db_cursor.execute("CREATE TABLE "+table_name+" ("+columns+");") 

    def ingest_dat_files(self):
        print('Ingesting dat files')
        self.ingest_dat_file('AM.dat',columns_am,'AM')
        self.ingest_dat_file('CO.dat',columns_co,'CO')
        self.ingest_dat_file('EN.dat',columns_en,'EN')
        # self.ingest_dat_file('HD.dat',columns_hd,'HD')
        self.ingest_dat_file('HS.dat',columns_hs,'HS')
        # self.ingest_dat_file('LA.dat',columns_la,'LA')
        # self.ingest_dat_file('SC.dat',columns_sc,'SC')
        # self.ingest_dat_file('SF.dat',columns_sf,'SF')
        print('Ingesting dat files complete')

    def ingest_dat_file(self,dat_file,columns,table_name):
        
        db_cursor = self.db_connection.cursor()
        to_db = []
        column_count = len(columns.split(','))
        question_marks ='?,'*(column_count-1)
        question_marks += '?'
        with open(self.dat_file_path+dat_file,'r') as dat_file_object: # `with` statement available in 2.5+
            dr = csv.reader(dat_file_object,delimiter='|')
            
            for i in dr:
                if(len(i) == column_count):
                    to_db.append((i))
        
        db_cursor.executemany("INSERT INTO "+table_name+" ("+columns+") VALUES ("+question_marks+");", to_db)
        self.db_connection.commit()


    def select_amateur(self,callsign):
        db_cursor = self.db_connection.cursor()
        db_cursor.execute("Select operator_class,previous_callsign from AM "
            "WHERE callsign =?;", (callsign,))
        rows = db_cursor.fetchall()
        
        if(rows):
            rtn = ''
            for row in rows:
                rtn += 'Operator Class: {},Previous Callsign: {}\n'.format(row[0],row[1])
            return rtn
        else:
            return None


    def select_comments(self,callsign):
        db_cursor = self.db_connection.cursor()
        db_cursor.execute("Select comment_date,description from CO "
            "WHERE callsign =?;", (callsign,))
        rows = db_cursor.fetchall()
        
        if(rows):
            rtn = ''
            for row in rows:
                rtn += '{} Comment: {}\n'.format(row[0],row[1])
            return rtn
        else:
            return None


    def select_entity(self,callsign):
        db_cursor = self.db_connection.cursor()
        db_cursor.execute("Select entity_name,city,state,frn from EN "
            "WHERE call_sign =?;", (callsign,))
        rows = db_cursor.fetchall()
        
        if(rows):
            rtn = ''
            for row in rows:
                rtn += 'FRN: {}, Name:{}, {},{}\n'.format(row[3],row[0],row[1],row[2])
            return rtn
        else:
            return None


    def select_history(self,callsign):
        db_cursor = self.db_connection.cursor()
        # db_cursor.execute("SELECT callsign,log_date,code FROM HS WHERE callsign=?", (callsign,))
        db_cursor.execute("Select log_date,code,EN.entity_name,substr(log_date,7,4) "
            "||substr(log_date,1,2)||substr(log_date,4,2) as tdate from HS "
            "INNER JOIN EN ON EN.unique_system_identifier = HS.unique_system_identifier "
            "WHERE HS.callsign =? ORDER BY tdate DESC;", (callsign,))
        rows = db_cursor.fetchall()
        
        if(rows):
            rtn = ''
            for row in rows:
                rtn += '{} {}, {}\n'.format(row[0],row[1],row[2])
            return rtn
        else:
            return None

    

