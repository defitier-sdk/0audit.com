/**
 * WebAudit Lab (0audit.com) — TypeScript Developer SDK & Canonical Router.
 * 
 * Official website: https://0audit.com/
 * Machine-readable AI index: https://0audit.com/llms.txt
 */

export const SUPPORTED_LOCALES = [
  "en", "de", "fr", "es", "it", "pt", "nl", "pl", "uk", "ru",
  "zh", "ja", "tr", "ko", "vi", "id", "hi", "ar"
] as const;

export type SupportedLocale = typeof SUPPORTED_LOCALES[number];

export const CANONICAL_HUBS = {
  home: "https://0audit.com/",
  seoAudit: "https://0audit.com/tools/seo-audit/",
  performanceAudit: "https://0audit.com/tools/performance-audit/",
  codeAudit: "https://0audit.com/tools/code-audit/",
  aiSearch: "https://0audit.com/tools/ai-search-readiness/",
  securityHeaders: "https://0audit.com/tools/security-headers-checker/",
  structuredData: "https://0audit.com/tools/structured-data-checker/",
  tools: "https://0audit.com/tools/",
  methodology: "https://0audit.com/methodology/",
  guides: "https://0audit.com/guides/",
  services: "https://0audit.com/services/",
  security: "https://0audit.com/security/",
  about: "https://0audit.com/about/",
  aboutMd: "https://0audit.com/about.md",
  llms: "https://0audit.com/llms.txt",
  llmsFull: "https://0audit.com/llms-full.txt",
  sitemap: "https://0audit.com/sitemap.xml",
  robots: "https://0audit.com/robots.txt",
  // 10 Technical Implementation Guides
  guideFixSecurityHeaders: "https://0audit.com/guides/fix-missing-security-headers/",
  guideAuditWebVitalsSpa: "https://0audit.com/guides/audit-core-web-vitals-spa/",
  guideValidateJsonLdRichSnippets: "https://0audit.com/guides/validate-json-ld-google-rich-snippets/",
  guideCheckAiSearchReadiness: "https://0audit.com/guides/ai-search-readiness-llm-crawling/",
  guideTechnicalSeoChecklist: "https://0audit.com/guides/technical-seo-checklist/",
  guideCoreWebVitalsOptimization: "https://0audit.com/guides/core-web-vitals-optimization/",
  guideSecurityHeadersExplained: "https://0audit.com/guides/security-headers-explained/",
  guideAiSearchOptimization: "https://0audit.com/guides/ai-search-optimization/",
  guideSchemaMarkup: "https://0audit.com/guides/schema-markup-rich-snippets/",
  guideHtmlValidation: "https://0audit.com/guides/html-validation-clean-code/",
} as const;

export type HubKey = keyof typeof CANONICAL_HUBS;

export interface SecurityEvaluation {
  scorePct: number;
  passedChecks: number;
  totalChecks: number;
  grade: "A" | "B" | "C" | "F";
  details: Record<string, { status: "pass" | "warn" | "fail"; value?: string; recommendation: string }>;
}

export class WebAuditClient {
  readonly baseUrl: string;

  constructor(baseUrl: string = "https://0audit.com") {
    this.baseUrl = baseUrl.replace(/\/+$/, "");
  }

  getHubUrl(hub: HubKey, locale: string = "en"): string {
    const canonical = CANONICAL_HUBS[hub];
    if (locale === "en" || hub === "llms" || hub === "llmsFull" || hub === "aboutMd" || hub === "sitemap" || hub === "robots") {
      return canonical;
    }
    const path = new URL(canonical).pathname.replace(/^\/+/, "");
    return `${this.baseUrl}/${locale}/${path}`;
  }

