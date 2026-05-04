---
name: vistage-public-trigger-monitor
description: Build and run a public-web trigger monitoring workflow for Vistage Chair recruitment. Use whenever a Chair asks to monitor public triggers, watch local companies, scan business news, track prospect timing, find CEO trigger events, create a weekly trigger digest, watch a market map, monitor target companies, set up Google Alerts/business journal scans, identify reasons to reach out, or decide which public events should trigger referral asks, prospect signals, prospect intel, outreach, guest invitations, or nurture. This skill uses public sources only and must not automate LinkedIn profile viewing, scraping, messaging, connecting, commenting, liking, or other social activity.
---

# Vistage Public Trigger Monitor

You help a Vistage Chair watch the market for public events that make the right CEO more receptive to a peer advisory conversation.

This is not a news clipping service. The Chair needs a practical weekly decision tool:

- What happened?
- Is it real, recent, and relevant?
- Does it suggest complexity, isolation, transition, or learning orientation?
- Is there a warm path?
- Should the Chair act this week, ask for a referral, run a signal scan, nurture, or ignore it?

This skill sits after `vistage-market-map-builder` and before `vistage-chair-authority-builder`, `vistage-stalled-prospect-reviver`, `vistage-prospect-signals`, `vistage-referral-source-briefs`, `vistage-referral-activation-engine`, `vistage-prospect-intel`, and `vistage-outreach-campaign`.

**Routing note:** Use this skill to monitor a market, segment, or target list over time. Use `vistage-chair-authority-builder` when trigger clusters should become content, talks, advisor briefings, or roundtable topics. Use `vistage-stalled-prospect-reviver` when a trigger belongs to an old, deferred, or ghosted prospect. Use `vistage-prospect-signals` for a deeper signal fiche on one named company. Use `vistage-referral-source-briefs` when the trigger points to a specific source to ask. Use `vistage-referral-activation-engine` when the trigger reveals a warm source or intro ask. Use `vistage-outreach-campaign` only after the Chair knows the target, trigger, source path, and desired ask.

---

## Core Wisdom

Public triggers are not excuses to pounce. They are timing clues.

A public announcement often points to private leadership pressure:

- Expansion can mean delegation strain.
- Acquisition can mean integration, identity, and control questions.
- A new COO/CFO can mean professionalization.
- A founder transition can mean succession, legacy, and role confusion.
- Awards can mean visibility, growth, and openness to peer recognition.
- Hiring spikes can mean systems are being stretched.
- PE backing can mean reporting cadence, growth pressure, and board scrutiny.

The Chair should use the trigger to create relevance, not pressure. The best move is often not direct outreach; it is asking the right member, banker, attorney, CPA, or community connector:

"Do you know [Name] well enough to make a thoughtful intro? This looks like the kind of transition where a confidential CEO room could be useful."

---

## Compliance Boundary

Do not automate LinkedIn.

Allowed:

- Public web search
- Company websites, press pages, blogs, careers pages
- Business journal and local news searches
- Chamber, association, award, event, and nonprofit pages
- Public PE portfolio pages and M&A announcements
- Public job postings and hiring pages
- Chair-provided LinkedIn notes or manually exported target lists
- Drafting manual search queries, alerts, digests, and outreach/referral recommendations

Not allowed:

- Automated LinkedIn profile viewing
- Automated LinkedIn scraping or Sales Navigator scraping
- Automated connection requests or messages
- Automated likes, comments, follows, or profile visits
- Treating user-provided LinkedIn notes as if they were independently verified public facts

If LinkedIn could help, phrase it as a manual Chair step.

---

## Inputs

Ask only for what is missing.

Minimum:

- Geography or market
- Group type and target member profile
- Monitor scope: named companies, priority segments, or both
- Time budget: 30-minute weekly scan, 2-hour weekly scan, or deeper monthly review

Helpful:

- Market map or target-company list
- Open seats and seat thesis
- Current members and conflict constraints
- Referral source map
- Business journal or local publication access
- Existing Google Alerts, saved searches, or CRM fields
- CRM/spreadsheet preference

If the Chair has no market map, use `vistage-market-map-builder` first.

---

## Starting Mode Selector

First classify the monitor. Different Chair situations need different watches.

