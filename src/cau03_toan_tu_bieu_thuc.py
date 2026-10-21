#Cho cac bien ban dau
tong_phut = 135
cong_suat_w = 250
#9.Dung // vaf % de tinh so gio tron ven va so phut con lai
so_gio = tong_phut // 60
so_phut_du = tong_phut % 60
print(f"Thoi gian:{so_gio} gio va {so_phut_du} phut")
#10. Tao bien su_dung_lau nhan True khi tong_phut > 60
su_dung_lau = tong_phut > 60
print("Su dung lau:",su_dung_lau)
#11. Tao bien du_lieu_hop_le nhan True khi cong_suat_w > 0 va tong_phut > 0
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Du lieu hop le:",du_lieu_hop_le)
#12. Kiem chung hai bieu thuc
kq1 = 100 + 20 * 3
kq2 = (100 + 20) * 3
print("Ket qua 100 + 20 * 3 =",kq1)
print("Ket qua (100 + 20) * 3 =",kq2)


      