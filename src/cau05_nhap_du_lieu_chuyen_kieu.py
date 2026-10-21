#17. Dung input() nhan 4 gia tri va in type() ngay sau khi nhap
ma_may = input("nhap ma may: ")
print("Kieu cua ma may:",type(ma_may))
cong_suat_str = input("Nhap cong suat (W): ")
print("Kieu cua cong suat(truoc ep kieu):",type(cong_suat_str))
so_phut_str = input("Nhap so phut su dung: ")
print("Kieu cua so phut(truoc ep kieu):",type(so_phut_str))
don_gia_str = input("Nhap don gia dien/kwh: ")
print("Kieu cua don gia(truoc ep kieu):",type(don_gia_str))
#18. Chuyen doi kieu du lieu
cong_suat_w = float(cong_suat_str)
so_phut = int(so_phut_str)
don_gia_kwh = float(don_gia_str)
#19. Tinh lai dien nang tieu thu va chi phi
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("\n--- Ket qua sau khi chuyen kieu va tinh toan ---")
print(f"Dien nang tieu thu: {dien_nang_kwh} kwh")
print(f"Chi phi dien: {chi_phi} VND")