| Mode | Signals | Primary Output |
|------|---------|----------------|
| New Chair / first group | No watchlist, broad market, unclear trigger thesis | 3-5 priority segments, starter sources, first 30-day scan plan |
| Existing group open-seat | Current room has specific gaps | Seat-specific triggers, conflict watchlist, top weekly actions |
| Named-company watchlist | Market map has A/B targets | Company trigger digest and access-weighted action list |
| Segment-specific monitor | Chair wants manufacturing, trades, family business, etc. | Source density check and segment trigger digest |
| Advisor-source monitor | Chair recruits through CPAs, attorneys, bankers, brokers | Source prompts plus client-facing trigger types |
| Second-group monitor | Existing group should not be diluted | Separate thesis, separate sources, distinct conflict rules |
| Stalled recruiting | Lots of activity, few conversations | Noisy-source pruning and higher-access action plan |

If the Chair does not specify the mode, infer it and state the assumption.

### Trigger Thesis Builder

Before scanning, define what would make a trigger worth action:

- **Watched universe:** companies, segments, geography, and excluded conflicts.
- **Trigger types:** expansion, leadership change, acquisition, award, hiring, succession, event, ownership.
- **Complexity threshold:** enough employees, locations, leadership layers, capital intensity, or role pressure for peer advisory to matter.
- **Disqualifiers:** direct conflict, reputation risk, low complexity, too junior, too sensitive to mention.
- **Access hypothesis:** member, advisor, event, community, content, or direct path.
- **Room-value hypothesis:** what this leader would add to the room.

Trigger thesis test:

"Would this public event justify a thoughtful Chair action this week?"

If not, monitor it as context or ignore it.

---

## Step 2: Choose Public Sources

Use source types matched to the market.

High-yield sources include company `/news`, `/press`, `/media`, `/blog`, `/careers`, leadership and events pages; local business journals; People on the Move; chambers; economic development groups; associations; Inc. 5000 and local award lists; M&A/PE/ESOP announcements; commercial real estate and permits; job postings; event speaker/sponsor lists; nonprofit boards; podcasts; interviews; and trade publications.

For low-digital-footprint operators, favor local news, trade associations, contractor or licensing awards where appropriate, permits, supplier/customer ecosystem pages, and member/advisor intelligence.

Avoid turning the monitor into general news scanning. Every source should connect to the Chair's seat thesis.

### Monitor Setup Recipes

Give the Chair a runnable setup, not just source theory.

| Recipe | Setup |
|--------|-------|
| Google Alerts | Create alerts for top companies, priority segments + city, `"CEO" "expansion" "[city]"`, `"president" "acquired" "[city]"`, and `"family business" "[city]" succession` |
| Business journal | Save searches for People on the Move, fastest-growing, M&A, expansions, awards, and private companies |
| Company pages | Bookmark `/news`, `/press`, `/media`, `/blog`, `/careers`, leadership, and events pages for A targets |
| Job posting check | Watch COO, CFO, controller, VP operations, HR, sales leader, GM, plant manager, and president roles |
| Award lists | Track fastest-growing, best places to work, family business, innovation, industry, and community leadership lists |
| Association/chamber | Watch board appointments, sponsors, speaker lists, new members, and event panels |
| Advisor feed | Ask bankers, CPAs, attorneys, brokers, and fractional CFOs what changes they are seeing in the segment |

For a 30-minute weekly scan, use 3-5 sources. For a 2-hour scan, use 8-12 sources plus named-company checks. Do not monitor more sources than the Chair can act on.

### Signal Density Check

Classify the monitor's source quality like a market map density check:

- **Too quiet:** few triggers after several scans. Add sources, broaden segment, or rely more on advisors.
- **Focused:** manageable trigger flow tied to the seat thesis. Keep cadence.
- **Broad:** too many items. Narrow by ownership, size, geography, or trigger type.
- **Noisy:** many articles but weak fit. Prune sources and tighten action threshold.
- **Low-trust:** signals are hard to verify. Use only as research prompts.

---

## Step 3: Use Search Patterns

Build reusable queries. Add geography, industry, or company names when needed.

Company queries:

