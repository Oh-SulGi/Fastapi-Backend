def extract_stock_info():
    import mojito
    import os
    import json
    import pandas as pd
    from dotenv import load_dotenv
    load_dotenv()

    api_key = os.environ.get('APP_KEY')
    secret_key = os.environ.get('APP_SECRET_KEY')
    acc_no = os.environ.get('STOCK_ACCOUNT')

    broker = mojito.KoreaInvestment(
        api_key=api_key,
        api_secret=secret_key,
        acc_no=acc_no
    )

    kospi_symbols = broker.fetch_kospi_symbols()
    kosdaq_symbols = broker.fetch_kosdaq_symbols()
    list_ = [kospi_symbols, kosdaq_symbols]

    for i in range(len(list_)):
        df = pd.DataFrame(list_[i])
        df_json = df.to_dict(orient='records')
        df_json = sorted(df_json, key=lambda x: x['시가총액'])[::-1][:25]

        if i == 0:
            path = 'D:\data\9월\mini_project\data\kospi_top25.json'
        else:
            path = 'D:\data\9월\mini_project\data\kosdaq_top25.json'

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(df_json, f, ensure_ascii=False, indent=4)

def load_local_data():
    import json

    kospi_path = 'D:\data\9월\mini_project\data\kospi_top25.json'
    kosdaq_path = 'D:\data\9월\mini_project\data\kosdaq_top25.json'

    with open(kospi_path, 'r', encoding='utf-8') as f:
        data1 = json.load(f)
    with open(kosdaq_path, 'r', encoding='utf-8') as f:
        data2 = json.load(f)

    return data1, data2

def financial_data(code, year):
    import OpenDartReader
    import pandas as pd
    import os
    import json
    from dotenv import load_dotenv
    load_dotenv()

    dart_api_key = os.environ.get('DART_API_KEY')
    dart = OpenDartReader(dart_api_key)

    dart_df = pd.DataFrame(dart.finstate(code, year))
    dart_df_json = dart_df.to_dict(orient='records')

    dict_ = {
        dart_df_json[i]['account_nm'] : dart_df_json[i]['thstrm_amount'] for i in range(len(dart_df_json))
    }

    return dict_

def total_finantial_data(data):
    dict_ = {}
    for i in range(len(data)):
        dict2 = {}

        if data == kospi:
            try:
                for k, v in financial_data(str(data[i]['단축코드']), 2022).items():
                    dict2[k] = v

                dict_[i] = {
                    list(data[0].keys())[0] : data[i]['단축코드'],
                    list(data[0].keys())[2] : data[i]['한글명'],
                    list(data[0].keys())[list(data[0].keys()).index('시가총액')] : int(data[i]['시가총액']) * 100000000,
                    list(data[0].keys())[list(data[0].keys()).index('상장주수')] : int(data[i]['상장주수']) * 1000
                }
                dict_[i].update(dict2)
            except:
                dict_[i] = {
                    list(data[0].keys())[0] : data[i]['단축코드'],
                    list(data[0].keys())[2] : data[i]['한글명'],
                    list(data[0].keys())[list(data[0].keys()).index('시가총액')] : int(data[i]['시가총액']) * 100000000,
                    list(data[0].keys())[list(data[0].keys()).index('상장주수')] : int(data[i]['상장주수']) * 1000
                }
        else:
            try:
                for k, v in financial_data(str(data[i]['단축코드']), 2022).items():
                    dict2[k] = v

                dict_[i+50] = {
                    list(data[0].keys())[0] : data[i]['단축코드'],
                    list(data[0].keys())[2] : data[i]['한글명'],
                    list(data[0].keys())[list(data[0].keys()).index('시가총액')] : int(data[i]['시가총액']) * 100000000,
                    list(data[0].keys())[list(data[0].keys()).index('상장주수')] : int(data[i]['상장주수']) * 1000
                }
                dict_[i+50].update(dict2)
            except:
                dict_[i+50] = {
                    list(data[0].keys())[0] : data[i]['단축코드'],
                    list(data[0].keys())[2] : data[i]['한글명'],
                    list(data[0].keys())[list(data[0].keys()).index('시가총액')] : int(data[i]['시가총액']) * 100000000,
                    list(data[0].keys())[list(data[0].keys()).index('상장주수')] : int(data[i]['상장주수']) * 1000
                }

    return dict_

def save_local_total_data(dict1, dict2):
    import json
    
    dict1 = total_finantial_data(dict1)
    dict2 = total_finantial_data(dict2)
    dict1.update(dict2)

    # path = 'D:\data\9월\mini_project\data\stock_finance.json'
    path = 'C:\Users\user\Desktop\project\mini_project\domain\create_data\data\stock_info.json'

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(dict1, f, ensure_ascii=False, indent=4)

def save_code_list(dict1, dict2):
    code_list1 = [dict1[i]['단축코드'] for i in range(25)]
    code_list2 = [dict2[i]['단축코드'] for i in range(25)]
    code_list = code_list1 + code_list2

    # path = 'D:\data\9월\mini_project\data\code_list.text'
    path = 'C:\Users\user\Desktop\project\mini_project\domain\create_data\data\code_list.text'

    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(code_list))

extract_stock_info()
kospi, kosdaq = load_local_data()
save_code_list(kospi, kosdaq)
save_local_total_data(kospi, kosdaq)