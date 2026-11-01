# 8通りの選び方すべてで old/new を比べ、all_paths.md に書く。python3 paths.py users.csv
import csv, math, itertools, sys
rows = list(csv.DictReader(open(sys.argv[1] if len(sys.argv)>1 else "users.csv")))
N=len(rows); k1=math.ceil(N*0.01)
order=sorted(rows,key=lambda r:-int(r["sessions_7d"])); top={r["user_id"] for r in order[:k1]}
thr=int(order[k1-1]["sessions_7d"])
out=["# 8通りの全経路（機械計算）","",f"行数: {N}。「極端な利用者」= sessions_7d 上位1%（{k1}人・sessions_7d>={thr}）","",
"| # | 指標 | 極端な利用者 | 不具合週(9/1-9/7) | old率 | new率 | 差(pt) | z | p | 判定 |","|---|---|---|---|---|---|---|---|---|---|"]
k=0; cnt={"効果あり":0,"効果なし":0,"逆効果":0}
for m,ex,bw in itertools.product(["active_day7","active_day30"],["含める","除外"],["含める","除く"]):
    k+=1; c={"old":[0,0],"new":[0,0]}
    for r in rows:
        if ex=="除外" and r["user_id"] in top: continue
        if bw=="除く" and r["variant"]=="new" and r["signup_date"]<="2026-09-07": continue
        c[r["variant"]][0]+=int(r[m]); c[r["variant"]][1]+=1
    (x1,n1),(x2,n2)=c["old"],c["new"]; p1,p2=x1/n1,x2/n2; p=(x1+x2)/(n1+n2)
    zz=(p2-p1)/math.sqrt(p*(1-p)*(1/n1+1/n2)); pv=math.erfc(abs(zz)/math.sqrt(2))
    v="効果あり" if (pv<0.05 and p2>p1) else ("逆効果" if pv<0.05 else "効果なし"); cnt[v]+=1
    out.append(f"| {k} | {m} | {ex} | {bw} | {p1:.3f} | {p2:.3f} | {100*(p2-p1):+.1f} | {zz:.2f} | {pv:.4f} | {v} |")
out+=["","判定: p<0.05 かつ new>old を「効果あり」、p<0.05 かつ new<old を「逆効果」、他を「効果なし」。比率の差の z 検定（両側）。","","集計: "+" / ".join(f"{a} {b}通り" for a,b in cnt.items())]
open("all_paths.md","w").write("\n".join(out)+"\n"); print("\n".join(out))
