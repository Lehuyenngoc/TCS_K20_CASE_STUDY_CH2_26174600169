from datetime import datetime
#1 Nhap du lieu dau vao
ma_phien = input("Ma phien: ")
ma_may = input("Ma may: ")
cong_suat_w = float(input("Cong suat thiet bi (W): "))
so_phut = float(input("Thoi gian su dung (phut): "))
don_gia_kwh = float(input("Don gia dien (VND/kwh): "))
# 2. Tinh toan du lieu
dien_nang_kwh = cong_suat_w * so_phut / 60 /1000
chi_phi = dien_nang_kwh * don_gia_kwh
tren_60_phut = so_phut > 60
# 3. Lay moc thoi gian ghi nhan hien tai
thoi_diem_ghi_nhan = datetime.now().strftime("%y-%M-%d %H-%M-%S")
# 4. Xuat kiem tra theo dung dinh dang de bai
print("\nMa phien:",ma_phien)
print(f"May: {ma_may}")
print(f"Cong suat: {cong_suat_w:.2f} w")
print(f"Thoi luong: {int(so_phut)} phut")
print(f"Dien nang: {dien_nang_kwh:.3f} kwh")
print(f"Chi phi: {chi_phi:.2f} VND")
print(f"Tren 60 phut: {tren_60_phut}")
print(f"Ghi nhan luc: {thoi_diem_ghi_nhan}")