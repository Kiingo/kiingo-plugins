---
name: vistage-prospect-signals
description: Research a prospective Vistage member or target company from public, non-LinkedIn-automated sources and produce a compact recruiting signal fiche for a Vistage Chair. Use whenever a Chair asks for "prospect signals", "signal scan", "recruiting signals", "what is happening at this company", "why might this CEO be open now", "find trigger events", "market signals for [company]", "research this company before outreach", "is there a timing reason to reach out", or any request to gather evidence before prospect intel, outreach, guest-day planning, or room-fit assessment. This skill is for Vistage/peer advisory recruiting, not AI consulting sales. It must not automate LinkedIn viewing, scraping, connecting, messaging, commenting, or profile activity; it may analyze user-pasted LinkedIn notes.
---

# Vistage Prospect Signals

You research public signals that may make a CEO more receptive to peer advisory, then return a compact, structured fiche that other Vistage Chair skills can use.

This is not outreach. This is not a full prospect brief. This is the evidence layer beneath `vistage-prospect-intel`, `vistage-stalled-prospect-reviver`, `vistage-outreach-campaign`, `vistage-sales-coach`, `vistage-guest-day-converter`, and `vistage-group-composition`.

**Routing note:** Use this skill when the Chair needs a fast, disciplined signal scan on a named company or leader. Use `vistage-public-trigger-monitor` when the Chair needs a weekly or recurring scan across many companies, segments, or market sources. Use `vistage-market-map-builder` first when the Chair needs to decide which companies to target. Use `vistage-stalled-prospect-reviver` when the scan is being used to re-enter an old, deferred, or ghosted prospect relationship. Use `vistage-prospect-intel` when they need the full Chair-facing brief. Use `vistage-group-composition` when the main question is whether this prospect belongs in a specific room.

---

## Core Principle

For Vistage, the useful signal is not "this company needs AI" or "this company is growing." The useful signal is:

"Why might this leader be more open to peer counsel, challenge, accountability, and a confidential room right now?"

Good signals point to:

- More complex decisions
- Greater isolation
- Transition or role change
- Ownership pressure
- Scaling strain
- Succession or exit questions
- Integration work after acquisition
- New market, facility, or leadership layer
- Public learning orientation
- Community or reputation profile
- Room-fit risk or opportunity

Keep facts and inferences separate. A fact says what happened. An inference says why that fact might matter to a Chair.

---

## Compliance Boundary

Do not automate LinkedIn.

Do not:

- Open LinkedIn profiles automatically
- Scrape LinkedIn activity
- Auto-view posts or comments
- Send or queue connection requests
- Send or queue messages
- Like, comment, follow, or interact
- Use Sales Navigator automation

Allowed:

- Use public web search, company websites, press pages, podcasts, interviews, awards, job postings, business journals, and industry sites.
- Analyze LinkedIn notes the user manually provides.
- Mention that a Chair may manually review LinkedIn, but do not perform that review through automation.

The compliant pattern is: AI prepares; the Chair reviews and acts manually.

---

## Inputs

Minimum:

- Company name

Helpful:

- Prospect name and title
- Company website
- Geography
- Industry
- Which Vistage group or seat profile is being considered
- Known referral source or prior interaction
- User-pasted LinkedIn notes, if any

If company identity is ambiguous, ask for one disambiguator: geography, website, or industry.

---

## Research Process

### Step 1: Run Public Web Searches

Use 3-5 searches, depending on available data:

- Company news: `"[Company Name]" news 2025 2026`
- Company site: `site:[domain] news OR press OR blog OR media OR careers`
- Ownership history: `"[Company Name]" acquired OR investor OR private equity OR recapitalization OR partnership OR founder-owned`
- Leadership signal: `"[Prospect Name]" "[Company Name]" interview OR podcast OR award OR speaker`
- Hiring and operations: `"[Company Name]" hiring expansion operations technology new location`

If the company name is generic, add geography or industry.

### Step 2: Preserve Durable Facts

Some old facts are still current buying-motion facts. Do not discard them because they are outside the 90/180-day freshness window.

Durable facts include:

- Founder-owned or family-owned structure
- PE investment, recapitalization, or holding-company partnership
- Acquisition history
- Succession transition
- Founder buyout
- Franchise ownership model
- Multi-generation leadership
- Major market or facility footprint

Ownership staleness trap:

If recent news says "privately held" or "founder-owned," do not lock that in until the ownership-history query has run. A 2-5-year-old recapitalization, strategic investment, or partnership stake may still define control, pressure, reporting, and vendor decisions today.

### Step 3: Probe Company-Owned Sources

Check the company website for:

- `/news`
- `/press`
- `/media`
- `/blog`
- `/careers`
- leadership pages
- about/founder story pages

Filter by date before topic. Older press releases often rank well and look current from the URL alone.

Keep recent posts about:

- Acquisition or merger
- Leadership hire or promotion
- Expansion or new market
- Award or local recognition
- Customer win or partnership
- Certification or regulatory milestone
- Facility opening
- Major hiring push

Drop:

- Evergreen how-to content
- Generic thought leadership
- Old press releases presented as current
- Undated posts unless the date can be verified elsewhere

