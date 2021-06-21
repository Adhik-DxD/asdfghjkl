import requests
import json
import argparse, time

parser = argparse.ArgumentParser(description='Get Manga-IDs for MangaDex.')
parser.add_argument('-n', type=str, dest='query', required=True, action='store', help='Title of the Manga')
args = parser.parse_args()

title = args.query
print('\nQuery: ',title)

a = requests.get("https://api.mangadex.org/manga/?limit=25&offset=0&title={}".format(title))
data = a.json()

alts = len(data['results'])
if alts <=10:
	times = alts
else:
	times = 10
print(f'{times} results')

for i in range(times):
	ID = data['results'][i]['data']['id']
	Tit = data['results'][i]['data']['attributes']['title']['en']
	Chs = data['results'][i]['data']['attributes']['lastChapter']
	print(f'---\n{i+1}:{Tit}\nID:\"{ID}\"\nLatest_chapter:\"{Chs}"')


