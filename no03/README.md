# no03 — auto memory、書いたら終わりになってない？

Anthropic の記事「The components of agent memory」（Lance Martin・2026-11-06・https://www.anthropic.com/research/components-of-agent-memory ）を読む回で、Claude Code の auto memory を見返させたときに使った自作のコマンドです。

## 中身

| ファイル | 何か |
|---|---|
| `.claude/commands/memory-review.md` | 自作のコマンド `/memory-review` の全文。動画と記事で打ったものと同じ文面 |
| `prompt_one_line.txt` | コマンドを置かずに、ふだんの対話で1回頼むときの1文（今夜の一手の一例） |

コマンドの中身はこの1文です。

```markdown
---
description: auto memory を見返して整理する（週1回の見直し用）
---
auto memory を見返して整理して。重複はまとめ、古い・食い違うメモは今の方針に直すか消し、MEMORY.md は索引として短く。
```

この文は古いメモを「消す」ことも許しています。消してよいかは自分で決めてください。

## 試し方

1. Claude Code で `/memory` を打ち、「Open auto-memory folder」から MEMORY.md を開いて、終わった用事の行を探す
2. 1回だけ頼むなら、`prompt_one_line.txt` の1文をそのまま頼む
3. 繰り返すなら、作業中のプロジェクトに `.claude/commands/memory-review.md` を置き、Claude Code を起動して `/memory-review` を打つ

```bash
mkdir -p .claude/commands
cat > .claude/commands/memory-review.md <<'EOF'
---
description: auto memory を見返して整理する（週1回の見直し用）
---
auto memory を見返して整理して。重複はまとめ、古い・食い違うメモは今の方針に直すか消し、MEMORY.md は索引として短く。
EOF
```

- ふだんの対話で打つと、ファイルの編集の許可を求められます。中身を確かめてから通してください
- 整理の後は、移した物が索引からたどれるかを一度見てください。索引から外れたメモは届きにくくなるかもしれません

## 実測の時点

- 2026-11-08・Claude Code 2.1.319・モデル Sonnet・`claude -p "/memory-review"` を1回。記憶のフォルダの読み書き・削除と、読み取り系のコマンドだけを許可
- 記憶は、長く使った auto memory を元に、映せない行を架空の話へ書き直した加工版
- この例では、MEMORY.md が146行から122行（31,498→14,231 バイト）になり、公開日を過ぎた予約4件は消されずに別の索引ファイル（`archive_index.md`）へ移った。メモのファイルの追加・削除は0
- `prompt_one_line.txt` の1文そのものでは試していません（頼み方の一例です）
- 1つの記憶・1つのモデル・整理1回の小さな試しです。どの記憶でも必ずこうなる、という主張ではありません。結果は版やモデルで変わります
