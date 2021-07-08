import requests        
"""
Replace the value of Vikarna in below URL with your favourite Author or Genre or Book title.
The API will pull out all the books that matches the input you gave.
This would enable all you Bibliophile to never Readgret(Google the word if you are not familiar :P) again in life.
"""
def api_call():
    headers = {'User-Agent': 'joker'}
    response = requests.get("https://www.googleapis.com/books/v1/volumes?q=vikarna", headers=headers)
    response.raise_for_status()
    return response.json()


reply = api_call()
items = reply.get('items')
for item in items:
	volumeInfo = item.get('volumeInfo')
	previewLink = volumeInfo.get('previewLink')
	title = volumeInfo.get('title')
	authors = volumeInfo.get('authors')
	description = volumeInfo.get('description')
	print ('***********************')
	print ('Book Title: %s' % (title))
	print ('Book Description: %s' % (description))
	print ('Book Preview: %s' % (previewLink))	
	print ('***********************')
