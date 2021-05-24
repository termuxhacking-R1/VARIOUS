import random as ran
import time

stop=False
def pelangi(word,to=None,tab=None):
	if tab:
		ct=["\t" for i in range(tab)]
	else:
		ct=''
	start=time.time()
	while 1:
		myl=[f"\033[9{ran.randint(0,9)}m{x}" for x in word]
		print(end=f"{''.join(ct)}"+f"{''.join(myl)}"+"\r",flush=True)
		if stop:
			break
		elif to:
			if int(time.time()-start) == int(to):
				break
	print()

