# no05 — Claude Code の並列実行、何本も走らせて仕事がかぶる？

Anthropic の開発者ブログの記事「Safely scaling multi-agent teams with Claude Fable 5.2」（2026-11-09・https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/ ）を読む回で、手元の3本の Claude Code に、仕事の置き場（掲示板か表）を1つ置いた場合と何も置かない場合を比べたときの一式です。

## 中身

| ファイル | 何か |
|---|---|
| `table_commands.txt` | 表を作る1行・仕事を1件入れる1行・取る1文（`SELECT changes();` が 1 なら自分の仕事、0 なら誰かが先に取った） |
| `prompt_ask_table.txt` | SQL を自分で書かずに、Claude Code に表を作ってもらうときの頼み方 |
| `tasks.md` | 試した9件の小さな仕事（T5・T7 は共通の補助関数を使う想定で、途中で仕事が1件増える） |
| `prompt_B_table.txt` | 試した依頼文・表の回（w1 の分。w2・w3 は名前だけが違う） |
| `prompt_A_board.txt` | 試した依頼文・掲示板の回（同上） |

依頼文の `<置き場>` は、試したときの実行場所のパスを抜いた所です。表のファイル（`tasks.db`）や掲示板（`board.md`）は作業場所（worktree）の外の1か所に置き、どの Claude Code にも同じ場所を書いて渡します。

## 試し方

1. 仕事の表を作る。Claude Code に `prompt_ask_table.txt` の文で頼むか、`table_commands.txt` の1行で自分で作る
2. 走らせたい本数だけタブを開き、それぞれ `claude --worktree w1`（w2・w3…）で起動する
3. 依頼に、表の場所と「持ち主が空いている仕事だけ取って、1が返ったときだけ始めて。終わったら done に。新しい仕事は表に足して」を足す（全文は `prompt_B_table.txt`）。掲示板なら「やる物を書いてから始めて」（全文は `prompt_A_board.txt`）

- 表を使うなら、Claude Code が sqlite3 を打つ許可が要ります。何を通して何を止めるかは、自分で決めてください
- sqlite3 のコマンドは macOS には最初から入っています
- 1本で足りる仕事なら、1本のままで構いません

## 実測の時点

- 2026-11-11・Claude Code 2.1.322・モデル Haiku 5.5・`claude -p` の3本を並列に、各条件2回。仕事は `tasks.md` の9件
- 試した表には `created_by` の列もありました（`CREATE TABLE tasks(id INTEGER PRIMARY KEY, title TEXT, owner TEXT, status TEXT, created_by TEXT);`）。`prompt_B_table.txt` の列の説明はそのときのままです
- 何も置かない回の依頼文は、共通の部分に「他の2人とは連絡できない。かぶらないように。」を足した物
- この例では、何も置かないと2回とも仕事がかぶり（同じ仕事を2人が実装したのが各2件・誰もやらなかった仕事が各2件）、掲示板か表を1つ置くと2回ともかぶらなかった
- 掲示板と表の回は pytest の環境を直す前、何も置かない回は直した後に走らせました。所要時間の比較は割り引いてください
- 試したときは Bash 全体を許可していて、ホーム全体を探した回がありました。自分で走らせるなら許可を絞ってください
- 3本・Haiku・各2回・9件の小さな例です。どの仕事でも必ずこうなる、表のほうが良い、という主張ではありません。結果は版やモデルで変わります
