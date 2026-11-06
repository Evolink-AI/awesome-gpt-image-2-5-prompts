#!/usr/bin/env python3
"""Verify the full prompt corpus and localization without network access.

The original 250-case release is immutable. New complete cases may be appended;
all declared cases are checked across every category and required language.
"""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ['en', 'es', 'pt', 'ja', 'ko', 'de', 'fr', 'tr', 'zh-TW', 'zh-CN', 'ru']
ORIGINAL_CASE_COUNT = 250
ORIGINAL_FIELDS = (
    'id', 'public_case_number', 'category', 'content_file', 'title', 'author',
    'source_url', 'root_source_url', 'published_at', 'prompt', 'prompt_sha256',
    'input_requirement', 'media',
)
# Frozen from release 4218eaeb200fee5fe829b6ed331fa46a5de3fe53, before additions.
ORIGINAL_CORPUS_SHA256 = 'ab7f672548b7056998e55cf5d05527e0481bd23576f3892906475ec3591fd213'
CASE_LABELS = dict(zip(LOCALES, [
    'Case', 'Caso', 'Caso', 'ケース', '사례', 'Fall', 'Cas', 'Örnek',
    '案例', '案例', 'Пример',
]))
PROMPT_LABELS = dict(zip(LOCALES, [
    'Prompt', 'Prompt', 'Prompt', 'プロンプト', '프롬프트', 'Prompt', 'Prompt',
    'İstem', '提示詞', '提示词', 'Промпт',
]))
INPUT_LABELS = dict(zip(LOCALES, [
    'Input', 'Entrada', 'Entrada', '入力', '입력', 'Eingabe', 'Entrée',
    'Girdi', '輸入', '输入', 'Входные материалы',
]))
PUBLIC_MEDIA_PREFIX = (
    'https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/'
    'github-repo-media/awesome-gpt-image-2-5-prompts/'
)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def split_blocks(text):
    """Return exact unlabeled prompt bodies and prose with fenced content removed."""
    prompts, prose, body = [], [], []
    fence = None
    for line in text.splitlines(keepends=True):
        value = line.removesuffix('\n')
        if fence is not None:
            if value == fence:
                raw = ''.join(body)
                require(raw.endswith('\n'), 'prompt must end with a newline before its closing fence')
                prompts.append(raw[:-1])
                prose.append('\n')
                fence, body = None, []
            else:
                body.append(line)
            continue
        match = re.fullmatch(r'`{3,}', value)
        if match:
            fence = value
            continue
        require(not value.startswith('```'), 'prompt fences must be unlabeled')
        prose.append(line)
    require(fence is None, 'unclosed prompt fence')
    return prompts, ''.join(prose)


def blocks(text):
    return split_blocks(text)[0]


def verify_prose_whitespace(text):
    """Original prompts may retain source whitespace; authored prose may not."""
    _, prose = split_blocks(text)
    for number, line in enumerate(prose.split('\n'), 1):
        require(line == line.rstrip(' \t'), f'authored prose has trailing whitespace at prose line {number}')


