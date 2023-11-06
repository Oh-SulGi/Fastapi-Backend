def stock_price_now():
    import mojito
    import os
    from datetime import datetime
    import json
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

    path = 'D:\data\9월\mini_project\domain\create_data\data\code_list.text'
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()

    code_list = list(data.split('\n'))
    now = datetime.now()

    dict_ = {}
    for code in code_list:
        resp = broker.fetch_price(code)

        dict_[code] = {
            'code' : code,
            'price' : resp['output']['stck_prpr'],
            'date' : f'{now.date()}',
            'time' : f'{now.hour}:{now.minute}'
        }
    
    return dict_

    # path = 'D:\data\9월\mini_project\domain\create_data\data\stock_price_now.json'

    # with open(path, 'w', encoding='utf-8') as f:
    #     json.dump(dict_, f, ensure_ascii=False, indent=4)

print(stock_price_now())