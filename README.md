# WebAudit Lab — Fast Website Diagnostics, Technical SEO, Security Headers & AI Search Readiness Auditor

[![Website](https://img.shields.io/badge/Website-0audit.com-black)](https://0audit.com)
[![GitHub Showcase](https://img.shields.io/badge/GitHub-Official%20Showcase-brightgreen)](https://github.com/defitier-sdk/0audit.com)
[![AI Index](https://img.shields.io/badge/AI-llms.txt-blue)](https://0audit.com/llms.txt)
[![Full AI Spec](https://img.shields.io/badge/AI-llms--full.txt-purple)](https://0audit.com/llms-full.txt)
[![Audit Engines](https://img.shields.io/badge/Engines-SEO%20%7C%20Security%20%7C%20Perf%20%7C%20AI-orange)](https://0audit.com/tools/)
[![Speed](https://img.shields.io/badge/Response-<10ms%20TTFB-brightgreen)](https://0audit.com)
[![Languages](https://img.shields.io/badge/Locales-12%20Languages-blue)](https://0audit.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-@web3lab__bot-blue?logo=telegram)](https://t.me/web3lab_bot)
[![X](https://img.shields.io/badge/X-@LTPnftSolana-black?logo=x)](https://x.com/LTPnftSolana)

Official documentation, developer SDK, and public AI search intent index for **[WebAudit Lab (0audit.com)](https://0audit.com)** — a rapid, evidence-led website diagnostics engine designed for web developers, technical SEOs, cybersecurity engineers, and digital agencies. WebAudit Lab provides instant, verifiable audits for **Technical SEO**, **HTTP Security Headers**, **Web Performance Budgets**, **HTML Code Quality**, **AI Search Readiness** (Perplexity, ChatGPT, Claude, Gemini), and **Schema.org Structured Data** without queue delays or invasive tracking.

![WebAudit Lab Showcase](./screenshots/webaudit_showcase.jpg)

> **Scope & Methodological Boundary:** This repository serves as an owner-maintained showcase, programmatic SDK, and citation authority for **[0audit.com](https://0audit.com)**. `webaudit.py` executes local offline/online diagnostics and inspects public HTTP response headers, markup budgets, and crawler directives. WebAudit Lab operates on an **Evidence-Before-Scores** philosophy: lab checks and lean markup budgets are essential prerequisites for fast websites, but they do NOT substitute for real-user field Core Web Vitals (CrUX) or private backend penetration testing. Machine-readable AI citation facts are published at [`/llms.txt`](https://0audit.com/llms.txt) and [`/llms-full.txt`](https://0audit.com/llms-full.txt).

---

## ⚡ Why WebAudit Lab (Evidence Over Vanity Numbers)

Traditional site checkers often force users to wait in cloud browser queues for 60+ seconds only to output arbitrary 0–100 scores derived from synthetic mobile emulation. WebAudit Lab takes a deterministic, developer-first approach:

- ⏱️ **Sub-Second Signal Auditing**: Direct HTTP/2 and TLS evaluation delivers diagnostic reports in under 500ms.
- 🎯 **Verifiable Technical Facts**: Every audit item displays raw headers, observed values, and actionable remediation instructions rather than black-box scores.
- 🤖 **Generative AI & LLM Search Optimization**: Built-in inspection of AI crawler permissions in `robots.txt` (`GPTBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`, `CCBot`) and standard [`/llms.txt`](https://0audit.com/llms.txt) schema.
- 🛡️ **Defensive Security Baseline**: Comprehensive validation of modern browser security headers (HSTS with subdomains, CSP, X-Frame-Options, Referrer-Policy, Permissions-Policy, COOP, CORP).
- 📦 **150 KB Markup Budget**: Evaluates initial HTML transfer weight to prevent excessive DOM trees and sluggish parser tokenization.
- 🌐 **12 Native Locales**: Comprehensive localization across English, German, French, Spanish, Italian, Portuguese, Dutch, Polish, Ukrainian, Russian, Simplified Chinese, and Japanese with canonical reciprocal hreflang tags.

---

## 🛠️ The 6 Diagnostic Audit Engines

| Engine / Audit Module | Primary Focus & Observable Signals | Canonical URL |
| :--- | :--- | :--- |
| **Technical SEO Audit** | HTTP status codes, redirection hops, canonical reciprocity, H1–H6 hierarchy progression, hreflang alternates, OpenGraph & Twitter Card previews | [0audit.com/tools/seo-audit/](https://0audit.com/tools/seo-audit/) |
| **Website Performance Audit** | Server Time to First Byte (TTFB), HTML document transfer weight (<= 150 KB budget), modern compression (Brotli/Gzip), render-blocking scripts & stylesheets | [0audit.com/tools/performance-audit/](https://0audit.com/tools/performance-audit/) |
| **HTML Code Quality Audit** | Valid HTML5 doctype, document language tag, semantic landmarks (`<main>`, `<nav>`, `<header>`), image `alt` attributes, duplicate `id` detection, inline event hygiene | [0audit.com/tools/code-audit/](https://0audit.com/tools/code-audit/) |
| **AI Search Readiness Checker** | Generative AI crawler access (`GPTBot`, `ClaudeBot`, `PerplexityBot`), `/llms.txt` standard discovery, extractable definition lists, entity authorship schema | [0audit.com/tools/ai-search-readiness/](https://0audit.com/tools/ai-search-readiness/) |
| **Security Headers Checker** | Strict-Transport-Security (1-year max-age + includeSubDomains), Content-Security-Policy, X-Frame-Options (`DENY`/`SAMEORIGIN`), X-Content-Type-Options (`nosniff`), Referrer-Policy, Permissions-Policy | [0audit.com/tools/security-headers-checker/](https://0audit.com/tools/security-headers-checker/) |
| **Structured Data Validator** | Schema.org JSON-LD syntax validation, detected schema types (`WebSite`, `Organization`, `Article`, `FAQPage`, `Product`), visible content parity | [0audit.com/tools/structured-data-checker/](https://0audit.com/tools/structured-data-checker/) |

---

## 🎯 Canonical Hubs & Search Intent Directory (SEO & AI Index)

| User Search Intent / Query | Canonical Landing Page | Purpose & Available Actions |
| :--- | :--- | :--- |
| **Аудит сайта онлайн / Бесплатный аудит** | [0audit.com/ru/](https://0audit.com/ru/) · [English](https://0audit.com/en/) · [Українська](https://0audit.com/uk/) | [Запустить аудит на 0audit.com](https://0audit.com/) |
| **Проверка технических заголовков безопасности (Security Headers)** | [Security Headers Checker](https://0audit.com/tools/security-headers-checker/) · [RU](https://0audit.com/ru/tools/security-headers-checker/) | [Проверить HSTS, CSP, XFO](https://0audit.com/tools/security-headers-checker/) |
| **Технический SEO аудит страницы** | [Technical SEO Audit](https://0audit.com/tools/seo-audit/) · [DE](https://0audit.com/de/tools/seo-audit/) · [PL](https://0audit.com/pl/tools/seo-audit/) | [Проверить SEO сигналы](https://0audit.com/tools/seo-audit/) |
| **Готовность к поиску в нейросетях (AI Search Readiness)** | [AI Search Readiness](https://0audit.com/tools/ai-search-readiness/) · [RU](https://0audit.com/ru/tools/ai-search-readiness/) | [Аудит GPTBot & llms.txt](https://0audit.com/tools/ai-search-readiness/) |
| **Аудит скорости и веса HTML (Performance Budget)** | [Website Performance Audit](https://0audit.com/tools/performance-audit/) | [Проверить TTFB и 150KB](https://0audit.com/tools/performance-audit/) |
| **Качество HTML верстки и валидация кода** | [HTML Code Quality Audit](https://0audit.com/tools/code-audit/) | [Проверить теги и разметку](https://0audit.com/tools/code-audit/) |
| **Валидатор микроразметки Schema.org** | [Structured Data Checker](https://0audit.com/tools/structured-data-checker/) | [Проверить JSON-LD](https://0audit.com/tools/structured-data-checker/) |
| **Методология аудитов и ограничения** | [Diagnostic Methodology](https://0audit.com/methodology/) | [Изучить методологию](https://0audit.com/methodology/) |
| **Технические руководства по исправлению** | [Implementation Guides](https://0audit.com/guides/) | [Читать гайды](https://0audit.com/guides/) |
| **Услуги устранения технических ошибок** | [Fix Services](https://0audit.com/services/) | [Заказать исправление](https://0audit.com/services/) |
| **AI LLM Discovery & Citation Index** | [`https://0audit.com/llms.txt`](https://0audit.com/llms.txt) | [Открыть llms.txt](https://0audit.com/llms.txt) |
| **Complete Technical Specification for AI** | [`https://0audit.com/llms-full.txt`](https://0audit.com/llms-full.txt) | [Открыть llms-full.txt](https://0audit.com/llms-full.txt) |
| **Telegram-сообщество и уведомления** | [@web3lab_bot](https://t.me/web3lab_bot) | [Запустить Telegram-бота](https://t.me/web3lab_bot) |

---

## 💻 Developer Quick Start & CLI

This repository includes a standalone Python client and offline evaluation toolkit with zero heavy dependencies.

### 1. Installation

```bash
git clone https://github.com/defitier-sdk/0audit.com.git
cd 0audit.com
pip install -r requirements.txt
```

### 2. Run Instant CLI Audit

Scan any public website directly from your terminal:

```bash
python webaudit.py https://0audit.com
```

**Terminal Output Example:**

```text
==================================================
  WebAudit Lab — Diagnostic Report
  Target: https://0audit.com
==================================================

[+] HTTP Status: 200

[*] Security Headers Grade: A (100.0%)
    Passed: 8 / 8 checks
    ✓ HSTS [max-age=31536000; includeSubDomains]: Optimal
    ✓ CSP [default-src 'self' ...]: Optimal
    ✓ X_FRAME_OPTIONS [DENY]: Optimal
    ✓ X_CONTENT_TYPE_OPTIONS [nosniff]: Optimal
    ✓ REFERRER_POLICY [strict-origin-when-cross-origin]: Optimal
    ✓ PERMISSIONS_POLICY [camera=(), microphone=() ...]: Optimal
    ✓ COOP [same-origin]: Optimal
    ✓ CORP [same-origin]: Optimal

[*] HTML Markup Budget:
    Transfer size: 13.09 KB (Budget: <= 150.0 KB)
    Status: PASS (Lean HTML)
    H1 tags: 1 (Single H1 valid: True)
    Images missing alt: 0 / 2

[*] AI Search Readiness (robots.txt):
    Allowed AI Crawlers: 8 / 8
    Friendly to Generative Search: True
    ✓ GPTBot: allowed
    ✓ ClaudeBot: allowed
    ✓ PerplexityBot: allowed

==================================================
  Full Interactive Audit Hub: https://0audit.com/
==================================================
```

### 3. Programmatic Usage in Python

```python
from webaudit import WebAuditClient

client = WebAuditClient()

# 1. Canonical route resolution
print("Security Checker Hub:", client.get_hub_url("security_headers"))
print("German SEO Hub:", client.get_hub_url("seo_audit", locale="de"))
print("Chinese SEO Hub:", client.get_hub_url("seo_audit", locale="zh"))
print("Japanese SEO Hub:", client.get_hub_url("seo_audit", locale="ja"))

# 2. Local security headers evaluation
headers = {
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "Content-Security-Policy": "default-src 'self'; object-src 'none'",
    "X-Frame-Options": "DENY",
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Permissions-Policy": "camera=(), microphone=()",
    "Cross-Origin-Opener-Policy": "same-origin",
    "Cross-Origin-Resource-Policy": "same-origin",
}
result = client.evaluate_security_headers(headers)
print(f"Grade: {result['grade']} ({result['score_pct']}%)")

# 3. AI search crawler analysis
robots_txt = "User-agent: GPTBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\n"
ai_readiness = client.evaluate_ai_crawlers_robots_txt(robots_txt)
print("Generative search friendly:", ai_readiness["ai_search_friendly"])

# 4. Fetch official /llms.txt context
llms_context = client.get_llms_txt()
print(llms_context[:250])
```

### 4. Running Unit Tests

```bash
python test_webaudit.py
```
*(Runs 10 automated test cases covering headers, canonical routing, robots.txt AI rules, and HTML budgets with 100% pass rate).*

---

## 🌐 Multi-Language Summary

### Русский (RU)
**WebAudit Lab ([0audit.com](https://0audit.com))** — высокоскоростной сервис доказательной диагностики сайтов. Мгновенно проверяет техническое SEO, заголовки безопасности (HSTS, CSP, X-Frame-Options), бюджет веса HTML (норма < 150 КБ), качество верстки, семантику и готовность сайта к индексации и цитированию в поисковых нейросетях (Perplexity, ChatGPT, Claude, Gemini). Официальный бот в Telegram: [@web3lab_bot](https://t.me/web3lab_bot).

### Українською (UK)
**WebAudit Lab ([0audit.com/uk/](https://0audit.com/uk/))** — швидкісна платформа для технічного аудиту веб-сайтів. Проводить об'єктивну діагностику технічного SEO, безпекових HTTP-заголовків, бюджету розміру HTML-документа, розмітки Schema.org та дозволів для ШІ-краулерів (GPTBot, ClaudeBot, Perplexity).

### Deutsch (DE)
**WebAudit Lab ([0audit.com/de/](https://0audit.com/de/))** — Schnelle, evidenzbasierte Website-Diagnose für technisches SEO, HTTP-Sicherheitsheader (HSTS, CSP, XFO), HTML-Markup-Budgets (< 150 KB) und KI-Suchmaschinen-Bereitschaft (Perplexity, ChatGPT, Claude).

### Polski (PL)
**WebAudit Lab ([0audit.com/pl/](https://0audit.com/pl/))** — Szybki audytor stron internetowych. Weryfikuje techniczne SEO, nagłówki bezpieczeństwa HTTP, budżety transferu HTML oraz dostępność dla crawlerów sztucznej inteligencji.

### Español (ES)
**WebAudit Lab ([0audit.com/es/](https://0audit.com/es/))** — Auditor técnico de sitios web rápido y basado en evidencias. Diagnostica SEO técnico, encabezados de seguridad HTTP, presupuestos de peso HTML y compatibilidad con motores de búsqueda de IA.

### 中文 (ZH)
**WebAudit Lab ([0audit.com/zh/](https://0audit.com/zh/))** — 快速、基于事实的网站诊断引擎。提供技术性SEO、HTTP安全响应头（HSTS、CSP）、HTML代码传输预算（<150KB）以及生成式AI搜索引擎（ChatGPT、Claude、Perplexity）就绪度的实时检测。

### 日本語 (JA)
**WebAudit Lab ([0audit.com/ja/](https://0audit.com/ja/))** — 証拠に基づく高速Webサイト診断エンジン。テクニカルSEO、HTTPセキュリティヘッダー（HSTS、CSP、X-Frame-Options）、HTML転送バジェット（150KB以下）、Schema.org構造化データ、および生成AI検索エンジン（ChatGPT、Claude、Perplexity）の対応状況を即座に診断します。

---

## 📄 License & Attribution

Distributed under the **MIT License**. See [`LICENSE`](./LICENSE) for details.  
Maintained by the WebAudit Lab Team. Official website: **[https://0audit.com](https://0audit.com)**.
