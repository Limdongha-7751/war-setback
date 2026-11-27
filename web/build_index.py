"""web/template.html 에 data/setback_data.json 을 넣어 루트의 index.html 을 만든다.
사용법 (저장소 루트에서): python web/build_index.py
"""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((root / "data" / "setback_data.json").read_text(encoding="utf-8"))
tpl = (root / "web" / "template.html").read_text(encoding="utf-8")
out = tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
(root / "index.html").write_text(out, encoding="utf-8")
print("index.html 생성 완료:", len(data["countries"]), "개국")
