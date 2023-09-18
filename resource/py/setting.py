#-- codingutf-8 --

import pymysql

class setting():

    def setting(set_name):
        
        conn = pymysql.connect(host='192.168.120.85', user='user', password='VPsystem1234!!', db='vps_planner', charset='utf8', port=1980)   # 데이터 베이스 접속 내용을 conn 변수에 저장
        
        sql = "SELECT set_detail FROM psvsetting WHERE set_name = %s AND usage_status = 1"   # 데이터베이스 명령어를 spl 변수에 저장
        with conn.cursor() as cur:
            cur.execute(sql,(set_name))
            setting = cur.fetchone()[0]

        return setting

    # global lines

    # lines = open('\\\\192.168.120.85\\vps공유\\00. VP승인 프로그램모음\\13.개발프로그램\\로그\\psvsetting','r').readlines()
    
    # def qc_premonth():
        
    #     for line in lines:
            
    #         if line[0] == '#':
    #             pass
    #         else:
    #             line = line.replace('\n','').split(' ')
    #             if line[0] == 'qc_premonth':
                    
    #                 qc_premonth = line[2]

    #                 return qc_premonth
    
    # def update():
        
    #     for line in lines:
            
    #         if line[0] == '#':
    #             pass
    #         else:
    #             line = line.replace('\n','').split(' ')
    #             if line[0] == 'update':

    #                 update = line[2]

    #                 return update

    # def tomonth():
        
    #     for line in lines:
            
    #         if line[0] == '#':
    #             pass
    #         else:
    #             line = line.replace('\n','').split(' ')
    #             if line[0] == 'tomonth':

    #                 tomonth = line[2]

    #                 return tomonth
                
    # def premonth():
    
    #     for line in lines:
            
    #         if line[0] == '#':
    #             pass
    #         else:
    #             line = line.replace('\n','').split(' ')
    #             if line[0] == 'premonth':

    #                 premonth = line[2]

    #                 return premonth

    # def ip():

    #     for line in lines:
            
    #         if line[0] == '#':
    #             pass
    #         else:
    #             line = line.replace('\n','').split(' ')
    #             if line[0] == 'ip':

    #                 ip = line[2]

    #                 return ip
            
    # def password():
    
    #     for line in lines:
    #         if line[0] == '#':
    #             pass
    #         else:
    #             line = line.replace('\n','').split(' ')
    #             if line[0] == 'password':

    #                 password = line[2]

    #                 return password
            
    # def cutcorrection():
    
    #     for line in lines:
    #         if line[0] == '#':
    #             pass
    #         else:
    #             line = line.replace('\n','').split(' ')
    #             if line[0] == 'cutcorrection':

    #                 cutcorrection = line[2]

    #                 return cutcorrection