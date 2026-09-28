"""
WebAudit Lab (0audit.com) — Python Developer SDK & Diagnostic Engine.

Official website: https://0audit.com/
Machine-readable AI Index: https://0audit.com/llms.txt
Full specification: https://0audit.com/llms-full.txt
"""

from __future__ import annotations

import re
import sys
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

DEFAULT_BASE_URL = "https://0audit.com"
RECOMMENDED_HTML_BUDGET_KB = 150.0

CANONICAL_HUBS: Dict[str, str] = {
    "home": "https://0audit.com/",
    "seo_audit": "https://0audit.com/tools/seo-audit/",
    "performance_audit": "https://0audit.com/tools/performance-audit/",
    "code_audit": "https://0audit.com/tools/code-audit/",
    "ai_search": "https://0audit.com/tools/ai-search-readiness/",
    "security_headers": "https://0audit.com/tools/security-headers-checker/",
    "structured_data": "https://0audit.com/tools/structured-data-checker/",
    "tools": "https://0audit.com/tools/",
    "methodology": "https://0audit.com/methodology/",
    "guides": "https://0audit.com/guides/",
    "services": "https://0audit.com/services/",
    "security": "https://0audit.com/security/",
    "about": "https://0audit.com/about/",
    "about_md": "https://0audit.com/about.md",
    "llms": "https://0audit.com/llms.txt",
    "llms_full": "https://0audit.com/llms-full.txt",
}

AI_BOTS: List[str] = [
    "GPTBot",
    "ChatGPT-User",
    "ClaudeBot",
    "anthropic-ai",
    "PerplexityBot",
    "Google-Extended",
    "CCBot",
    "Bytespider",
]


