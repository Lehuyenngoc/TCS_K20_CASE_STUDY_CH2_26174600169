from datetime import datetime
#Lay thoi gian hien tai va dinh dang chuoi
thoi_diem = datetime.now()
thoi_diem_next = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_next)
print(type(thoi_diem_next))
#Bo sung khoang tinh thoi gian
bat_dau = datetime(2026,10,14,13,15)
ket_thuc = datetime(2026,10,14,15,5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))
#24.Du doan ket qua phep tru: 15:05 - 13:15 = 1 gio 50 phut (1:50:00)
#25. Giai thich
# - datetime: Moc thoi gian cu the (ngay,gio)
# - str: Chuoi chu the hien thoi gian sau khi dung strftime()
# - timedelta: Khoang thoi gian lech giua 2 moc datetime

