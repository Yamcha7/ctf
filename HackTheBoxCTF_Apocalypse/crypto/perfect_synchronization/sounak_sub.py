import collections
f = open("real_output.txt","r")
l = [x for x in f.read().splitlines()]
d = dict(collections.Counter(l))
s = ''
for x in l:
	if x == 'fbe86a428051747607a35b44b1a3e9e9':
		s+='{'
	elif x == 'c53ba24fbbe9e3dbdd6062b3aab7ed1a':
		s+='}'
	elif x == '61331054d82aeec9a20416759766d9d5':
		s+=' '
	elif x == '3a17ebebf2bad9aa0dd75b37a58fe6ea':
		s+='H'
	elif x == '68d763bc4c7a9b0da3828e0b77b08b64':
		s+='T'
	elif x == '9673dbe632859fa33b8a79d6a3e3fe30':
		s+='B'
	elif x == 'c87a7eb9283e59571ad0cb0c89a74379':
		s+='E'
	elif x == '5f122076e17398b7e21d1762a61e2e0a':
		s+='A'
	elif x == '8cbd4cfebc9ddf583a108de1a69df088':
		s+='O'
	elif x == '200ecd2657df0197f202f258b45038d8':
		s+='S'
	elif x == '34ece5ff054feccc5dabe9ae90438f9d':
		s+='N'
	elif x == 'f89f2719fb2814d9ab821316dae9862f':
		s+='L'
	elif x == '305d4649e3cb097fb094f8f45abbf0dc':
		s+='R'
	elif x == 'e23c1323abc1fc41331b9cdfc40d5856':
		s+='D'
	elif x == '4a3af0b7397584c4d450c6f7e83076aa':
		s+='M'
	elif x == '66975492b6a53cc9a4503c3a1295b6a7':
		s+='W'
	elif x == 'e9b131ab270c54bbf67fb4bd9c8e3177':
		s+='I'
	elif x == '5d7185a6823ab4fc73f3ea33669a7bae':
		s+='Y'
	elif x == '457165130940ceac01160ac0ff924d86':
		s+='C'
	elif x == 'd178fac67ec4e9d2724fed6c7b50cd26':
		s+='U'
	elif x == 'dfc8a2232dc2487a5455bda9fa2d45a1':
		s+='F'
	elif x == '60e8373bfb2124aea832f87809fca596':
		s+='Q'
	elif x == '78de2d97da222954cce639cc4b481050':
		s+='G'
	elif x == '0df9b4e759512f36aaa5c7fd4fb1fba8':
		s+='V'
	elif x == '2fc20e9a20605b988999e836301a2408':
		s+='X'
	elif x == '2190a721b2dcb17ff693aa5feecb3b58':
		s+='P'
	elif x == 'fb78aed37621262392a4125183d1bfc9':
		s+='K'
	elif x == '293f56083c20759d275db846c8bfb03e':
		s+='Z'
	elif x == '5ae172c9ea46594cea34ad1a4b1c79cd':
		s+='J'
	elif x == 'a94f49727cf771a85831bd03af1caaf5':
		s+='_'
	else :
		s+=x+'**'
print(s)		

f.close()
