#文字計數

data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f: #一筆一筆重複讀
		data.append(line) # 把自訂變數line，一行一行裝進data清單裡
		count += 1
		if count % 10000 == 0:
			print(len(data)) # 每讀取一行10000筆就把進度印出來

print(len(data)) # 印出data共幾筆資料
print(data[0]) # 印出data第一筆資料的內容


wc = {} #word_count(宣告一個空字典)
for d in data:
	words = d.split(' ') #一堆清單裝著一堆字 split預設值就是空白鍵可不寫(用預設值的話，連續使用空白鍵時會忽略)
	for word in words:
		if word in wc:
			wc[word] +=1 #就把出現在字典裡的次數加1
		else:
			wc[word] = 1 #新增key進入wc字典中然後次數是1

for word in wc:
	if wc[word] > 5000: #在字典中出現次數大於5000的字
		print(word, wc[word]) #word是字典當中每一個key
print(len(wc))

while True:
	word = input('輸入你想查的字')
	if word == 'q':
		break
	if word in wc: #避免輸入的字不在字典中程式會當掉
		print(word, '出現的次數為', wc[word])
	else:
		print('沒這個字')

print('感謝使用本查詢功能')
