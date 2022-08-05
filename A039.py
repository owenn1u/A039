ranking =  int(input('第九次總選舉入選成員您好，請輸入第九次總選舉名次: '))
if ranking > 48 or ranking < 1:
	print('輸入錯誤，僅能輸入範圍1~48的數字')
	raise SystemExit


member = int(input('請輸入加入期別: '))
if member <= 6:
	print('恭喜你在加入團體多年後仍有高人氣！')
	if member <= 4:
		print('更恭喜你在最後一次總選舉中能站在大舞台上')
else:
	print('誠摯祝福！也期待你未來在團內的璀璨發展～')