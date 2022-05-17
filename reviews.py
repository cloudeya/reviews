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


sum_len = 0
for d in data: #d是data中的每筆字串
	sum_len += len(d) # sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len / len(data)) #如果多了縮排會變成每次加一筆數據都算一次平均

