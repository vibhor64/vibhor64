# Your imports go here
import logging
import json

logger = logging.getLogger(__name__)

'''
    Given a directory with receipt file and OCR output, this function should extract the amount

    Parameters:
    dirpath (str): directory path containing receipt and ocr output

    Returns:
    float: returns the extracted amount

'''
def extract_amount(dirpath: str) -> float:
    f = open(f'{dirpath}\\ocr.json',)
    data = json.load(f)
    logger.info('extract_amount called for dir %s', dirpath)
    length = (len(data['Blocks']))
    cash = []
    method = 0
    for i in range(0, length):
        for item in data['Blocks'][i]:
            # print(i)
            if item == 'Text':
                if data['Blocks'][i]['Text'] == 'TOTAL' or data['Blocks'][i]['Text'] == 'Total' or data['Blocks'][i]['Text'] == 'CREDIT' or data['Blocks'][i]['Text'] == 'Total :' or data['Blocks'][i]['Text'] == 'USD' or data['Blocks'][i]['Text'] == 'AMOUNT' or data['Blocks'][i]['Text'] == '$' or data['Blocks'][i]['Text'] == 'Payment' or data['Blocks'][i]['Text'] == 'PAYMENTS':
                    i = i + 1
                    amount = data['Blocks'][i]['Text']
                    # print('here')
                    # print(amount)
                    amount1 = 0
                    try:
                        list1=[]
                        list1[:0]=amount
                        if list1[0] == '$':
                            list1.pop(0)
                        str1 = ""   
                        # print(list1)
                        for ele in list1: 
                            # str1 = ""  
                            str1 += ele 
                        # print(str1)
                        amount = str1 
                        amount1 = float(amount)
                        # cash.append(amount1)
                    except Exception as e:
                        # print(e)
                        break
                    cash.append(amount1)
                    # print(amount1)
                    # print(i)
                    # print(data['Blocks'][i]['Text'])
                    # print(type(amount))
                    # method = 1
                    # return
    for i in range(0, length):
        if method == 0:            
            for item in data['Blocks'][i]:
                if item == 'Text':
                    # print(i)
                    if 'AMOUNT PAID : ' in data['Blocks'][i]['Text']:
                        amount = (data['Blocks'][i]['Text'])
                        list1= []
                        list1[:0]=amount
                        newlist = list1[15:]
                        list1.pop(15)
                        str1 = ""
                        amount2 = 0
                        for ele in newlist: 
                            str1 += ele 
                        amount = str1 

                        try:
                            list1=[]
                            list1[:0]=amount
                            if list1[0] == '$':
                                list1.pop(0)
                            str1 = ""  
                            for ele in list1: 
                                str1 += ele 
                            amount = str1 
                            amount2 = float(amount)
                        except Exception:
                            break
                        
                        
                        cash.append(amount2)
                        # print(amount2)
                        # method = 1
                        # return

    for i in range(0, length):
        if method == 0:            
            for item in data['Blocks'][i]:
                if item == 'Text':
                    asw = data['Blocks'][i]['Text']
                    list1=[]
                    list1[:0]= asw
                        # if list1[0] == '$':
                    # print(list1)
                    if list1[0] == '$':
                        # i = i + 1
                        # print(list1)
                        try:
                            if (data['Blocks'][i+1]['Text']) == 'weekly' or (data['Blocks'][i+1]['Text']) == 'daily':
                                break
                        except Exception:
                            pass
                        amount = (data['Blocks'][i]['Text'])
                        amount3 = 0
                        # print(amount)
                        try:
                            if list1[0] == '$':
                                list1.pop(0)
                            if ',' in list1:
                                list1.remove(',')
                            str1 = ""  
                            # print(list1)
                            for ele in list1: 
                                str1 += ele 
                            amount = str1 
                            amount3 = float(amount)
                        except Exception:
                            break
                        # print(list1)

                        cash.append(amount3)
                        # method = 1
                        # return

    if len(cash) != 0:
        price = max(cash)
        return price
    elif len(cash) == 0:
        return 0

# For testing this module, uncomment the following command below and keep chaning the receipt number in dirpath
# dirpath = './data\\receipt2'
# extracted_amount = extract_amount(dirpath)
# print(extracted_amount)