def verify_catalog(cases, categories):
    count = len(cases)
    require(count >= ORIGINAL_CASE_COUNT, 'original 250-case corpus is incomplete')
    original = [{key: case[key] for key in ORIGINAL_FIELDS} for case in cases[:ORIGINAL_CASE_COUNT]]
    encoded = json.dumps(original, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
    require(hashlib.sha256(encoded).hexdigest() == ORIGINAL_CORPUS_SHA256,
            'original 250-case metadata, prompts or media changed')
    require([c['public_case_number'] for c in cases] == list(range(1, count + 1)),
            'case numbers must be unique and contiguous from 1')
    require(len({c['id'] for c in cases}) == count, 'duplicate case id')
    require(len({c['prompt_sha256'] for c in cases}) == count, 'duplicate prompt')
    require(bool(categories) and len(set(categories)) == len(categories), 'missing or duplicate categories')
    require(all(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', c) for c in categories), 'invalid category slug')
    require(list(dict.fromkeys(c['category'] for c in cases)) == categories,
            'category routes must follow first corpus appearance without empty categories')
    for case in cases:
        ident = case['id']
        require(bool(case['prompt'].strip()), f'empty prompt: {ident}')
        require(hashlib.sha256(case['prompt'].encode()).hexdigest() == case['prompt_sha256'],
                f'prompt hash mismatch: {ident}')
        require(case['content_file'] == f"cases/{case['category']}.md", f'incorrect content file: {ident}')
        require(re.match(r'https?://[^\s]+$', case['source_url']), f'invalid source URL: {ident}')
        require(bool(case['author']), f'missing author: {ident}')
        require(bool(case['media']) and len(set(case['media'])) == len(case['media']),
                f'missing or duplicated media: {ident}')
        require(all(url.startswith(PUBLIC_MEDIA_PREFIX) for url in case['media']),
                f'media must use the locked R2 repository namespace: {ident}')


def verify_page(text, cases, category, locale, relative):
    prompt_bodies, prose = split_blocks(text)
    require(prompt_bodies == [c['prompt'] for c in cases], f'prompt content/order changed: {relative}')
    anchors = re.findall(r'^<a id="([a-z0-9-]+-case-\d+)"></a>$', prose, re.M)
    expected = [f"{category}-case-{c['public_case_number']}" for c in cases]
    require(anchors == expected, f'case anchors/order differ from catalog: {relative}')
    require(len(re.findall(r'^### ', prose, re.M)) == len(cases), f'case heading count mismatch: {relative}')
    preamble = prose.split(f'<a id="{expected[0]}"></a>', 1)[0]
    menu_targets = re.findall(r'\]\(#([a-z0-9-]+-case-\d+)\)', preamble)
    require(menu_targets == expected, f'category menu count/order mismatch: {relative}')
    for index, case in enumerate(cases):
        anchor = expected[index]
        section = prose.split(f'<a id="{anchor}"></a>', 1)[1]
        if index + 1 < len(expected):
            section = section.split(f'<a id="{expected[index + 1]}"></a>', 1)[0]
        heading = re.search(r'^### (.+)$', section, re.M)
        require(heading is not None and heading[1].startswith(f"{CASE_LABELS[locale]} {case['public_case_number']}: ["),
                f'localized case label/number missing: {relative}#{anchor}')
        require(f"]({case['source_url']})" in heading[1], f'source-linked title missing: {relative}#{anchor}')
        require(section.count(f"]({case['source_url']})") == 1,
                f'duplicate source attribution: {relative}#{anchor}')
        require(re.search(r'\(\S+(?: \S+)* \[' + re.escape(case['author']) + r'\]\(https?://[^)]+\)\)$', heading[1]),
                f'author-linked heading missing: {relative}#{anchor}')
        require(re.search(r'\*\*' + re.escape(PROMPT_LABELS[locale]) + r'\s*[:：]\*\*', section),
                f'localized prompt label missing: {relative}#{anchor}')
        require(re.search(r'\*\*' + re.escape(INPUT_LABELS[locale]) + r'\s*[:：]\*\*', section),
                f'localized input label missing: {relative}#{anchor}')
        urls = set(re.findall(r'(?:src|href)=["\']([^"\']+)["\']', section))
        urls.update(re.findall(r'\]\((https?://[^)]+)\)', section))
        rendered_media = {u for u in urls if u.startswith(PUBLIC_MEDIA_PREFIX)}
        require(rendered_media == set(case['media']), f'case media set mismatch: {relative}#{anchor}')
        require(re.search(r'^---\s*$', section, re.M), f'case separator missing: {relative}#{anchor}')


def main():
    cases = json.loads((ROOT / 'data/prompts.json').read_text())['cases']
    categories = json.loads((ROOT / 'data/content-layout.json').read_text())['categories']
    verify_catalog(cases, categories)
    pages = 0
    for locale in LOCALES:
        readme = ROOT / ('README.md' if locale == 'en' else f'README_{locale}.md')
        index = readme.read_bytes().decode()
        _, index_prose = split_blocks(index)
        expected_targets = set()
        for category in categories:
            relative = f'cases/{category}.md' if locale == 'en' else f'cases/{locale}/{category}.md'
            path = ROOT / relative
            category_cases = [c for c in cases if c['category'] == category]
            expected_targets.update(f"{relative}#{category}-case-{c['public_case_number']}" for c in category_cases)
            verify_page(path.read_bytes().decode(), category_cases, category, locale, relative)
            pages += 1
        actual_targets = set(re.findall(r'\]\((cases/[^)#]+\.md#[a-z0-9-]+-case-\d+)\)', index_prose))
        require(actual_targets == expected_targets, f'README case navigation mismatch: {readme.name}')
        pages += 1
    for path in ROOT.rglob('*.md'):
        require(path.stat().st_size < 450 * 1024, f'Markdown exceeds 450 KiB: {path}')
        verify_prose_whitespace(path.read_bytes().decode())
    print(json.dumps({
        'status': 'passed', 'cases': len(cases), 'original_cases_locked': ORIGINAL_CASE_COUNT,
        'languages': len(LOCALES), 'pages': pages, 'original_prompt_hashes': 'matched',
        'original_corpus_sha256': ORIGINAL_CORPUS_SHA256,
    }, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (AssertionError, OSError, KeyError, ValueError, TypeError) as exc:
        print(f'Content verification failed: {exc}', file=sys.stderr)
        sys.exit(1)
