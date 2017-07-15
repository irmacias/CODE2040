import requests
import json
import iso8601
from datetime import timedelta

# Variables to be used.

token = 'b4ee4ec5ebaf77cf5c7b43c03d5e39b1'
github = "https://github.com/irmacias/CODE2040"


# Step 1: Registration

def registration(token, github):
    payload = {'token': token, 'github': github}
    r = requests.post('http://challenge.code2040.org/api/register', json=payload)
    return r.text

print (registration(token, github))


# Step 2: Reverse a String

def string_reverse(token):
    payload = {'token': token}
    r = requests.post('http://challenge.code2040.org/api/reverse/', json=payload)
    new_string = ''.join(reversed(r.text))
    payload_2 = {'token': token, "string": new_string}
    new_r = requests.post('http://challenge.code2040.org/api/reverse/validate', json=payload_2)
    return new_r.text

# Simple string reverse, nothing too fancy
print (string_reverse(token))


# Step 3: Needle in a haystack

def needle_in_haystack(token):
    payload = {'token': token}
    r = requests.post('http://challenge.code2040.org/api/haystack', json=payload)
    needle = json.loads(r.text)['needle']
    location = None
    for index, potential_needles in enumerate(json.loads(r.text)['haystack']):
        if potential_needles == needle:
            location = index
    payload_2 = {'token': token, 'needle': location}
    new_r = requests.post('http://challenge.code2040.org/api/haystack/validate', json=payload_2)
    return new_r.text

# Also somewhat straight-forward for loop
print (needle_in_haystack(token))


# Step 4: Prefix

def prefix(token):
    payload = {'token': token}
    r = requests.post('http://challenge.code2040.org/api/prefix', json=payload)
    prefix = json.loads(r.text)["prefix"]
    array = json.loads(r.text)["array"]
    new_array = []
    for string in array:
        if not string.startswith(prefix):
            new_array.append(string)
    payload_2 = {'token': token, 'array': new_array}
    new_r = requests.post('http://challenge.code2040.org/api/prefix/validate', json=payload_2)
    return new_r.text


print (prefix(token))


# Step 5: The dating game

def the_dating_game(token):
    payload = {'token': token}
    r = requests.post('http://challenge.code2040.org/api/dating', json=payload)
    datestamp = json.loads(r.text)["datestamp"]
    interval = timedelta(seconds=json.loads(r.text)["interval"])
    new_date = interval + iso8601.parse_date(datestamp)
    new_date = new_date.strftime('%Y-%m-%dT%H:%M:%SZ')
    payload_2 = {"token": token, "datestamp": new_date}
    new_r = requests.post('http://challenge.code2040.org/api/dating/validate', json=payload_2)
    return new_r.text


print (the_dating_game(token))