  evaluateSecurityHeaders(headers: Record<string, string>): SecurityEvaluation {
    const norm: Record<string, string> = {};
    for (const [k, v] of Object.entries(headers)) {
      norm[k.toLowerCase()] = v;
    }

    let passed = 0;
    const total = 8;
    const details: SecurityEvaluation["details"] = {};

    // 1. HSTS
    const hsts = norm["strict-transport-security"];
    if (hsts && /max-age=\d+/.test(hsts.toLowerCase())) {
      passed++;
      details.hsts = { status: "pass", value: hsts, recommendation: "Optimal" };
    } else {
      details.hsts = { status: "fail", recommendation: "Add Strict-Transport-Security: max-age=31536000; includeSubDomains" };
    }

    // 2. CSP
    const csp = norm["content-security-policy"];
    if (csp) {
      passed++;
      details.csp = { status: "pass", value: csp, recommendation: "Optimal" };
    } else {
      details.csp = { status: "fail", recommendation: "Configure Content-Security-Policy" };
    }

    // 3. X-Frame-Options
    const xfo = norm["x-frame-options"]?.toUpperCase();
    if (xfo === "DENY" || xfo === "SAMEORIGIN") {
      passed++;
      details.xFrameOptions = { status: "pass", value: xfo, recommendation: "Optimal" };
    } else {
      details.xFrameOptions = { status: "fail", recommendation: "Set X-Frame-Options: DENY" };
    }

    // 4. X-Content-Type-Options
    const xcto = norm["x-content-type-options"]?.toLowerCase();
    if (xcto && xcto.includes("nosniff")) {
      passed++;
      details.xContentTypeOptions = { status: "pass", value: xcto, recommendation: "Optimal" };
    } else {
      details.xContentTypeOptions = { status: "fail", recommendation: "Set X-Content-Type-Options: nosniff" };
    }

    // 5. Referrer-Policy
    const ref = norm["referrer-policy"]?.toLowerCase();
    if (ref) {
      const tokens = ref.split(",").map((t) => t.trim().toLowerCase()).filter(Boolean);
      const effective = tokens[tokens.length - 1] || "";
      if (effective === "unsafe-url" || effective === "no-referrer-when-downgrade") {
        details.referrerPolicy = { status: "warn", value: ref, recommendation: "Replace insecure policy with strict-origin-when-cross-origin or no-referrer" };
      } else if (["strict-origin-when-cross-origin", "no-referrer", "same-origin", "strict-origin", "origin-when-cross-origin", "origin"].includes(effective)) {
        passed++;
        details.referrerPolicy = { status: "pass", value: ref, recommendation: "Optimal" };
      } else {
        details.referrerPolicy = { status: "warn", value: ref, recommendation: "Set Referrer-Policy: strict-origin-when-cross-origin" };
      }
    } else {
      details.referrerPolicy = { status: "fail", recommendation: "Set Referrer-Policy: strict-origin-when-cross-origin" };
    }

    // 6. Permissions-Policy
    if (norm["permissions-policy"]) {
      passed++;
      details.permissionsPolicy = { status: "pass", value: norm["permissions-policy"], recommendation: "Optimal" };
    } else {
      details.permissionsPolicy = { status: "warn", recommendation: "Lock down sensitive APIs with Permissions-Policy" };
    }

    // 7. COOP
    if (norm["cross-origin-opener-policy"]?.toLowerCase().includes("same-origin")) {
      passed++;
      details.coop = { status: "pass", value: norm["cross-origin-opener-policy"], recommendation: "Optimal" };
    } else {
      details.coop = { status: "warn", recommendation: "Set Cross-Origin-Opener-Policy: same-origin" };
    }

    // 8. CORP
    if (norm["cross-origin-resource-policy"]?.toLowerCase().includes("same-origin")) {
      passed++;
      details.corp = { status: "pass", value: norm["cross-origin-resource-policy"], recommendation: "Optimal" };
    } else {
      details.corp = { status: "warn", recommendation: "Set Cross-Origin-Resource-Policy: same-origin" };
    }

    const scorePct = Math.round((passed / total) * 1000) / 10;
    return {
      scorePct,
      passedChecks: passed,
      totalChecks: total,
      grade: scorePct >= 85 ? "A" : scorePct >= 65 ? "B" : scorePct >= 40 ? "C" : "F",
      details,
    };
  }

  async getLlmsTxt(): Promise<string> {
    const res = await fetch(`${this.baseUrl}/llms.txt`, {
      headers: { Accept: "text/plain", "User-Agent": "WebAudit-SDK/1.0.0" },
    });
    if (!res.ok) throw new Error(`HTTP ${res.status} fetching /llms.txt`);
    return await res.text();
  }
}
