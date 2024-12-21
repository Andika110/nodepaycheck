import requests

print(f'Check Eligible Nodepay Multiple Account')
print(f'By ADFMIDN | @ylasgamers')

def checkElig(token):
    try:
        # Define the API endpoint
        url = "https://api.nodepay.ai/api/season/airdrop-status?"
        
        # Define headers with the Bearer token
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'  # Set content type to JSON
        }
        
        # Send the Get request
        response = requests.get(url, headers=headers)
        is_eligible = response.json().get('data', {}).get('is_eligible')
        wallet = response.json().get('data', {}).get('wallet_address')
        season01 = response.json().get('data', {}).get('season1_tokens')
        season02 = response.json().get('data', {}).get('season2_tokens')
        if False == is_eligible:
            print(f'Sorry You Not Eligible!')
        else:
            print(f'Eligible : {is_eligible}')
            print(f'Wallet : {wallet}')
            print(f'Season 0 & 1 : {season01} Token')
            if None == season02:
                print(f'Season 2 TBD!')
                print(f'-------------------------------')
            else:
                print(f'Season 2 : {season02} Token')
                print(f'-------------------------------')
    except Exception as e:
        print(f"Error: {e}")
        pass

try:
   with open('token_list.txt', 'r') as file:
    local_data = file.read().splitlines()
    for token_list in local_data:
        checkElig(token_list)
except FileNotFoundError:
    print("Error: token_list.txt file not found.")
    pass