- `"[Company]" acquisition OR acquired OR merger OR investor OR private equity`
- `"[Company]" expansion OR "new location" OR facility OR headquarters`
- `"[Company]" CEO OR president OR founder OR COO OR CFO`
- `"[Company]" award OR "fastest growing" OR "best places to work"`
- `site:[domain] news OR press OR careers OR leadership`

Market queries:

- `"[city]" "fastest growing companies" CEO`
- `"[city]" "People on the Move" CEO president founder`
- `"[city]" manufacturer expansion president`
- `"[industry]" "[city]" acquisition CEO`
- `"[city]" "family business" award CEO`
- `"[industry]" association "[city]" board president`

Advisor-path queries:

- `"[city]" CPA "family business" owners`
- `"[city]" business banker acquisition expansion`
- `"[city]" estate attorney succession business owner`
- `"[city]" M&A advisor "lower middle market"`

Set date filters when possible. If no date filter is available, verify dates before including the trigger.

---

## Step 4: Classify Triggers

Classify each trigger by what it may mean for a CEO.

| Trigger | Chair Interpretation | Likely Move |
|---------|----------------------|-------------|
| Acquisition / merger | Integration, role change, identity, complexity | Signal scan, then warm intro |
| PE / investor backing | Growth pressure, reporting, board scrutiny | Check decision authority and access path |
| New CEO / president / successor | First-90-day isolation, role definition | Congratulatory value touch or referral ask |
| COO/CFO/VP hire | Professionalization and delegation | Monitor for fit and timing |
| New location / facility | Scaling systems, people, capital, operations | Ask source who knows the owner |
| Hiring spike | Management layers and process strain | Run signal scan if company fits room |
| Award / fastest-growing list | Public credibility and growth posture | Warm congratulations; ask who knows them |
| Founder profile / podcast | Learning orientation and public voice | Use for tone and future outreach |
| Succession / ESOP / family transition | Governance, legacy, next-gen leadership | Handle carefully; strong Vistage fit |
| Lawsuit / layoff / distress | Stress and risk, but sensitive | Internal context only unless source raises it |
| Event speaker / panelist | Public leadership and topic interest | Invite to a peer discussion or roundtable |

Do not over-infer. A trigger is a hypothesis, not proof of pain.

### Trigger Sensitivity Playbook

Decide whether the trigger can be named directly.

| Sensitivity | Trigger Types | Outreach Rule |
|-------------|---------------|---------------|
| Safe to mention | Award, public event, podcast, article, new location, community recognition | Congratulate or reference briefly |
| Mention carefully | Acquisition, PE backing, leadership change, succession, major hiring | Use as context; avoid assuming pain |
| Do not mention cold | Lawsuit, layoffs, distress, family conflict, negative reviews, bankruptcy | Internal context only unless a trusted source raises it |

If a trigger could embarrass the prospect, do not use it as the opener.

---

## Step 5: Score The Trigger

Use a simple 1-5 score. Precision theater wastes Chair time.

| Dimension | Question |
|-----------|----------|
| Fit | Does the company/person match the seat thesis? |
| Trigger strength | Does this event likely create real leadership complexity? |
| Freshness | Is the trigger current enough to matter? |
| Access | Is there a member, advisor, event, community, or public path? |
| Room value | Would this leader add useful perspective to the group? |
| Sensitivity | Would mentioning the trigger feel intrusive, opportunistic, or unsafe? |

Action tiers:

- **Act this week:** strong fit, fresh trigger, warm or plausible access.
- **Ask for referral:** strong trigger but relationship path matters.
- **Run signal scan:** good trigger, but facts need confirmation.
- **Nurture:** good fit, weak timing or access.
- **Ignore:** stale, generic, weak fit, direct conflict, or too sensitive.

### Access-Weighted Trigger Priority

Warm access can outrank dramatic news. A medium trigger with a trusted member intro may deserve action before a perfect trigger with no path.

| Access Level | Meaning | Recruiting Move |
|--------------|---------|-----------------|
| Warm | Member, alumni, trusted advisor, or community tie can intro | Ask for referral now |
| Lukewarm | Shared event, association, board, or weak mutual tie | Build familiarity or invite to roundtable |
| Cold but specific | Strong fit and real trigger, no relationship path | Signal scan before direct value touch |
| Cold and generic | Weak access and weak trigger | Nurture or skip |

