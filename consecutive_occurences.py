from collections import defaultdict

def consecutive_occurences(word):
	letters=defaultdict(int)
	temp = word[0]
	c=1
	for char in word[1:]:
		if char== temp:
			c+=1
			continue
		else:
			letters[temp]=max(c,letters[temp])
			c=1
			temp=char
	letters[temp]=c
	sorted_letters=sorted(letters.items(), key=lambda x:x[1], reverse= True)
	for letter, value in sorted_letters[:3]:
		print(f'{letter},{value}')

consecutive_occurences('aaabbccaddde')