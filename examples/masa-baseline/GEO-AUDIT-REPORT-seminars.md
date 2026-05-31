# GEO Audit Report: MASA Seminars

**Audit Date:** 2026-05-31
**URL:** https://www.masaseminars.com
**Business Type:** Event lead-gen / seminar registration microsite
**Pages Analyzed:** 9 (complete site — homepage, about-us, faqs, events, contact-us, plus utility pages)

---

## Executive Summary

**Overall GEO Score: 39/100 (Critical)**

masaseminars.com is essentially invisible to AI systems. The site has 9 pages, no structured data of any kind, no llms.txt, no AI crawler permissions, and content so thin that there is almost nothing for AI systems to cite or index. This is expected for a microsite whose sole purpose is event registration — but it represents a significant missed opportunity, because "free MASA seminar" and "MASA lunch seminar" are exactly the types of local queries that AI-powered search (Google AI Overviews, Perplexity local search) is beginning to handle. Without Event schema, this site's seminars will never appear in AI-generated event discovery responses.

The site's GEO gap is structural, not content-quality-based. The fixes are fast and high-impact relative to the effort required.

### Score Breakdown

| Category | Score | Weight | Weighted Score |
|---|---|---|---|
| AI Citability | 32/100 | 25% | 8.0 |
| Brand Authority | 52/100 | 20% | 10.4 |
| Content E-E-A-T | 38/100 | 20% | 7.6 |
| Technical GEO | 48/100 | 15% | 7.2 |
| Schema & Structured Data | 18/100 | 10% | 1.8 |
| Platform Optimization | 40/100 | 10% | 4.0 |
| **Overall GEO Score** | | | **39/100** |

---

## Critical Issues (Fix Immediately)

### C1 — No llms.txt file
**URL:** https://www.masaseminars.com/llms.txt → 404
**Impact:** AI crawlers have no machine-readable document explaining what MASA seminars are, who they're for, where they take place, or how they relate to MASA Global membership. Without it, AI assistants asked "how can I learn about MASA?" or "are there MASA seminars near me?" have no authoritative source.
**Fix:** Create a concise llms.txt specific to the seminar channel (see template below).

### C2 — No schema of any kind detected on any page
**Pages checked:** All 9 pages
**Impact:** No Organization, Event, FAQPage, or BreadcrumbList schema. This is the most acute gap: the Events page lists (when populated) physical events with dates, locations, and registration — exactly what Event schema is designed to mark up. Google AI Overviews and Google's event discovery features depend entirely on Event schema to surface local events.
**Fix:** Implement Event schema on all event listing pages; Organization schema on homepage; FAQPage schema on /faqs.

### C3 — No FAQPage schema on /faqs despite 11 questions
**URL:** https://www.masaseminars.com/faqs
**Impact:** 11 FAQ questions with no schema markup. These are directly answerable questions ("Is there a cost to attend?", "How long is the seminar?", "Can I bring a guest?") that AI systems would cite if structured correctly.
**Fix:** Add FAQPage JSON-LD to /faqs.

---

## High Priority Issues

### H1 — No Event schema on the events page
**URL:** https://www.masaseminars.com/events
**Impact:** This is the highest-value schema opportunity on the site. When events are scheduled, each event has a name, date, time, location, and registration URL — exactly the fields Event schema requires. Without it, MASA seminars cannot appear in:
- Google's event rich results
- Google AI Overviews for "MASA seminar near me" queries
- Perplexity local event responses
- AI calendar integration features

**Sample Event JSON-LD template:**
```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "MASA Free Lunch Seminar — [City, State]",
  "description": "Free 60–90 minute lunch seminar on emergency medical transportation coverage. Learn how MASA protects you from $69,000 air ambulance bills. Lunch included at no cost.",
  "startDate": "[ISO 8601 datetime]",
  "endDate": "[ISO 8601 datetime]",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "location": {
    "@type": "Place",
    "name": "[Venue Name]",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "[Street]",
      "addressLocality": "[City]",
      "addressRegion": "[State]",
      "postalCode": "[ZIP]",
      "addressCountry": "US"
    }
  },
  "organizer": {
    "@type": "Organization",
    "name": "MASA Global",
    "url": "https://www.masaseminars.com"
  },
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "[Registration URL]"
  },
  "image": "[Event image URL]"
}
```

