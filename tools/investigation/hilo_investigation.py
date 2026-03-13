import requests

API_KEY = "JX559XE9VY3DPWWEATUIZURQQ4ZG138VF3"
# V2 endpoint
BASE = "https://api.etherscan.io/v2/api?chainid=1"

# HILO token contract (من CMC)
HILO_CA = "0x6c3fe25a4de7fa243c653cfe1f165bf11d99704e"  # تحقق من CA الفعلي

TARGETS = {
    "HILO_Uniswap_V3_Pool": "0xa6d6bdb66131b45c61a54d47f096ec036428fc0d",
    "HILO_Uniswap_V2_Pool": "0xf7ae6612c56de3f52095731bdffeb22e64de70dd",
    "Binance_Deposit": "0x318b9a4e5d13f41759652604d30c87694b1ee1ae",
}

def query(params):
    params['apikey'] = API_KEY
    r = requests.get(BASE, params=params)
    return r.json()

def check(label, address):
    print(f"\n{'='*55}")
    print(f"[TARGET] {label}")
    print(f"[ADDR]   {address}")

    # ETH balance
    d = query({'module':'account','action':'balance','address':address,'tag':'latest'})
    if d['status'] == '1':
        eth = int(d['result']) / 10**18
        print(f"[ETH]    {eth:.6f} ETH")

    # Token transfers (آخر 20)
    d2 = query({'module':'account','action':'tokentx','address':address,
                'page':'1','offset':'20','sort':'desc'})
    if d2['status'] == '1':
        txs = d2['result']
        print(f"[TOKEN TX] {len(txs)} تحويل token مؤخراً:")
        seen_tokens = {}
        for tx in txs:
            sym = tx.get('tokenSymbol','?')
            dec = int(tx.get('tokenDecimal', 18))
            val = int(tx['value']) / 10**dec
            seen_tokens[sym] = seen_tokens.get(sym, 0) + val
        for sym, total in seen_tokens.items():
            print(f"  → {sym}: {total:,.2f} total volume")

        # طباعة أكبر 5 تحويلات
        print("\n  أكبر 5 تحويلات:")
        sorted_txs = sorted(txs, key=lambda x: int(x['value']), reverse=True)[:5]
        for tx in sorted_txs:
            dec = int(tx.get('tokenDecimal', 18))
            val = int(tx['value']) / 10**dec
            sym = tx.get('tokenSymbol','?')
            d_type = "OUT" if tx['from'].lower()==address.lower() else "IN "
            print(f"  {d_type} {val:>12,.2f} {sym} | {tx['hash'][:20]}...")
    else:
        print(f"[!] {d2.get('message','no data')}")

    # Normal TXs
    d3 = query({'module':'account','action':'txlist','address':address,
                'page':'1','offset':'5','sort':'desc'})
    if d3['status'] == '1':
        print(f"\n[NORMAL TX] آخر {len(d3['result'])} عملية ETH:")
        for tx in d3['result']:
            val = int(tx['value']) / 10**18
            d_type = "OUT" if tx['from'].lower()==address.lower() else "IN "
            print(f"  {d_type} {val:.6f} ETH | block {tx['blockNumber']}")

for label, addr in TARGETS.items():
    check(label, addr)

print("\n\n[DONE] تحقق من HILO token contract address على CoinMarketCap للتأكد")
