import os
import asyncio
from datetime import datetime, timedelta
from pprint import pprint
from dateutil.relativedelta import relativedelta
import pandas as pd
from cryptocompare import cryptocompare
from utils import percent_calc, str2datetime
import ccxt.async_support as ccxt


def get_historical_price(crypto_name="BTC",
                         start=datetime.now() - relativedelta(months=6),
                         end=datetime.now(),
                         currency="JPY",
                         cache_path="cache"):
    limit = (end - start).days * 24
    fn = os.path.join(cache_path, f"{crypto_name}_{currency}_{start.date()}_{end.date()}.csv")
    if os.path.exists(fn):
        df = pd.read_csv(fn)
        return df

    if not os.path.exists(cache_path):
        os.makedirs(cache_path)

    values = []
    while limit > 0:
        amount = min(1920, limit)
        tmp = cryptocompare.get_historical_price_hour(coin=crypto_name, currency=currency, limit=amount, toTs=end)
        end -= timedelta(hours=amount)
        limit -= amount
        values.extend(tmp)

    df = pd.DataFrame(values)
    df.sort_values("time", inplace=True)
    df.drop_duplicates(subset="time", inplace=True)

    df["perc_val"] = df.apply(lambda row: percent_calc(row["close"], row["open"]), axis=1)
    df["price"] = df["close"]
    df.to_csv(fn, index=False)
    return df


async def fetch_ticker(exchange, symbol):
    try:
        result = await exchange.fetch_ticker(symbol)
        return result
    except ccxt.BaseError as e:
        print(type(e).__name__, str(e), str(e.args))
        raise e


async def get_ticker(crypto_name="BTC", currency="JPY", exchange_id="bitbank"):
    if not exchange_id in ccxt.exchanges:
        raise ValueError(f"Exchange not supported: {exchange_id}")

    symbol = f"{crypto_name}/{currency}"
    exchange = getattr(ccxt, exchange_id)({
        'enableRateLimit': True,
    })
    await exchange.load_markets()
    ticker = await fetch_ticker(exchange, symbol)
    return ticker


def get_ohlcv(crypto_name="BTC", currency="JPY", exchange_id="bitbank"):
    import ccxt
    if not exchange_id in ccxt.exchanges:
        raise ValueError(f"Exchange not supported: {exchange_id}")

    symbol = f"{crypto_name}/{currency}"
    exchange = getattr(ccxt, exchange_id)({
        'enableRateLimit': True,
    })
    exchange.load_markets()
    result = exchange.fetch_ohlcv(symbol, timeframe='1h')
    return result


def test():
    pattern_file = "./input/market_patterns.csv"
    # simulation_result_base = "simulations"
    # result_file = os.path.join(simulation_result_base, f"result_{datetime.now().strftime('%Y%m%d%H%M%S')}.xlsx")

    df_pattern = pd.read_csv(pattern_file)
    df_pattern = str2datetime(df_pattern)

    for i, row in df_pattern.iterrows():
        id_ = row["id_"]
        crypto_name = row["crypto_name"]
        start = row["start"]
        end = row["end"]

        get_historical_price(crypto_name=crypto_name,
                             start=start,
                             end=end,
                             currency="USD")


def test_ccxt():
    results = asyncio.get_event_loop().run_until_complete(get_ohlcv())
    pprint(results)


if __name__ == '__main__':
    # test()
    test_ccxt()