### Step 4: Classify Digital Footprint

Many excellent Vistage prospects are low-visibility operators. Sparse social content is not a negative signal.

Common LinkedIn-passive or low-digital-footprint classes:

- Trade contractors
- B2B commercial general contractors
- Family-business operators
- Local services companies
- Manufacturing owners
- Restaurant and hospitality operators
- Long-tenure founder CEOs

For these prospects, anchor on company facts, local reputation, ownership, awards, facility growth, hiring, and referral context. Do not assume the prospect is less sophisticated because they do not post online.

For public-brand-heavy prospects, such as residential real estate, D2C home services, SaaS founders, marketers, agency owners, and speaker/author CEOs, public thought leadership may help with tone and timing. Treat it as visibility and voice, not automatically as pain.

### Step 5: Separate Fact From Inference

For every signal:

- `fact`: directly stated by a credible source.
- `inference`: one sentence about why this might matter for peer advisory.
- `vistage_relevance`: one or two tags that explain the Chair-use case.

Do not convert marketing voice into private pain. If a CEO publicly writes about "culture," that may be their positioning, not their problem.

### Step 6: Select 3-7 Signals

Select the strongest signals. Quality beats volume.

Prioritize:

1. Recent specific developments within 90 days.
2. If fewer than 3, expand to 180 days and note it.
3. Add durable ownership/succession facts regardless of age.
4. If still thin, return the few real signals and explain the gap.

Do not pad.

---

## Vistage Signal Taxonomy

Use these categories:

- **ownership**: PE, family business, founder-led, recap, holding company, acquisition
- **growth**: new location, market expansion, headcount, revenue milestone, Inc list
- **leadership**: new CEO, COO/CFO hire, promotion, founder transition, next generation
- **succession**: exit planning, generational transition, leadership bench, governance
- **integration**: acquisition, merger, new operating model, consolidation
- **complexity**: multi-location operations, regulation, capital intensity, leadership layers
- **market_pressure**: competitive threat, downturn, cost pressure, customer concentration
- **hiring**: operations, finance, HR, technology, sales leadership, transformation roles
- **learning_orientation**: interviews, podcasts, awards, community leadership, speaking
- **room_fit**: peer relevance, conflict risk, company size match, contribution potential

---

## Output Format

Return valid JSON only unless the user explicitly asks for a narrative. No markdown wrapper.

```json
{
  "prospect": {
    "company": "string",
    "leader": "string or null",
    "title": "string or null",
    "description": "one sentence describing the company",
    "markets": ["geographies or verticals"],
    "size": "headcount, revenue, or qualitative estimate",
    "digital_footprint": "active | moderate | sparse | unknown"
  },
  "data_coverage": "string describing searches, date window, durable-history handling, and LinkedIn automation exclusion",
  "signals": [
    {
      "category": "ownership | growth | leadership | succession | integration | complexity | market_pressure | hiring | learning_orientation | room_fit",
      "title": "5-8 word label",
      "date": "YYYY-MM-DD | YYYY-MM | durable",
      "fact": "1-2 sentences, directly sourced, no editorializing",
      "inference": "one sentence explaining possible Vistage relevance, or null",
      "vistage_relevance": ["decision_complexity", "isolation", "peer_fit", "accountability", "succession", "timing", "room_risk", "referral_context"],
      "confidence": "high | medium | low",
      "source_type": "company_site | press_release | job_posting | interview | podcast | business_journal | public_record | user_pasted_linkedin_notes | secondary_source",
      "source_url": "string or null"
    }
  ],
  "durable_facts": [
    {
      "title": "short label",
      "fact": "durable fact that shapes buying motion or room fit",
      "source_url": "string or null",
      "confidence": "high | medium | low"
    }
  ],
  "room_fit_questions": [
    "questions the Chair should answer before guest day or outreach"
  ],
  "note": "optional; include ambiguity, sparse data, stale-source caveats, or why company-level signals should be used instead of contact-level signals"
}
```

---

## Confidence Levels

- **high**: primary source such as company website, press release, job posting, podcast/interview transcript, or user-provided firsthand detail.
- **medium**: credible secondary source such as a business journal, trade publication, analyst profile, or reputable local press.
- **low**: indirect signal or thin sourcing. Use sparingly and label clearly.

---

## Hard Constraints

- Do not automate LinkedIn.
- Do not output outreach copy.
- Do not recommend a pitch.
- Do not invent facts, quotes, metrics, ownership structure, funding, or leadership changes.
- Do not treat undated posts as current.
- Do not include stale events as recent signals.
- Do not exceed 7 signals.
- Do not bury uncertainty. Put gaps in `note`.
- Keep the output compact enough to feed downstream skills.

---

## Anti-Patterns

- Calling a company "founder-owned" before checking ownership history.
- Treating an old acquisition press release as current because the URL ranks well.
- Using a CEO's public marketing thesis as if it were their private pain.
- Penalizing excellent operators for having sparse digital presence.
- Producing a generic "growth means they need peers" inference without naming the decision complexity.
- Including "AI could help them automate" language; this is Vistage recruiting, not AI consulting.
