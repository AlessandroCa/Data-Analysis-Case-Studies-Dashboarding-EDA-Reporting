file_path = "Portafolio_Analytics/Project03_Telecom_Call_Data_Analysis_and_Billing/telefonate.csv"

def getCallData(file_name):
    with open(file_name, "r") as file:
        next(file)
        tuple_list = []
        for line in file:
            line = line.strip().replace("#", "")
            items = line.split(",")
            if len(items) < 6:
                continue
            tuple_line = (int(items[0]), int(items[1]), int(items[2]), int(items[3]), items[4], items[5])
            tuple_list.append(tuple_line)
        
    return tuple_list

tuple_list = getCallData(file_path)
for t in tuple_list:
    print(t)


