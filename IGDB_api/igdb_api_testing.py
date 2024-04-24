from requests import post
response = post('https://api.igdb.com/v4/franchises', **{'headers': {'Client-ID': 'Client ID', 'Authorization': 'Bearer access_token'},'data': 'fields checksum,created_at,games,name,slug,updated_at,url;'})
print ("response: %s" % str(response.json()))