This template should be dynamically generated for each scheduled event.

### H2 — No AI crawler permissions in robots.txt
Same issue as masaaccess.com. robots.txt only blocks HubSpot preview paths; no AI crawler permissions, no sitemap reference.
**Fix:** Add GPTBot, ClaudeBot, PerplexityBot allow rules and `Sitemap: https://masaseminars.com/sitemap.xml`.

### H3 — Separate domain dilutes MASA brand authority
masaseminars.com operates as a completely separate domain from masaaccess.com with no visible cross-linking (homepage was analyzed and no link to masaaccess.com was found). From an AI entity recognition standpoint, MASA's authority is split across two domains with no explicit organizational relationship signaled in schema.
**Fix:** Add `Organization` schema to masaseminars.com homepage with `sameAs` linking to masaaccess.com: `"sameAs": "https://www.masaaccess.com"`. Also add explicit footer link: "MASA seminars are offered by MASA Global — masaaccess.com."

### H4 — Homepage has no meta description
AI crawlers and search engines use meta descriptions as a content signal. The homepage has no meta description.
**Fix:** Add: "Find a free MASA lunch seminar near you. Learn how to protect your family from emergency ambulance bills — no cost to attend. Search events by location."

---

## Medium Priority Issues

### M1 — llms.txt content specification for masaseminars.com
When created, the llms.txt should be brief and cross-reference masaaccess.com:

```
# MASA Seminars

> MASA seminars are free educational lunch events where MASA representatives
> present emergency medical transportation coverage to prospective members.
> masaseminars.com is the event registration site for MASA Global (masaaccess.com).

## What MASA Seminars Are
- Free 60–90 minute lunch-and-learn events
- Presented by MASA sales representatives
- Topics: emergency ground and air ambulance costs, MASA membership benefits, how to enroll
- No purchase required to attend
- Guests welcome (adults 26+ only; Medicaid recipients cannot enroll)

## Who Should Attend
Adults concerned about emergency medical transport costs. Particularly relevant for
those aged 45+, frequent travelers, retirees, and families with aging parents.

## How to Register
Search for events at https://masaseminars.com/events or call 855-786-2053.
Email: rsvp@masaseminars.com

## About MASA
MASA (Medical Access & Service Advantage) is a membership organization providing
emergency medical transportation coverage. Full product details at masaaccess.com.

## State Availability
MASA membership is not available in: AK, DE, DC, KY, IA, MA, MD, MI, MT, NH, NM,
ND, NY, NJ, PA, SC, UT, WA, WV, RI.
```

### M2 — Content is too thin for AI citation (32 citability score)
The site has almost no substantive content — most pages are 100–300 words. FAQ answers are 1–2 sentences. This is appropriate for a microsite but limits AI citation value.
**Priority fix:** The FAQ page is the best candidate for expansion. Longer answers (100+ words) to the product-level questions ("What is MASA?", "What does it cost?") would meaningfully improve citability.

### M3 — No Organization schema with cross-domain sameAs
See H3 above. The organizational relationship between masaseminars.com and masaaccess.com is invisible to AI systems without explicit schema linking.

---

## Low Priority Issues

### L1 — Limited social media presence
Only Facebook is referenced. No YouTube, Instagram, LinkedIn, or Twitter/X.

### L2 — No video content on the site
Testimonials mention "interactive" presentations but there's no video of a seminar, presenter, or testimonial on the site itself. Video builds trust and improves E-E-A-T signals.

### L3 — BreadcrumbList schema absent
Minor but easy to implement in HubSpot.

---

## Category Deep Dives

### AI Citability — 32/100
The site has very little content for AI systems to cite. The homepage has good cost statistics ("emergency ambulance bills," "2 million members") but they're embedded in sparse copy without the self-contained passage structure AI models prefer. FAQ answers are 1–2 sentences each — unusable as citation blocks. The events page is dynamic/empty. The About-us page is a brief mission statement.

The single highest-citability element is the state availability list on the Contact page — a specific, factual list of 19 excluded jurisdictions that AI systems could cite for "Is MASA available in [state]?" queries.

### Brand Authority — 52/100
The ABC/NBC/CBS media mentions are the strongest brand authority signal on this site — these are genuine third-party credibility markers that AI models weight heavily. BBB and Google Reviews logos reinforce this. The "2 million members" stat is a significant authority signal.

