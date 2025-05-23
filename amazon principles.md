### 🔹 Amazon Leadership Principles – One-Line Summaries

1. **Customer Obsession** – Focus relentlessly on delivering value to customers, even beyond what they ask for.
2. **Ownership** – Act like an owner: take responsibility for outcomes, not just tasks.
3. **Invent and Simplify** – Look for ways to innovate and reduce complexity.
4. **Dive Deep** – Stay curious and go into the details when needed — don’t just skim the surface.
5. **Are Right, A Lot** – Use good judgment and strong instincts to make consistently sound decisions.
6. **Insist on the Highest Standards** – Never compromise on quality; raise the bar for yourself and others.
7. **Think Big** – Take bold ideas seriously and imagine impactful, scalable solutions.
8. **Bias for Action** – Favor speed and calculated risk over waiting for perfect certainty.
9. **Frugality** – Accomplish more with less — resource constraints can breed creativity.
10. **Earn Trust** – Build trust through honesty, empathy, and delivering results.
11. **Deliver Results** – Focus on what truly matters and consistently get it done.
12. **Have Backbone; Disagree and Commit** – Respectfully challenge decisions when you disagree, then fully commit once a path is chosen.


---

## 1. **Customer Obsession**

**Story 1: Full app migration with customer input**

* **Situation:** You were leading the migration of a full legacy app for a client.
* **Task:** Ensure the new system met client needs and performed better than the old one.
* **Action:** You proactively set up meetings with the client to understand their frustrations with the old app and asked questions beyond the requirements to uncover pain points.
* **Result:** You implemented changes that weren’t originally requested but significantly improved usability and performance, and the client gave positive feedback.

**Story 2: Fixing edge-case bugs**

* **Situation:** While migrating pages from the legacy Java app, you noticed certain edge cases that caused minor issues.
* **Task:** These weren’t in the backlog but could impact the user experience.
* **Action:** You documented them, fixed the ones you could, and flagged the others to the team even though it wasn’t strictly your responsibility.
* **Result:** Clients experienced fewer bugs and support tickets dropped.



## 2. **Ownership**

**Story 1: Taking ownership of full app migration**

* **Situation:** Initially, you were only responsible for migrating individual Java pages.
* **Task:** Over time, you became the lead for the entire migration project.
* **Action:** You took responsibility not only for development but also for coordinating with stakeholders, performance testing, and planning deployment strategy.
* **Result:** The project advanced faster, and other teams began relying on your documentation and decisions.

**Story 2: Handling production issue after hours**

* **Situation:** A small part of the app you migrated caused a production issue.
* **Task:** Fix it quickly, though you weren’t on call.
* **Action:** You stayed late, investigated the root cause, and deployed a hotfix. Then, you added better logging and wrote a post-mortem to prevent future issues.
* **Result:** The client barely noticed the downtime, and you gained your manager's trust for taking initiative.



## 3. **Invent and Simplify**

**Story 1: Simplifying data flow**

* **Situation:** During migration, you noticed that the original app used a very complex data flow between services.
* **Task:** Simplify the architecture without breaking functionality.
* **Action:** You proposed and implemented a cleaner, more modular setup using Node.js microservices.
* **Result:** This reduced bugs, made testing easier, and new developers could onboard faster.

**Story 2: Streamlining deployments**

* **Situation:** Deployment involved too many manual steps and was error-prone.
* **Task:** Improve the pipeline.
* **Action:** You introduced scripts or a CI/CD tool to automate repetitive tasks and made documentation for the team.
* **Result:** Deployment became more reliable and 2x faster.



## 4. **Dive Deep**

**Story 1: Debugging a performance bottleneck**

* **Situation:** The migrated app was noticeably slower than expected in staging.
* **Task:** Identify and resolve the performance issue.
* **Action:** You profiled SQL queries, analyzed backend logs, and found a poorly indexed query causing latency.
* **Result:** After fixing it, response times improved by 60%, and you shared your findings with the team so others could avoid similar mistakes.

**Story 2: Investigating inconsistent bug reports**

* **Situation:** QA reported intermittent failures in a module you didn’t directly work on.
* **Task:** Help identify the root cause, even though it wasn’t your responsibility.
* **Action:** You dug into logs, test cases, and backend calls, and eventually traced the issue to a rare race condition during login.
* **Result:** Fixing it increased app reliability and you were recognized for your attention to detail.



## 5. **Are Right, A Lot**

**Story 1: Choosing the right tech stack**

* **Situation:** While leading the full app migration, you had to decide between different hosting setups and backend tech.
* **Task:** Make a decision that balanced performance, cost, and maintainability.
* **Action:** You researched options, considered the team’s strengths, and proposed a Node.js-based setup with a managed SQL service, documenting trade-offs.
* **Result:** Your decision led to faster dev cycles, and the client was happy with both performance and cost.

**Story 2: Predicting client needs**

* **Situation:** The client didn’t initially ask for analytics or monitoring.
* **Task:** Decide whether to add them.
* **Action:** You suggested basic metrics logging and uptime alerts based on experience with past issues.
* **Result:** When an issue came up later, you identified it immediately thanks to logs — earning trust from the client.



