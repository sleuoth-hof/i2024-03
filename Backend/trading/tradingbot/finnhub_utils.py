# finnhub_utils.py
import finnhub

def get_stock_price(ticker):
    finnhub_client = finnhub.Client(api_key="cpk6guhr01qs6dmbtir0cpk6guhr01qs6dmbtirg")
    try:
        price = finnhub_client.quote(ticker)['c']
        return price
    except Exception as e:
        print(f"Error fetching price for {ticker}: {e}")
        return None



# from django_ratelimit.decorators import ratelimit

# @ratelimit(key='ip', rate='60/m')
# def get_stock_price(request, ticker):
#     try:
#         finnhub_client = finnhub.Client(api_key="cpk6guhr01qs6dmbtir0cpk6guhr01qs6dmbtirg")
#         price = finnhub_client.quote(ticker)['c']
#         return JsonResponse({'price': price})
#     except Ratelimited as e:
#         return JsonResponse({'error': 'Rate limit exceeded. Try again later.'}, status=429)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