Weakness: masaseminars.com is a separate domain with no explicit organizational connection to masaaccess.com in schema or content. AI systems evaluating MASA's brand authority are working with split signals across two domains.

### Content E-E-A-T — 38/100
No author attribution, no presenter credentials, no medical or financial advisory input, no external citations. The About-us page has organizational credibility signals (50 years, 2M members) but names no individuals. Testimonials quote attendees generically ("the presenter").

This is expected for a microsite but the E-E-A-T gap limits the site's authority in AI evaluations.

### Technical GEO — 48/100
HubSpot CMS provides a solid technical foundation. HTTPS, clean URLs, and basic accessibility are presumably in place. The robots.txt is minimal (HubSpot defaults only). No sitemap reference in robots.txt. No AI crawler permissions. No meta description on homepage. These are all quick fixes.

### Schema & Structured Data — 18/100
The lowest-scoring dimension. No JSON-LD detected on any of the 9 pages. The site has three clear schema opportunities that are completely unimplemented:
1. **Event schema** — highest value; enables AI and Google event discovery
2. **FAQPage schema** — 11 questions waiting for markup
3. **Organization schema** — establishes MASA as a recognized entity with sameAs cross-reference to masaaccess.com

The 18/100 score reflects that the site structure and content are technically appropriate for schema — the markup just hasn't been added.

### Platform Optimization — 40/100
Limited but not zero. Facebook is present. ABC/NBC/CBS mentions suggest local TV presence that AI training data may have captured. No YouTube, Reddit, or Wikipedia presence confirmed for the seminar channel. The site's microsite nature limits platform footprint organically.

---

## Quick Wins (This Week)

1. **Add Event schema to the events page** — dynamically generate JSON-LD for each scheduled event using the template above. This is the single highest-GEO-impact fix on the site.
2. **Add FAQPage JSON-LD to /faqs** — 11 questions, 30-minute implementation.
3. **Add Organization schema to homepage** with `sameAs: "https://www.masaaccess.com"` — links the two domains.
4. **Update robots.txt** — AI crawler permissions + sitemap URL.
5. **Add meta description to homepage** — 30 seconds in HubSpot.

---

## 30-Day Action Plan

### Week 1: Schema foundations
- [ ] Add Organization schema to homepage (with sameAs masaaccess.com)
- [ ] Add FAQPage schema to /faqs
- [ ] Add Event schema template (ready to populate when events are scheduled)
- [ ] Update robots.txt: AI crawlers + sitemap URL
- [ ] Add homepage meta description

### Week 2: llms.txt + cross-domain linking
- [ ] Publish llms.txt at masaseminars.com/llms.txt (spec in M1 above)
- [ ] Add explicit footer link to masaaccess.com: "Join MASA online at masaaccess.com"
- [ ] Add "Can't find an event? Enroll online at masaaccess.com/compare-plans/" to events zero-results state

### Week 3: Content depth
- [ ] Expand FAQ answers to 100+ words for product-level questions
- [ ] Add presenter bio section to About-us page
- [ ] Add video content (even a 60-second explainer) to homepage

### Week 4: Verification
- [ ] Verify schema with Google Rich Results Test
- [ ] Verify llms.txt is accessible and correctly formatted
- [ ] Confirm AI crawlers are successfully accessing the site
- [ ] Run a follow-up GEO spot-check

---

## Appendix: Pages Analyzed

| URL | Status | Schema | GEO Issues |
|-----|--------|--------|------------|
| https://masaseminars.com | 200 | None | No schema, no meta description, no llms.txt |
| https://masaseminars.com/about-us | 200 | None | No schema, no individual credentials |
| https://masaseminars.com/faqs | 200 | None | 11 questions, no FAQPage schema |
| https://masaseminars.com/events | 200 | None | No Event schema; 0 events currently listed |
| https://masaseminars.com/contact-us | 200 | None | No LocalBusiness schema; state exclusions not visible |
| https://masaseminars.com/llms.txt | 404 | N/A | Does not exist |
| https://masaseminars.com/sitemap.xml | 200 | N/A | 9 URLs; not referenced in robots.txt |
| https://masaseminars.com/robots.txt | 200 | N/A | No AI crawlers, no sitemap reference |

---

*Generated by GEO Audit Suite — `/geo audit` | Baseline audit for masaseminars.com | 2026-05-31*
