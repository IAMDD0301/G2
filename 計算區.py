# 距離計算區
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = math.sin(d_lat/2)**2 + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(d_lon/2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1-a))

# 找最近避難所
def find_nearest_shelter(lat, lon):
    nearest = None
    min_dist = float("inf")
    for s in shelters:
        d = haversine(lat, lon, s["lat"], s["lon"])
        if d < min_dist:
            min_dist = d
            nearest = s
            nearest["distance"] = round(d, 3)
    return nearest

# 使用者介面
if __name__ == "__main__":
    print("=== 苗栗市避難所智慧查詢系統（行政里點選版） ===\n")

    villages = list(village_coords.keys())
    for i, v in enumerate(villages, 1):
        print(f"{i}. {v}")

    choice = input("\n請輸入您所在行政里的編號：")

    if not choice.isdigit() or not (1 <= int(choice) <= len(villages)):
        print("\n⚠ 輸入錯誤，請重新執行程式。")
    else:
        village = villages[int(choice) - 1]
        user_lat, user_lon = village_coords[village]
        shelter = find_nearest_shelter(user_lat, user_lon)

        print("\n【查詢結果】")
        print("所在里別：", village)
        print("最近避難所：", shelter["name"])
        print("避難所地址：", shelter["address"])
        print("距離：約", shelter["distance"], "公里")
        print("導航連結：")
        print(f"https://www.google.com/maps/dir/{user_lat},{user_lon}/{shelter['lat']},{shelter['lon']}/")
