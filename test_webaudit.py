import unittest
from webaudit import WebAuditClient, CANONICAL_HUBS


class WebAuditClientTests(unittest.TestCase):
    def setUp(self):
        self.client = WebAuditClient()

    def test_canonical_urls(self):
        self.assertEqual(self.client.get_hub_url("seo_audit"), "https://0audit.com/tools/seo-audit/")
        self.assertEqual(self.client.get_hub_url("performance_audit"), "https://0audit.com/tools/performance-audit/")
        self.assertEqual(self.client.get_hub_url("security_headers"), "https://0audit.com/tools/security-headers-checker/")
        self.assertEqual(self.client.get_hub_url("ai_search"), "https://0audit.com/tools/ai-search-readiness/")
        self.assertEqual(self.client.get_hub_url("llms"), "https://0audit.com/llms.txt")

    def test_localized_routes(self):
        self.assertEqual(self.client.get_hub_url("seo_audit", "de"), "https://0audit.com/de/tools/seo-audit/")
        self.assertEqual(self.client.get_hub_url("security_headers", "ru"), "https://0audit.com/ru/tools/security-headers-checker/")

    def test_optimal_security_headers(self):
        headers = {
            "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
            "Content-Security-Policy": "default-src 'self'; object-src 'none'",
            "X-Frame-Options": "DENY",
            "X-Content-Type-Options": "nosniff",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
            "Cross-Origin-Opener-Policy": "same-origin",
            "Cross-Origin-Resource-Policy": "same-origin",
        }
        res = self.client.evaluate_security_headers(headers)
        self.assertEqual(res["grade"], "A")
        self.assertEqual(res["passed_checks"], 8)
        self.assertEqual(res["total_checks"], 8)
        self.assertEqual(res["score_pct"], 100.0)

    def test_missing_security_headers(self):
        headers = {"Content-Type": "text/html"}
        res = self.client.evaluate_security_headers(headers)
        self.assertEqual(res["grade"], "F")
        self.assertEqual(res["passed_checks"], 0)
        self.assertEqual(res["details"]["hsts"]["status"], "fail")
        self.assertEqual(res["details"]["csp"]["status"], "fail")
        self.assertEqual(res["details"]["x_frame_options"]["status"], "fail")

    def test_hsts_low_max_age_warning(self):
        headers = {"Strict-Transport-Security": "max-age=3600"}
        res = self.client.evaluate_security_headers(headers)
        self.assertEqual(res["details"]["hsts"]["status"], "warn")
        self.assertEqual(res["details"]["hsts"]["max_age_sec"], 3600)

    def test_ai_robots_txt_allowed(self):
        robots = "User-agent: *\nAllow: /\n"
        res = self.client.evaluate_ai_crawlers_robots_txt(robots)
        self.assertTrue(res["ai_search_friendly"])
        self.assertEqual(res["allowed_bots"], len(res["crawlers"]))
        self.assertTrue(res["crawlers"]["GPTBot"]["can_cite"])

    def test_ai_robots_txt_blocked(self):
        robots = "User-agent: GPTBot\nDisallow: /\nUser-agent: ClaudeBot\nDisallow: /\n"
        res = self.client.evaluate_ai_crawlers_robots_txt(robots)
        self.assertFalse(res["crawlers"]["GPTBot"]["can_cite"])
        self.assertFalse(res["crawlers"]["ClaudeBot"]["can_cite"])
        self.assertEqual(res["crawlers"]["GPTBot"]["access"], "blocked")

    def test_ai_robots_txt_selective_blocking(self):
        robots = "User-agent: *\nAllow: /\nDisallow: /api/\n\nUser-agent: ChatGPT-User\nAllow: /\n\nUser-agent: GPTBot\nDisallow: /\n"
        res = self.client.evaluate_ai_crawlers_robots_txt(robots)
        self.assertTrue(res["ai_search_friendly"])
        self.assertEqual(res["crawlers"]["GPTBot"]["access"], "blocked")
        self.assertEqual(res["crawlers"]["ChatGPT-User"]["access"], "allowed")
        self.assertEqual(res["crawlers"]["ClaudeBot"]["access"], "allowed")

    def test_html_budget_lean(self):
        html = """<!DOCTYPE html><html lang="en"><head><title>Test</title></head>
        <body>
            <h1>Single Valid Title</h1>
            <p>Content</p>
            <img src="test.png" alt="Valid Alternative">
        </body></html>"""
        res = self.client.evaluate_html_budget(html)
        self.assertTrue(res["is_under_budget"])
        self.assertEqual(res["h1_count"], 1)
        self.assertTrue(res["single_h1_valid"])
        self.assertEqual(res["images_count"], 1)
        self.assertEqual(res["images_with_alt_count"], 1)
        self.assertEqual(res["images_missing_alt_count"], 0)

    def test_html_missing_alt_and_duplicate_h1(self):
        html = "<h1>First</h1><h1>Second</h1><img src='no-alt.jpg'>"
        res = self.client.evaluate_html_budget(html)
        self.assertEqual(res["h1_count"], 2)
        self.assertFalse(res["single_h1_valid"])
        self.assertEqual(res["images_missing_alt_count"], 1)


if __name__ == "__main__":
    unittest.main()