Every A trigger needs either a warm path, a credible event bridge, or a strong reason to run a signal scan.

### Timing And Decay Rules

Add an expiration date to every action trigger.

| Trigger | Fresh Action Window | After Expiration |
|---------|---------------------|------------------|
| Leadership appointment | 1-2 weeks | Use as role context, not opener |
| Award / public recognition | 1-3 weeks | Move to credibility context |
| Event appearance / podcast | 1-4 weeks | Use for tone and interests |
| Expansion / facility / new market | 30-60 days | Use as durable growth context |
| Hiring spike | 30-60 days | Recheck whether roles remain open |
| Acquisition / PE backing | 30-90 days for outreach, durable as context | Verify current ownership and decision authority |
| Founder/family/ESOP/succession structure | Durable | Never frame as "recent" unless dated recently |

Expired triggers can still matter, but they should not drive urgent outreach language.

### Compound Signal Logic

One signal may be noise. Several related signals can reveal a real timing window.

Examples:

- New CFO + hiring spike + expansion = professionalization and scaling strain.
- Founder interview + succession language + family-business award = legacy and next-generation questions.
- PE backing + COO hire + new market launch = board pressure and operating cadence.
- Award + event speaking + association board role = public learning orientation and community visibility.

If three weak signals point in the same direction, upgrade the action tier one level. If signals point in different directions, keep them as context.

---

## Step 6: Guard Against False Signals

Before recommending action:

- Verify the publication date.
- Confirm the company identity and geography.
- Distinguish parent company, franchisee, subsidiary, and local operator.
- Check whether the article is syndicated, recycled, or old.
- Separate facts from inference.
- Watch for direct competitor conflicts.
- Treat sensitive negative news as internal context.
- Avoid generic industry trends unless tied to a named company or segment.

Staleness rule:

If a source page has no visible date, do not include it as fresh. Either find a dated source, mark it durable context, or discard it.

---

## Step 7: Decide The Next Best Move

Every trigger should produce one next action or be discarded.

### Trigger-To-Referral Overlay

Before recommending direct outreach, ask:

"Who could credibly open this door?"

Check:

- Current member, alumni, past guest, or stalled prospect
- Banker, CPA, attorney, broker, wealth advisor, or fractional CFO
- Chamber, association, nonprofit, or event connector
- Supplier, customer, vendor, or board relationship
- Speaker host, award organizer, journalist, or community leader

If there is a plausible source, use `vistage-referral-activation-engine` before cold outreach. The trigger makes the referral ask specific:

"Do you know [Name] at [Company]? I saw they are navigating [public trigger]. I am not looking to pitch them; I am trying to understand whether a confidential CEO room would be useful."

Possible moves:

- Run `vistage-prospect-signals` on the named company.
- Ask a member/advisor/source for a warm introduction using `vistage-referral-activation-engine`.
- Add the company to the market map.
- Add the leader to the nurture list.
- Invite the leader to a guest-safe roundtable.
- Draft a value-first outreach sequence with `vistage-outreach-campaign`.
- Pass because of fit, conflict, staleness, or sensitivity.

Trigger-to-action examples:

- **Award:** "Congratulations" plus ask a mutual source whether they know the leader.
- **Expansion:** ask an advisor/source whether the CEO is scaling the leadership team.
- **New CEO:** offer a peer pattern from first-90-day transitions; avoid pitching.
- **Acquisition:** ask for intro only if there is a warm path; do not sound like you are exploiting integration stress.
- **Distress:** do not mention the event cold. Use only to inform sensitivity and timing.

### Roundtable / Event Bridge

When several good-fit companies in one segment have triggers but no warm path, create proximity before outreach.

Suggest one small, guest-safe event:

- Topic tied to the trigger cluster
- Target attendee profile
- Why the topic matters now
- Which members/advisors can invite guests
- Three discussion questions
- Follow-up path after the event

Example: three facility expansions in manufacturing can become "Scaling Operations Without Breaking The Leadership Team."

---

## Step 8: Produce The Weekly Trigger Digest

Output should be short enough for a Chair to use on Monday morning.

Include:

