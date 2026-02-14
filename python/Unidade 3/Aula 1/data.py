from datetime import datetime

def formatarData(data = datetime.now(), formato='%d/%m/%Y'):
    return datetime.strftime(data, formato)

def criarData(data, formato='%Y-%m-%d'):
    return datetime.strptime(data, formato)

# data = criarData ('2023-04-07')

# print(formatarData(data))

# print(datetime.strptime('2023-04-07', '%Y-%m-%d'))    
# data = datetime(1999, 4, 7)
# print(formatarData(data, "%m/%d/%Y"))
# print(formatarData(datetime.now(), "%m/%d/%Y"))