## 6. **Insist on the Highest Standards**

**Story 1: Code quality in migration**

* **Situation:** You were reviewing code from junior developers during the app migration.
* **Task:** Ensure quality without delaying delivery.
* **Action:** You gave constructive feedback, enforced tests, and created reusable templates/components to reduce bugs.
* **Result:** Fewer regressions, and the team velocity actually improved because of better practices.

**Story 2: Testing neglected modules**

* **Situation:** Some legacy modules had little to no automated tests.
* **Task:** Improve test coverage without stalling delivery.
* **Action:** You wrote unit tests for critical logic and added regression tests for edge cases that had broken before.
* **Result:** Stability improved, and QA started spending less time on manual testing.



## 7. **Think Big**

**Story 1: Proposing app-wide changes**

* **Situation:** While leading the migration, you saw a chance to improve UX globally (e.g. consistency, responsiveness).
* **Task:** Go beyond the scope of just “porting” the app.
* **Action:** You pitched a unified design system and performance improvements (lazy loading, caching) to stakeholders.
* **Result:** The improvements were approved, resulting in a faster, more modern app.

**Story 2: Mentoring and process**

* **Situation:** New devs joining the migration struggled with setup and standards.
* **Task:** Improve onboarding and overall efficiency.
* **Action:** You documented everything (architecture, setup, patterns) and created a shared FAQ.
* **Result:** New team members became productive faster, and the docs are still in use.



## 8. **Bias for Action**

**Story 1: Quick decision under pressure**

* **Situation:** A deployment deadline was tight, and a module wasn’t fully ready.
* **Task:** Decide whether to delay or push a partial version.
* **Action:** You made a call to temporarily disable the non-critical part behind a feature flag and shipped the rest, notifying the client in advance.
* **Result:** You hit the deadline without compromising quality, and the client appreciated the transparency.

**Story 2: Hotfix outside normal workflow**

* **Situation:** A bug in production affected a key feature, and the official process for fixes was slow.
* **Task:** Resolve the issue quickly without breaking the rules.
* **Action:** You proposed and implemented a lightweight emergency path for verified hotfixes and documented it.
* **Result:** Bug was fixed in hours instead of days, and the team adopted the new hotfix flow for future cases.



## 9. **Frugality**

**Story 1: Cost-conscious hosting**

* **Situation:** You were comparing hosting options for the new app.
* **Task:** Pick a performant but cost-efficient solution.
* **Action:** You benchmarked managed platforms, chose one with auto-scaling and only-on-demand pricing, and avoided over-provisioning.
* **Result:** Infrastructure cost was 40% lower than initially estimated.

**Story 2: Reusing existing components**

* **Situation:** Designers asked for new components during migration.
* **Task:** Avoid rebuilding from scratch if not needed.
* **Action:** You suggested reusing and slightly modifying existing shared components in React instead of writing new ones.
* **Result:** Saved dev time and reduced maintenance overhead.



## 10. **Earn Trust**

**Story 1: Client trust through transparency**

* **Situation:** A planned feature couldn’t be delivered as initially scoped.
* **Task:** Communicate the issue clearly to the client.
* **Action:** You explained the blockers, proposed alternatives, and gave realistic new timelines without hiding anything.
* **Result:** The client appreciated your honesty and gave you more freedom in future planning.

**Story 2: Helping teammates grow**

* **Situation:** A junior teammate struggled with understanding a legacy system.
* **Task:** Support them without taking over their work.
* **Action:** You scheduled pair-programming sessions, explained the logic patiently, and encouraged them to take ownership.
* **Result:** They gained confidence, finished their task, and later thanked you for helping them grow.



## 11. **Deliver Results**

**Story 1: On-time migration delivery**

* **Situation:** You were leading a large migration project with a fixed deadline.
* **Task:** Deliver the app with all key features on time.
* **Action:** You broke the work into manageable milestones, tracked blockers daily, and kept communication clear with all stakeholders.
* **Result:** You delivered before the deadline and the client was satisfied with both the performance and design.

**Story 2: Exceeding KPIs**

* **Situation:** You were asked to improve load times by 20%.
* **Task:** Optimize the app without breaking anything.
* **Action:** You implemented smart caching, code-splitting in React, and lazy loading for assets.
* **Result:** The app ended up 45% faster, exceeding expectations.



## 12. **Have Backbone; Disagree and Commit**

**Story 1: Challenging a risky proposal**

* **Situation:** A colleague proposed a shortcut for backend logic that you knew would cause long-term issues.
* **Task:** Speak up without being disrespectful.
* **Action:** You explained your concerns, presented data, and suggested a more stable alternative. There was some pushback, but you stuck to your reasoning.
* **Result:** The team agreed with you, and it saved rework later when the risks became clear.

**Story 2: Accepting team decision after disagreement**

* **Situation:** You disagreed with the choice of a 3rd-party tool for logging.
* **Task:** Commit after the team voted to go with it.
* **Action:** Despite your concerns, you fully committed, learned the tool inside out, and even helped others onboard.
* **Result:** The tool worked fine, and your attitude showed maturity and team-first thinking.
