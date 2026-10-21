#Cho cac bien ban dau
cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
#13. Tinh dien nang tieu thu va chi phi dien
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
#14. In gia tri va kieu du lieu cua hai ket qua
print("Dien nang (kwh):",dien_nang_kwh,"|Kieu:",type(dien_nang_kwh))
print("Chi phi (VND):",chi_phi,"|Kieu:",type(chi_phi))
#16.Thay so_phut bang 60 roi tinh lai va so sanh
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("\n--- Ket qua khi so_phut = 60 ---")
print("Dien nang moi (kwh):",dien_nang_kwh)
print("Chi phi moi (VND):",chi_phi)
