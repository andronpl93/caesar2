from django.shortcuts import render
from django.http import HttpResponse
import logging
import json
import re
elita=dict(a='8.17',b='1.49',c='2.78',d='4.25',e='12.7',f='2.23',g='2.02',h='6.09',i='6.97',j='0.15',k='0.77',l='4.03',m='2.41',n='6.75',o='7.51',p='1.93',q='0.1',r='5.99',s='6.33',t='9.06',u='2.76',v='0.98',w='2.36',x='0.15',y='1.97',z='0.05')	
abc=[chr(i+97) for i in range(26)]


def start(request):
		return render(request, 'igor/kalk.html', {})
		
		
def decoder(request):
	paket=diagram(request)
	paket['result']=[]
	rot=Rot(request)
	if rot==-1:
		paket['errors'].append('Необоходимо заполнить поле ROT целочисленным положительным значением!')
	if not paket['errors']:
		paket['rot']=rot
		for i in paket['text']:
			if ord(i)<=ord("z") and ord(i)>=ord("a"):								
				if ord(i)-rot<ord('a'):
					paket['result'].append(chr(ord(i)-rot+26))
				else:
					paket['result'].append(chr(ord(i)-rot))
			else:
				paket['result'].append(i)

	return HttpResponse(json.dumps(paket))
	
def encoder(request):
	paket=diagram(request)
	paket['result']=[]
	rot=Rot(request)
	if rot==-1:
		paket['errors'].append('Необоходимо заполнить поле ROT целочисленным положительным значением!')
	if not paket['errors']:
		paket['rot']=rot	
		for i in paket['text']:
				if ord(i)<=ord("z") and ord(i)>=ord("a"):
					if ord(i)+rot>ord('z'):
						paket['result'].append(chr(ord(i)+rot-26))
					else:
						paket['result'].append(chr(ord(i)+rot))
				else:
					paket['result'].append(i)

	return HttpResponse(json.dumps(paket))

def vanga(request):
	paket=diagram(request)
	paket['result']=[]
	if not paket['errors']:
		mi=0;
		Mi=2600
		kek="";
		for i in range(26):
			for j in range(26):
				mi+=abs(float(elita[abc[j]])-paket['chastota'][(j+i)-((j+i)//26)*26])
			if mi<Mi:
				Mi=mi
				kek=i
			mi=0
		logging.debug('4+')
		if kek==0:
			paket['massage']='Судя по всему, данный текст не зашифрован'
		else:
			paket['massage']='Есть подозрение, что текст зашифрован с ключем ROT'+str(kek)
			
	return HttpResponse(json.dumps(paket))
	
def Rot(request):
	try:																			
		rot=int(request.POST.get("inText"))
		if rot>26:
			rot=rot-(rot//26)*26													#чтобы не шифровать по кругу 
		elif rot<0:
			return -1
	except ValueError:
			return -1
	return rot
	
def diagram(request):
	paket={'errors':[]}
	text=request.POST.get('lef')

	if len(text)==0 :
		paket['errors'].append('Введите текст')
		return paket	
	text=str(text).lower()
	tex=re.sub(r'[^a-z]','',text)  
	if len(tex)==0 and dlina:
		paket['errors'].append('Нет символов для шифрования')
		return paket
	leng=len(tex)	  																
	chastota=[round((tex.count(i)/leng)*100,1) for i in abc]
	norm=[((i-min(chastota))*100/(max(chastota)-min(chastota)))+1 for i in chastota]																				# чтобы наибольний столбик был высотой в 100%, 
	paket.update({'norm':norm,'chastota':chastota,'text':text})
	return paket
	


	
logging.basicConfig(
	level = logging.DEBUG,
	format = '%(asctime)s %(levelname)s %(message)s',
)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	