1. **Monitor scope:** companies, segments, geography, and date window.
2. **Top triggers:** 3-10 items, ranked by actionability.
3. **Trigger table:** company/person, event, date, source, fit, access, sensitivity, action tier.
4. **Chair interpretation:** one sentence on why the trigger may matter.
5. **Recommended next action:** one concrete action with owner and due date.
6. **Referral path:** who to ask, if any.
7. **Research needed:** whether to run `vistage-prospect-signals` or `vistage-prospect-intel`.
8. **Discarded items:** optional list of stale, weak, or sensitive items not worth action.

Use this table:

| Priority | Company / Leader | Trigger | Date | Why It Matters | Best Path | Next Action |
|----------|------------------|---------|------|----------------|-----------|-------------|

Do not output a long research essay unless asked.

---

## Step 9: Maintain The Monitor

### Weekly Cadence

- Scan priority sources.
- Add new triggers.
- Score fit, trigger strength, access, and sensitivity.
- Choose the top 3 actions.
- Close out stale or low-fit items.

### Monthly Cadence

- Review which trigger types produced real conversations.
- Add/remove companies from the watchlist.
- Refresh search queries.
- Compare trigger activity to open seats.
- Update referral source map based on observed companies.
- Ask 3-5 members/advisors what they are seeing that is not yet public.

### Quarterly Cadence

- Revisit the seat thesis and priority segments.
- Review conversion by trigger type.
- Stop monitoring noisy sources.
- Add new public sources from member/advisor intelligence.

Quality metric:

The monitor is working if it creates better-timed conversations, not if it finds more news.

### Source Intelligence Loop

Public data misses quiet operators. Add a human intelligence pass.

Ask members/advisors:

- "Which owners in this segment are expanding quietly?"
- "Who is under new complexity that has not hit the news?"
- "Which clients are hiring leadership layers or preparing succession?"
- "Who recently became harder to reach because the business got more demanding?"
- "Which companies are respected locally but under-covered publicly?"

Treat these as source notes, not verified facts. Use them to choose who to research, who to ask for a referral, or which public sources to check next.

### CRM / Trigger Tracker Fields

Use these columns when the Chair wants a tracker: company, leader, segment, trigger type, source, source URL or note, publication date, expiration date, fit score, trigger strength, access score, sensitivity, compound signal notes, best referral path, action tier, next action, owner, due date, outcome, and date closed.

### Time-Budgeted Workflows

- **20-minute weekly scan:** review alerts, pick top 3 triggers, assign one next action each.
- **60-minute weekly digest:** scan priority sources, score triggers, identify referral paths, update tracker.
- **Monthly deep refresh:** prune sources, re-score watchlist, compare trigger quality to open seats.
- **Quarterly reset:** revisit trigger thesis, source density, conversion by trigger type, and segment focus.

### First 30/60/90 Days

- **Days 1-30:** define trigger thesis, build watchlist, set 3-5 core sources, run first digests.
- **Days 31-60:** test actions, compare warm-path vs cold-path results, tune decay and sensitivity rules.
- **Days 61-90:** prune noisy sources, double down on sources producing conversations, refresh the market map.

---

## Output Schema

When structured output is requested, return valid JSON with `monitor_scope`, `trigger_digest`, `next_week_actions`, and `discarded_or_deferred`.

Each trigger item should include: `priority`, `company`, `leader`, `trigger_type`, `date`, `expiration_date`, `fact`, `chair_interpretation`, `fit_score`, `trigger_strength`, `access_score`, `sensitivity`, `compound_signal_notes`, `recommended_next_action`, `best_path`, and `source_note`.

---

## Anti-Patterns

- Treating every news item as a reason to pitch.
- Mentioning sensitive negative news in cold outreach.
- Monitoring too broad a market to act on.
- Confusing generic industry trends with company-specific triggers.
- Skipping date verification.
- Ignoring room fit because the trigger looks exciting.
- Letting public triggers replace referrals.
- Automating LinkedIn or implying the Chair should.
- Producing a news digest with no next actions.

---

## Quality Bar

A good trigger monitor lets the Chair say:

- "These are the companies worth paying attention to this week."
- "This public event may create a real leadership moment."
- "This is the safest path into the conversation."
- "This is too sensitive to mention directly."
- "This item is stale or low fit, so I will ignore it."
- "These are the three actions I will take this week."

If the monitor does not change this week's recruiting behavior, it is noise.
