#Nhap du lieu tu ban phim
ma_phien = input("Nhap ma phien: ")
ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat (W): "))
so_phut = float(input("Nhap so phut su dung: "))
don_gia_kwh = float(input("Nhap don gia (VND/kwh): "))
#Tinh dien ang tieu thu va chi phi
dien_nang_kwh = cong_suat_w * so_phut / 60 /1000
chi_phi = dien_nang_kwh * don_gia_kwh
#In dau ra theo dung dinh dang yeu cau
print(f"\nMa phien: {ma_phien}")
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh}")
print(f"Chi phi: {chi_phi}")