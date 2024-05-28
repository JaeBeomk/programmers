import pyupbit
import time

# 거래소 API 키 설정
# api_key = 'your_api_key'
# api_secret = 'your_api_secret'
# 간단히 암호화를 위해 일단 txt에다 숨김
with open("bit_key_info.txt") as f :
    lines = f.readlines()
    acc_key = lines[0].strip()
    sec_key = lines[1].strip()

# 업비트 객체 생성
upbit = pyupbit.Upbit(acc_key, sec_key)


# 기본 설정
symbol = 'KRW-BTC'  # 거래할 암호화폐 페어
amount = 0.001  # 거래할 수량 (BTC 단위)

# 잔고확인
def get_balance(ticker):
    balance = upbit.get_balance(ticker)
    return balance

print(get_balance("KRW"))  # 원화 잔고 확인

# 매수 및 매도
def buy_order(price):
    order = upbit.buy_market_order(symbol, price)
    return order

def sell_order(price):
    order = upbit.sell_market_order(symbol, price)
    return order

# 기본적인 이동평균선 전략
import pandas as pd

def get_ohlcv(symbol, interval='minute1', count=200):
    df = pyupbit.get_ohlcv(symbol, interval=interval, count=count)
    return df

def apply_strategy(df):
    df['ma50'] = df['close'].rolling(window=50).mean()
    df['ma200'] = df['close'].rolling(window=200).mean()

    if df['ma50'].iloc[-1] > df['ma200'].iloc[-1]:
        return 'buy'
    elif df['ma50'].iloc[-1] < df['ma200'].iloc[-1]:
        return 'sell'
    else:
        return 'hold'

# 무한 루프
while True:
    df = get_ohlcv(symbol)
    signal = apply_strategy(df)
    
    if signal == 'buy':
        krw_balance = get_balance("KRW")
        if krw_balance > 5000:  # 최소 주문 금액 이상일 때
            print("사자...")
            buy_order(krw_balance * 0.9995)  # 수수료를 감안한 금액으로 매수
    elif signal == 'sell':
        btc_balance = get_balance("BTC")
        if btc_balance > 0.00008:  # 최소 주문 수량 이상일 때
            print("팔자...")
            sell_order(btc_balance)
    else:
        print("대기...")

    time.sleep(60)  # 1분 대기
    print(get_balance("KRW"))
    
