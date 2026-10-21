# ---DOAN CODE SUA HOAN CHINH ---
ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: ")) #Ep kieu float
so_phut = int(input("Nhap so phut: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kwh") # Dung dung ten bien dien_nang_kwh
# --- CHAN DOAN VA GHI NHAN LOI ---
# Loi 1: TypeError - Dong 4 goc: KHong the nhan chuoi (str) voi so nguyen.
#Nguyen nhan & cach sua: 'cong_suat_w' chua ep kieu sang float(); Can sua thanh foat(input(...)).
#Loi 2: NameError - Dong 6 goc: Bien 'dien_nang' khong ton tai
#Nguye nha & cach sua: Go sai ten bien; Can sua 'dien_nang' thanh 'dien_nang_kwh'