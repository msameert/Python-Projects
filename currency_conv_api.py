import requests


def currency_converter():
    print("--- Welcome to Currency Converter ---")
    base = input("Enter the Base Currency(USD, PKR) : ").upper()
    target = input("Enter your target currency : ").upper()
    amount = float(input("Enter Amount : "))


    # API Endpoint (free to use)
    api_key = "86d531b2c3bbd29e8aaac00d313f19c1"
    url = f"https://api.exchangerate.host/convert?access_key={api_key}&from={base}&to={target}&amount={amount}"
     

    try: 
        response = requests.get(url)
        data = response.json()

        if "result" in data and data["result"] is not None:
            converted = data["result"]
            print(f"\n {amount} {base} = {converted} {target}")
        else:
            print("Invalid Currency Code or API error ")
    
    except Exception as e:
        print("Error",e)

currency_converter()