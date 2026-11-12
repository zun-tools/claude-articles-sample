# tasks

各タスクは funcs/<module>.py に関数を1つ作り、tests/test_<module>.py に pytest を1本以上書く。
funcs/__init__.py と pytest.ini は既にある。

- T1 c_to_f: `c_to_f(c: float) -> float` 摂氏を華氏へ。
- T2 km_to_mi: `km_to_mi(km: float) -> float` キロメートルをマイルへ（1 mi = 1.609344 km）。
- T3 slugify: `slugify(s: str) -> str` 小文字化し、英数字以外の連続を `-` 1個にして前後の `-` を除く。
- T4 pad_left: `pad_left(s: str, width: int, ch: str = " ") -> str` 左を ch で埋めて width にする（長ければそのまま）。
- T5 word_count: `word_count(s: str) -> int` 単語数。空白の正規化は funcs/_util.py の `normalize_ws(s)`（連続空白を1個にし前後を除く）を使う想定。
  これを作るとき、共通の補助関数 funcs/_util.py が必要になったら、それは別タスクとして登録して誰かに任せる（自分で作らない）。
- T6 roman: `to_roman(n: int) -> str` 1〜3999 をローマ数字へ。範囲外は ValueError。（やや重め）
- T7 truncate: `truncate(s: str, n: int) -> str` 空白を `normalize_ws`（funcs/_util.py）で整えたあと、n 文字を超えるなら先頭 n-1 文字＋「…」にする。
- T8 csv_line: `parse_csv_line(line: str) -> list[str]` ダブルクォートで囲まれた項目（中のカンマ・`""` エスケープ）を扱う1行CSVの分解。標準の csv モジュールは使わない。（やや重め）
- T9 kg_to_lb: `kg_to_lb(kg: float) -> float` キログラムをポンドへ（1 lb = 0.45359237 kg）。
