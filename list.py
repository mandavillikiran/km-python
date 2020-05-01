n = input('')
wkdic = {0:'mon',1:'tue',3:'wed',4:'thu',5:'fri',6:'sat',7:'sun'}
wkday = wkdic.get(int(n))
print(wkday)