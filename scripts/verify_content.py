#!/usr/bin/env python3
"""Check the complete prompt corpus, routes and media without network access."""
from pathlib import Path
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
LOCALES=['en','es','pt','ja','ko','de','fr','tr','zh-TW','zh-CN','ru']
def blocks(text):
    result=[];pos=0
    while True:
        m=re.search(r'^(`{3,})\n',text[pos:],re.M)
        if not m:break
        start=pos+m.end();fence=m[1];end=re.search(r'^'+re.escape(fence)+r'$' ,text[start:],re.M)
        if not end:raise AssertionError('unclosed prompt fence')
        raw=text[start:start+end.start()]
        assert raw.endswith('\n')
        result.append(raw[:-1]);pos=start+end.end()
    return result
def verify_prose_whitespace(text):
    """Source prompts may have original trailing spaces; authored prose may not."""
    fence=None
    for number,line in enumerate(text.split('\n'),1):
        if fence is not None:
            if line==fence:fence=None
            continue
        if re.fullmatch(r'`{3,}',line):
            fence=line
            continue
        assert line==line.rstrip(' \t'),f'authored prose has trailing whitespace at line {number}'
    assert fence is None,'unclosed prompt fence'
def main():
    cases=json.loads((ROOT/'data/prompts.json').read_text())['cases']
    cats=json.loads((ROOT/'data/content-layout.json').read_text())['categories']
    assert len(cases)==250 and [c['public_case_number'] for c in cases]==list(range(1,251))
    assert len({c['id'] for c in cases})==250
    assert len({c['prompt_sha256'] for c in cases})==250
    for c in cases:assert hashlib.sha256(c['prompt'].encode()).hexdigest()==c['prompt_sha256']
    pages=0
    for loc in LOCALES:
        readme=ROOT/('README.md' if loc=='en' else f'README_{loc}.md')
        index=readme.read_text();pages+=1
        for cat in cats:
            rel=f'cases/{cat}.md' if loc=='en' else f'cases/{loc}/{cat}.md'
            p=ROOT/rel;text=p.read_bytes().decode();cc=[c for c in cases if c['category']==cat]
            assert blocks(text)==[c['prompt'] for c in cc],f'prompt changed: {rel}'
            assert p.stat().st_size<450*1024
            for c in cc:
                anchor=f"{cat}-case-{c['public_case_number']}"
                assert f'({rel}#{anchor})' in index
                assert text.count(f'<a id="{anchor}"></a>')==1
                section=text.split(f'<a id="{anchor}"></a>')[1].split('\n<a id=')[0]
                assert f']({c["source_url"]})' in section
                for url in c['media']:assert url in section
            pages+=1
    for p in ROOT.rglob('*.md'):
        assert p.stat().st_size<450*1024,str(p)
        verify_prose_whitespace(p.read_bytes().decode())
    print(json.dumps({'status':'passed','cases':len(cases),'languages':len(LOCALES),'pages':pages,'original_prompt_hashes':'matched'},indent=2))
if __name__=='__main__':
    try:main()
    except (AssertionError,OSError,KeyError,ValueError) as exc:
        print(f'Content verification failed: {exc}',file=sys.stderr);sys.exit(1)
