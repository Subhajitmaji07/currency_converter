import requests


class ConvertCurrency():
    def __init__(self):
        self.url= f'http://data.fixer.io/api/latest?access_key={"0dfce72579453e0489decb179a6c339f"}'
        self.rates=self.get_exchange_rates()

    def get_exchange_rates(self):
        response = requests.get(self.url)
        data = response.json()
        if 'rates' in data:
            return data['rates']
        else:
            raise Exception("Error fetching exchange rates")
        
    def convert(self,init_curr,target_curr,amount):
        if init_curr not in self.rates or target_curr not in self.rates:
            raise ValueError("Currency type does not Supported")
        
        #if init_curr !="USD":
        amount= amount / self.rates[init_curr]
        converted_amount = amount * self.rates[target_curr]
        return round(converted_amount, 2)
    
def main():
    c = ConvertCurrency() #creating an objet for ConvertCurrency class

    init_curr=input("Enter the initial Currecny: ").strip().upper()
    target_curr=input("Enter the target Currency: ").strip().upper()
    amount=float(input("Enter the amount:"))

    try:
        covnerted_amount=c.convert(init_curr,target_curr,amount)
        print(f"{amount} {init_curr} = {covnerted_amount} {target_curr}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occured: {e}")

if __name__=="__main__":
    main()

