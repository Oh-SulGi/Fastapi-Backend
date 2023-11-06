def stock_daily_price(date1, date2): 
    import FinanceDataReader as fdr
    import pandas as pd
    import json

    with open('D:\data\9월\mini_project\data\code_list.text', 'r', encoding='utf-8') as f:
        data = f.read()

    arr = data.split('\n')
    df = pd.DataFrame()

    for i in arr:
        df2 = fdr.DataReader(i, date1, date2)
        df2['code'] = i
        df = pd.concat([df, df2])
    
    df.reset_index(drop=False, inplace=True)
    df = df.drop('Change', axis=1)
    df['Date'] = df['Date'].astype(str)

    df_dict = df.to_dict(orient='records')

    path = 'D:\data\9월\mini_project\data\stock_daily_price.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(df_dict, f, ensure_ascii=False, indent=4)

stock_daily_price('2013-01-01', '2023-09-22')

