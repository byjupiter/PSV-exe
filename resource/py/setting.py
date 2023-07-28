#-- codingutf-8 --

class setting():

    global lines

    lines = open('\\\\192.168.120.85\\vps공유\\00. VP승인 프로그램모음\\13.개발프로그램\\로그\\psvsetting','r').readlines()
    
    def update():
        
        for line in lines:
            
            if line[0] == '#':
                pass
            else:
                line = line.replace('\n','').split(' ')
                if line[0] == 'update':

                    update = line[2]

                    return update

    def tomonth():
        
        for line in lines:
            
            if line[0] == '#':
                pass
            else:
                line = line.replace('\n','').split(' ')
                if line[0] == 'tomonth':

                    tomonth = line[2]

                    return tomonth
                
    def premonth():
    
        for line in lines:
            
            if line[0] == '#':
                pass
            else:
                line = line.replace('\n','').split(' ')
                if line[0] == 'premonth':

                    premonth = line[2]

                    return premonth

    def ip():

        for line in lines:
            
            if line[0] == '#':
                pass
            else:
                line = line.replace('\n','').split(' ')
                if line[0] == 'ip':

                    ip = line[2]

                    return ip
            
    def password():
    
        for line in lines:
            if line[0] == '#':
                pass
            else:
                line = line.replace('\n','').split(' ')
                if line[0] == 'password':

                    password = line[2]

                    return password
            
    def cutcorrection():
    
        for line in lines:
            if line[0] == '#':
                pass
            else:
                line = line.replace('\n','').split(' ')
                if line[0] == 'cutcorrection':

                    cutcorrection = line[2]

                    return cutcorrection
        