class WebAuditClient:
    """Official programmatic client and diagnostic router for WebAudit Lab."""

    def __init__(self, base_url: str = DEFAULT_BASE_URL) -> None:
        self.base_url = base_url.rstrip("/")

    def get_hub_url(self, key: str, locale: str = "en") -> str:
        """Returns the canonical URL for a specific audit tool hub."""
        if key not in CANONICAL_HUBS:
            raise KeyError(f"Unknown hub '{key}'. Available: {list(CANONICAL_HUBS.keys())}")
        canonical = CANONICAL_HUBS[key]
        if locale == "en" or key in ("llms", "llms_full", "about_md"):
            return canonical
        # Multi-language canonical route
        path = urllib.parse.urlparse(canonical).path.lstrip("/")
        return f"{self.base_url}/{locale}/{path}"

    @staticmethod
    def evaluate_security_headers(headers: Dict[str, str]) -> Dict[str, Any]:
        """
        Evaluates defensive HTTP response headers against modern security standards.
        Audits: HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, COOP, CORP.
        """
        # Normalize header keys to lowercase
        norm_headers = {k.lower(): v for k, v in headers.items()}
        results: Dict[str, Any] = {}
        passed = 0
        total = 8

        # 1. HSTS
        hsts = norm_headers.get("strict-transport-security")
        if hsts:
            has_subdomains = "includesubdomains" in hsts.lower()
            max_age_match = re.search(r"max-age=(\d+)", hsts.lower())
            max_age = int(max_age_match.group(1)) if max_age_match else 0
            is_valid = max_age >= 31536000
            results["hsts"] = {
                "status": "pass" if is_valid else "warn",
                "value": hsts,
                "has_subdomains": has_subdomains,
                "max_age_sec": max_age,
                "recommendation": "Maintain max-age >= 31536000 (1 year) with includeSubDomains." if not is_valid else "Optimal",
            }
            if is_valid:
                passed += 1
        else:
            results["hsts"] = {
                "status": "fail",
                "value": None,
                "recommendation": "Add Strict-Transport-Security: max-age=31536000; includeSubDomains",
            }

        # 2. CSP
        csp = norm_headers.get("content-security-policy")
        if csp:
            results["csp"] = {
                "status": "pass",
                "value": csp,
                "has_default_src": "default-src" in csp,
                "has_object_none": "object-src 'none'" in csp or "object-src none" in csp,
                "recommendation": "Optimal",
            }
            passed += 1
        else:
            results["csp"] = {
                "status": "fail",
                "value": None,
                "recommendation": "Configure a Content-Security-Policy to mitigate XSS and unauthorized script injection.",
            }

        # 3. X-Frame-Options
        xfo = norm_headers.get("x-frame-options")
        if xfo and xfo.upper() in ("DENY", "SAMEORIGIN"):
            results["x_frame_options"] = {"status": "pass", "value": xfo.upper(), "recommendation": "Optimal"}
            passed += 1
        else:
            results["x_frame_options"] = {
                "status": "fail",
                "value": xfo,
                "recommendation": "Set X-Frame-Options: DENY or SAMEORIGIN to prevent clickjacking.",
            }

        # 4. X-Content-Type-Options
        xcto = norm_headers.get("x-content-type-options")
        if xcto and "nosniff" in xcto.lower():
            results["x_content_type_options"] = {"status": "pass", "value": xcto, "recommendation": "Optimal"}
            passed += 1
        else:
            results["x_content_type_options"] = {
                "status": "fail",
                "value": xcto,
                "recommendation": "Set X-Content-Type-Options: nosniff to prevent MIME confusion exploits.",
            }

        # 5. Referrer-Policy
        ref = norm_headers.get("referrer-policy")
        if ref:
            tokens = [t.strip().lower() for t in ref.split(",") if t.strip()]
            effective = tokens[-1] if tokens else ""
            if effective in ("unsafe-url", "no-referrer-when-downgrade"):
                results["referrer_policy"] = {
                    "status": "warn",
                    "value": ref,
                    "recommendation": "Replace insecure policy with strict-origin-when-cross-origin or no-referrer.",
                }
            elif effective in ("strict-origin-when-cross-origin", "no-referrer", "same-origin", "strict-origin", "origin-when-cross-origin", "origin"):
                results["referrer_policy"] = {"status": "pass", "value": ref, "recommendation": "Optimal"}
                passed += 1
            else:
                results["referrer_policy"] = {
                    "status": "warn",
                    "value": ref,
                    "recommendation": "Set Referrer-Policy: strict-origin-when-cross-origin to protect user privacy.",
                }
        else:
            results["referrer_policy"] = {
                "status": "fail",
                "value": None,
                "recommendation": "Set Referrer-Policy: strict-origin-when-cross-origin to protect user privacy.",
            }

        # 6. Permissions-Policy
        pp = norm_headers.get("permissions-policy")
        if pp:
            results["permissions_policy"] = {"status": "pass", "value": pp, "recommendation": "Optimal"}
            passed += 1
        else:
            results["permissions_policy"] = {
                "status": "warn",
                "value": None,
                "recommendation": "Configure Permissions-Policy to lock down camera, microphone, and geolocation APIs.",
            }

        # 7. Cross-Origin-Opener-Policy (COOP)
        coop = norm_headers.get("cross-origin-opener-policy")
        if coop and "same-origin" in coop.lower():
            results["coop"] = {"status": "pass", "value": coop, "recommendation": "Optimal"}
            passed += 1
        else:
            results["coop"] = {
                "status": "warn",
                "value": coop,
                "recommendation": "Consider setting Cross-Origin-Opener-Policy: same-origin for process isolation.",
            }

        # 8. Cross-Origin-Resource-Policy (CORP)
        corp = norm_headers.get("cross-origin-resource-policy")
        if corp and corp.lower() in ("same-origin", "same-site"):
            results["corp"] = {"status": "pass", "value": corp, "recommendation": "Optimal"}
            passed += 1
        else:
            results["corp"] = {
                "status": "warn",
                "value": corp,
                "recommendation": "Consider setting Cross-Origin-Resource-Policy: same-origin to prevent cross-origin leaks.",
            }

        score_pct = round((passed / total) * 100, 1)
        return {
            "score_pct": score_pct,
            "passed_checks": passed,
            "total_checks": total,
            "grade": "A" if score_pct >= 85 else "B" if score_pct >= 65 else "C" if score_pct >= 40 else "F",
            "details": results,
        }

    @staticmethod
    def evaluate_ai_crawlers_robots_txt(robots_txt: str) -> Dict[str, Any]:
        """
        Analyzes robots.txt directives for major generative AI crawlers (GPTBot, ClaudeBot, etc.).
        Returns crawl access status and indexation recommendations.
        """
        lines = [line.strip() for line in robots_txt.splitlines() if line.strip() and not line.strip().startswith("#")]
        current_agents: List[str] = []
        bot_rules: Dict[str, List[str]] = {bot.lower(): [] for bot in AI_BOTS}
        global_disallows: List[str] = []

        in_user_agents = False
        for line in lines:
            if ":" not in line:
                continue
            key, val = [p.strip() for p in line.split(":", 1)]
            key_lower = key.lower()

            if key_lower == "user-agent":
                agent = val.lower()
                if not in_user_agents:
                    current_agents = []
                    in_user_agents = True
                current_agents.append(agent)
            else:
                in_user_agents = False
                if key_lower == "disallow" and val:
                    for agent in current_agents:
                        if agent == "*":
                            global_disallows.append(val)
                        elif agent in bot_rules:
                            bot_rules[agent].append(val)

        status: Dict[str, Any] = {}
        for bot in AI_BOTS:
            bot_lower = bot.lower()
            specific = bot_rules.get(bot_lower, [])
            if "/" in specific:
                access = "blocked"
            elif "/" in global_disallows and not specific:
                access = "blocked_by_global"
            else:
                access = "allowed"

            status[bot] = {
                "access": access,
                "specific_disallows": specific,
                "can_cite": access == "allowed",
            }

        allowed_count = sum(1 for b in status.values() if b["can_cite"])
        return {
            "crawlers": status,
            "allowed_bots": allowed_count,
            "total_evaluated_bots": len(AI_BOTS),
            "ai_search_friendly": allowed_count >= (len(AI_BOTS) // 2),
        }

    @staticmethod
    def evaluate_html_budget(html: str) -> Dict[str, Any]:
        """
        Evaluates HTML transfer weight against the 150 KB lean markup budget.
        Counts key document elements (H1 tags, scripts, stylesheets, images without alt).
        """
        raw_bytes = html.encode("utf-8") if isinstance(html, str) else html
        size_kb = len(raw_bytes) / 1024.0

        # Regex counts for baseline sanity
        h1_matches = re.findall(r"<h1\b[^>]*>(.*?)</h1>", html, re.IGNORECASE | re.DOTALL)
        script_matches = re.findall(r"<script\b[^>]*>", html, re.IGNORECASE)
        async_defer_scripts = re.findall(r"<script\b[^>]*(?:async|defer)[^>]*>", html, re.IGNORECASE)
        img_tags = re.findall(r"<img\b[^>]*>", html, re.IGNORECASE)
        img_with_alt = [img for img in img_tags if re.search(r'\balt\s*=\s*["\'][^"\']*["\']', img, re.IGNORECASE)]

        is_under_budget = size_kb <= RECOMMENDED_HTML_BUDGET_KB

        return {
            "html_size_kb": round(size_kb, 2),
            "budget_threshold_kb": RECOMMENDED_HTML_BUDGET_KB,
            "is_under_budget": is_under_budget,
            "h1_count": len(h1_matches),
            "single_h1_valid": len(h1_matches) == 1,
            "script_tags_count": len(script_matches),
            "async_defer_count": len(async_defer_scripts),
            "images_count": len(img_tags),
            "images_with_alt_count": len(img_with_alt),
            "images_missing_alt_count": len(img_tags) - len(img_with_alt),
        }

    def get_llms_txt(self) -> str:
        """Fetches the official /llms.txt file from WebAudit Lab."""
        req = urllib.request.Request(
            f"{self.base_url}/llms.txt",
            headers={"Accept": "text/plain", "User-Agent": "WebAudit-SDK/1.0.0"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode("utf-8")


def run_cli_audit(target_url: str) -> None:
    """Executes a diagnostic scan on target_url and prints a structured summary."""
    if not target_url.startswith(("http://", "https://")):
        target_url = "https://" + target_url

    print(f"\n==================================================")
    print(f"  WebAudit Lab — Diagnostic Report")
    print(f"  Target: {target_url}")
    print(f"==================================================")

    req = urllib.request.Request(
        target_url,
        headers={"User-Agent": "WebAudit-Scanner/1.0.0 (+https://0audit.com)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            status_code = response.getcode()
            headers = dict(response.info())
            html = response.read().decode("utf-8", errors="replace")

        print(f"\n[+] HTTP Status: {status_code}")

        # 1. Security Headers
        sec = WebAuditClient.evaluate_security_headers(headers)
        print(f"\n[*] Security Headers Grade: {sec['grade']} ({sec['score_pct']}%)")
        print(f"    Passed: {sec['passed_checks']} / {sec['total_checks']} checks")
        for key, res in sec["details"].items():
            icon = "[PASS]" if res["status"] == "pass" else "[WARN]" if res["status"] == "warn" else "[FAIL]"
            val = f" [{res['value']}]" if res.get("value") else ""
            print(f"    {icon} {key.upper()}{val}: {res['recommendation']}")

        # 2. Markup Budget
        budget = WebAuditClient.evaluate_html_budget(html)
        print(f"\n[*] HTML Markup Budget:")
        print(f"    Transfer size: {budget['html_size_kb']} KB (Budget: <= {budget['budget_threshold_kb']} KB)")
        print(f"    Status: {'PASS (Lean HTML)' if budget['is_under_budget'] else 'WARN (Exceeds 150KB budget)'}")
        print(f"    H1 tags: {budget['h1_count']} (Single H1 valid: {budget['single_h1_valid']})")
        print(f"    Images missing alt: {budget['images_missing_alt_count']} / {budget['images_count']}")

        # 3. Robots.txt AI Check
        parsed = urllib.parse.urlparse(target_url)
        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
        try:
            r_req = urllib.request.Request(robots_url, headers={"User-Agent": "WebAudit-Scanner/1.0.0"})
            with urllib.request.urlopen(r_req, timeout=5) as r_resp:
                robots_txt = r_resp.read().decode("utf-8", errors="replace")
            ai_eval = WebAuditClient.evaluate_ai_crawlers_robots_txt(robots_txt)
            print(f"\n[*] AI Search Readiness (robots.txt):")
            print(f"    Allowed AI Crawlers: {ai_eval['allowed_bots']} / {ai_eval['total_evaluated_bots']}")
            print(f"    Friendly to Generative Search: {ai_eval['ai_search_friendly']}")
            for bot, b_res in ai_eval["crawlers"].items():
                b_icon = "[ALLOW]" if b_res["can_cite"] else "[BLOCK]"
                print(f"    {b_icon} {bot}: {b_res['access']}")
        except Exception as e:
            print(f"\n[!] robots.txt check skipped: {e}")

        print(f"\n==================================================")
        print(f"  Full Interactive Audit Hub: https://0audit.com/")
        print(f"==================================================\n")

    except Exception as err:
        print(f"Error fetching {target_url}: {err}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_cli_audit(sys.argv[1])
    else:
        client = WebAuditClient()
        print("WebAudit Client Initialized.")
        print("SEO Audit Hub:", client.get_hub_url("seo_audit"))
        print("Security Headers Hub:", client.get_hub_url("security_headers"))
        print("AI Search Hub:", client.get_hub_url("ai_search"))
        print("\nRun: python webaudit.py <url> to scan any public website.")
