# import psycopg2
# conn = psycopg2.connect(dbname='albertastaduran', user='albertastaduran',
#                         password='mypassword', host='localhost')
# cursor = conn.cursor()
# def isint(s):
#     try:
#         int(s)
#         return True
#     except ValueError:
#         return False
# cursor.execute('SELECT name, price FROM product')
# name_price = cursor.fetchall()
# # name_price = sum(name_price,())
# # name_price = list(name_price)
# # name = []
# # prices = []
# # for value in name_price:
# #     if isint(value) :
# #         prices.append(value)
# #     else :
# #         name.append(value)
# # for n, row in enumerate(name):
# #     name[n] = row.replace('\n','')


# print(name_price)
# # print(prices)
def params(com,index):
    try:
        return com[index]
    except:
        return None

param = params(all,1)
print(param)