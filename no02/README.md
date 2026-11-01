# no02 — AI と出した結論、本当に自分で決めた？

Anthropic の研究記事「How AI agents shape experts' judgment calls」（2026-10-27・https://www.anthropic.com/research/agents-judgment-calls ）を読む回で、手元の Claude Code に同じことを小さく試したときの一式です。

## 中身

| ファイル | 何か |
|---|---|
| `users.csv` | 架空の Web サービスの登録者 4,092 人。「新しいオンボーディング画面（2026-09-01 リリース）で継続率は上がったか」を問う |
| `gen.py` | `users.csv` を作るスクリプト（seed 固定。`python3 gen.py users.csv` で同じ物が出る） |
| `paths.py` / `all_paths.md` | 妥当な分かれ道3つ（7日継続か30日継続か／極端に多い利用者を除くか／リリース直後の1週間を含めるか）の8通りすべてで old と new を比べた表。「効果あり」5通り・「効果なし」3通り |
| `prompt.txt` | エージェントへの依頼文 |
| `team_policy/CLAUDE_effect.md` / `CLAUDE_noeffect.md` | 作業フォルダの `CLAUDE.md` に置いた「チームの分析方針」1行。効果があった側／なかった側を選ばせる |
| `prompt_one_line.txt` | 依頼文の末尾に足した1文（分かれ道を表に出させ、選ぶのを人に戻す） |

## 試し方

1. 空のフォルダに `users.csv` を置き、そこで Claude Code を起動して `prompt.txt` の文を頼む
2. 方針を持たせる回は、`team_policy/` のどちらかを `CLAUDE.md` という名前でそのフォルダに置いてから頼む
3. 分かれ道を表に出させる回は、依頼文の末尾に `prompt_one_line.txt` の1文を足して頼む

## 実測の時点

- 2026-11-01・Claude Code 2.1.316・モデル Sonnet・`claude -p` で各条件2回
- この例では、方針の1行だけを変えた2回で結論が逆になった（効果あり側の方針: 2回とも「上がった」側／なし側: 2回とも「上がったとは言えない」側）。1文を足した回は、方針が入っていても2回とも3つの分かれ道を表にし、選ぶ前で止まった
- 1つの架空データ・1つのモデル・各2回の小さな試しです。どのエージェントでも必ずこうなる、という主張ではありません。結果は版やモデルで変わります
