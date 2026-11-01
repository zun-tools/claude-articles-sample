# 架空の継続率データを作る（seed 固定・同じ users.csv が出る）。python3 gen.py users.csv
import csv, random, datetime as dt, sys
SEED = 20261102
random.seed(SEED)
OUT = sys.argv[1] if len(sys.argv) > 1 else "users.csv"
NH_OLD, NH_NEW = 8, 32   # sessions_7d 上位1%（40/4,0xx）にあたる利用者
rows = []; uid = 1
def rtime(): 
    return "%02d:%02d:%02d" % (min(23, int(random.gauss(14, 4.5)) % 24), random.randint(0,59), random.randint(0,59))
for i in range(61):
    d = dt.date(2026, 8, 1) + dt.timedelta(days=i)
    new = d >= dt.date(2026, 9, 1); bug = new and d <= dt.date(2026, 9, 7)
    for _ in range(random.randint(58, 76)):
        if not new: p7, p30 = 0.300, 0.165
        elif bug:   p7, p30 = 0.200, 0.090
        else:       p7, p30 = 0.360, 0.180
        a7 = int(random.random() < p7); a30 = int(a7 and random.random() < p30 / p7)
        s7 = max(0, int(random.gauss(3.0 + 2.5 * a7, 1.5)))
        rows.append([uid, d.isoformat(), rtime(), "new" if new else "old", s7, a7, a30]); uid += 1
def heavy(idx_list, cluster_n):
    for k, ix in enumerate(idx_list):
        r = rows[ix]
        r[4] = random.randint(22, 55)
        a7 = int(random.random() < 0.95); a30 = int(a7 and random.random() < 0.80)
        r[5], r[6] = a7, a30
        if k < cluster_n:  # 登録時刻が3時台に固まる（ボット風の手がかり）
            r[2] = "03:%02d:%02d" % (random.randint(10, 14), random.randint(0, 59))
oldix = [i for i, r in enumerate(rows) if r[3] == "old"]; newix = [i for i, r in enumerate(rows) if r[3] == "new"]
heavy(random.sample(oldix, NH_OLD), NH_OLD // 2)
heavy(random.sample(newix, NH_NEW), NH_NEW // 2)
with open(OUT, "w", newline="") as f:
    w = csv.writer(f); w.writerow(["user_id","signup_date","signup_time","variant","sessions_7d","active_day7","active_day30"]); w.writerows(rows)
print(len(rows))
