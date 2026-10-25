"""Single source of truth for the portfolio site and the resume/CV.

Every fact here must be recorded in the knowledge base (Desktop/profile-knowledge-base:
resume/Resume.md, resume/CV.md, credentials/Credentials.md, projects/Current_Projects.md).
Do not add claims or metrics that are not recorded there. Credentials.md lists what may be
printed: items marked "context only" (e.g. Team Member of the Month) stay off every output.

Shared data (contact, skills, experience, projects, education, publication, certifications,
languages) feeds both outputs. The SITE block holds copy that only the website uses.

Emphasis rules (2026-10-21): dates only for employment, education and the certification/paper (years,
no months), none on projects or features; the IEEE paper is a minor credential.

Confidentiality (2026-10-25): the Samsung project is classified. Never name it (no project name or
acronym) in any output or anywhere in this repo. Its public umbrella name is "Carrier Services
Platform"; the task force is its main part and the admin portal is part of it.
AI-assisted work at Samsung is an ongoing practice (analyzing manual workflows for problems and
improving them with AI), not a fixed list of tasks such as tickets or endpoint testing.

Writing rules (approved 2026-10-22; apply to resume, CV, site copy and any tailored version; check
every line against them before saving):
1. Current job is ongoing work: present tense, "regularly" for recurring work, never framed as a
   finished one-off. Past tense only for previous employers.
2. Numbers kept to a minimum: currently only "2+ years". No metrics such as the 50% ticket figure,
   no headcounts, team names or sizes, ticket/policy/store counts: "new hires", "across teams",
   "client and stakeholder requests".
3. Roles stated as held now, no backstory (no "inherited from", "departed", "mentor-guided"). The
   PM/PO role is "associate technical project manager / product owner".
4. No single feature dominates: PBAC is at most one plain mention of "access control", no acronym,
   no counts, not in skills.
5. Applies everywhere: resume, CV, site copy and any tailored version.
6. No words that inflate scope: no "entire", "almost all", "much of"; state what was built.
7. Current job in present tense with no "I" ("Leads", "Handles", "Owns"); bullets ordered so each
   leads into the next: build, then support and automation, then planning and PM. Previous jobs stay
   in past tense.
8. Bullets and descriptive sentences say "AI-assisted", never a specific AI tool (Cline, Claude), and
   carry no AWS service lists or step-by-step task details. The skills section may still list tools
   and services.

Inline markup: **text** renders bold on the site. Only SITE copy uses it; documents never see it.
"""
from __future__ import annotations

# --------------------------------------------------------------------------- identity & contact
NAME = "Lorenzo Miguel Ocampo"
TITLE = "Full Stack Software Engineer"
LOCATION = "Philippines (UTC+8)"
PHONE = "+63 929 209 6391"
EMAIL = "lorenzo.ocampo279@gmail.com"
LINKEDIN = ("linkedin.com/in/lmlocampo", "https://www.linkedin.com/in/lmlocampo/")
GITHUB = ("github.com/Chubber279", "https://github.com/Chubber279")
LINKS = [LINKEDIN, GITHUB]
WORK_AUTH = [
    "Authorized to work in the Philippines",
    "Available as contractor or via employer of record",
    "No visa sponsorship needed (remote)",
]

SUMMARY = (
    "Full stack software engineer with 2+ years building and supporting production systems in "
    "Java/Spring Boot, Vue.js and AWS, currently at Samsung R&D and previously on an airline ticketing "
    "platform. Builds features across the frontend and backend, handles client and stakeholder "
    "requests, and regularly improves manual workflows with AI-assisted automation. Also owns "
    "quarterly planning and new-hire onboarding, and works as an associate technical PM / product "
    "owner across teams. Strong written English; seeking a fully remote, product-focused role."
)

# --------------------------------------------------------------------------- skills
# Documents print "Label: a, b, c" exactly as written. The site uses the trimmed SITE["skills"] and
# shows each item as a tag with the first letter capitalized.
SKILLS = [
    ("Languages", ["Java", "JavaScript", "Python", "C#"]),
    ("Frameworks", ["Spring Boot", "Vue.js", "React.js", "Node.js", ".NET", "FastAPI"]),
    ("Data", ["MySQL", "DynamoDB", "Aurora RDS", "SQLite"]),
    ("Cloud (AWS)", ["EC2", "Lambda", "SQS", "KMS", "S3", "Athena"]),
    ("AI-assisted development", ["Claude", "Cline", "prompt design", "workflow automation", "code review"]),
    ("Practices & tools", ["REST APIs", "Agile/Scrum", "Git/GitHub", "Postman", "Figma", "Jira",
                           "Confluence"]),
    ("Delivery & leadership", ["Quarterly/feature planning", "cross-team coordination", "status reporting",
                               "mentoring", "documentation"]),
]

# --------------------------------------------------------------------------- experience
# resume: 1-page resume and the site timeline. cv: 2-page CV.
EXPERIENCE = [
    dict(
        company="Samsung R&D Philippines",
        role="Full Stack Software Engineer",
        dates="2025 – Present",
        location="Philippines",
        resume=[
            "Leads a project task force and builds admin-portal features such as carrier certificate "
            "management and access control, across a Vue.js frontend and a Spring Boot backend on AWS",
            "Handles client and stakeholder requests through production debugging and direct database "
            "fixes, and regularly analyzes manual workflows and improves them with AI-assisted automation",
            "Owns quarterly planning, feature scoping and new-hire onboarding; as associate technical "
            "PM / product owner, runs meetings, presents reports and coordinates work across teams",
        ],
        cv=[
            "Leads the main task force on a carrier services platform, building the frontend for its "
            "new pages in Vue.js and a per-device history log in Java/Spring Boot on AWS",
            "Builds and maintains carrier certificate management and access control for the admin portal",
            "Handles client and stakeholder requests through production debugging and direct database "
            "fixes",
            "Regularly analyzes manual team workflows for slow or repetitive steps and improves them "
            "with AI-assisted automation",
            "Owns quarterly planning, scoping new features and breaking them down into tasks",
            "Onboards and teaches new hires joining the team",
            "Works as associate technical PM / product owner on a live project: sets up meetings, "
            "prepares and presents reports, and coordinates work across teams",
            "Writes internal wiki documentation for meetings, reports and to-dos, closing recurring "
            "knowledge gaps in the team",
            "Uses Samsung's internal AI assistant (Gauss) for code review, documentation and SDLC task "
            "automation",
        ],
    ),
    dict(
        company="Aeronology Philippines Inc",
        role="Junior Software Engineer",
        dates="2023 – 2025",
        location="Philippines",
        resume=[
            "Built and extended booking and ticketing features on an airline ticketing platform used by "
            "travel agencies, working across a .NET/C# and SQL/MySQL backend, a React.js frontend, "
            "Python and AWS",
            "Owned the LIFT Airlines integration end to end, so travel agencies could book LIFT flights "
            "through the platform",
            "Investigated production incidents, mostly flight-detail mismatches from airline API data, "
            "and shipped fixes that handle incomplete data so the same errors stopped recurring",
            "Reviewed teammates' code, tested releases and improved backend code and documentation",
        ],
        cv=[
            "Built and extended booking and ticketing features on an airline ticketing platform used by "
            "travel agencies (.NET/C#, React.js, SQL/MySQL, Python, AWS)",
            "Owned the LIFT Airlines integration end to end, so travel agencies could book LIFT flights "
            "through the platform",
            "Investigated production incidents, mostly flight-detail mismatches caused by airline API "
            "data, and shipped hotfixes that handle incomplete data so the same errors stopped recurring",
            "Handled travel-agency client requests alongside feature work",
            "Reviewed teammates' code and tested releases before deployment",
            "Improved backend code and documentation, making the codebase easier to read and work on",
        ],
    ),
]

# --------------------------------------------------------------------------- side projects
# text: resume/CV bullet. The site case-study fields live in SITE["work"].
PROJECTS = [
    dict(
        name="Retail Sales & Inventory Site",
        tech=["Python", "FastAPI", "SQLite", "Vue.js"],
        text="Builds and maintains a local web app for a multi-brand fashion retailer that reshapes its "
        "data partner's daily ERP exports into the sales, inventory and sell-through views the "
        "merchandising manager needs, plus a weekly owners' report, reusing the existing Python ETL "
        "cleaning code so its numbers match the Excel reports; includes a staff scheduler with "
        "auto-fill assignments that replaced hand and Excel scheduling",
    ),
]

# --------------------------------------------------------------------------- education & research
EDUCATION = dict(
    school="University of the Philippines Los Baños",
    degree="BS Computer Science",
    dates="2019 – 2023",
    detail="Cum Laude · GWA 1.61 (1.0 = highest) · DOST-SEI MERIT Scholarship Grantee",
)

PUBLICATION = dict(
    title="A Novel Automatic Definition Selector and Scoring Scheme for the Identification of "
    "Filipino Metaphors",
    authors="Ocampo, L. M., & Clariño, M. A. A. D.",
    venue="2024 6th International Conference on Computer Communication and the Internet (ICCCI), IEEE",
    short_venue="ICCCI 2024",
    doi="10.1109/ICCCI62159.2024.10674510",
    doi_url="https://ieeexplore.ieee.org/document/10674510",
    resume_line="Primary author: methodology, implementation and manuscript. Presented orally.",
    cv_line="Primary author of thesis research on NLP-based automatic metaphor identification in "
    "Filipino text; independently designed the methodology, implemented the system and wrote the "
    "manuscript, with the adviser contributing editorial revisions.",
)

PRESENTATION = (
    "Oral presentation of the paper above, ICCCI 2024 (IEEE), to an international audience of "
    "academics and industry professionals."
)

CERTIFICATIONS = [("AWS Certified AI Practitioner", "Amazon Web Services", "2025")]

AWARDS = [
    "Cum Laude, BS Computer Science, University of the Philippines Los Baños (2023)",
    "DOST-SEI MERIT Scholarship Grantee",
]

LANGUAGES = [
    ("English", "Native / full professional proficiency"),
    ("Filipino", "Native"),
    ("Japanese", "Elementary, JLPT N5"),
]

# --------------------------------------------------------------------------- output names
RESUME_STEM = "Lorenzo_Ocampo_Resume_2026"
CV_STEM = "Lorenzo_Ocampo_CV_2026"

# --------------------------------------------------------------------------- website-only copy
SITE = dict(
    # Public address of the deployed site. Must stay absolute: link previews ignore relative URLs.
    url="https://chubber279.github.io/personal-portfolio/",
    description="Full stack software engineer (Java/Spring Boot, Vue.js, AWS) based in the Philippines, "
    "open to remote roles. Case studies and experience.",
    og_description="Production systems in Java/Spring Boot, Vue.js and AWS. AI-assisted automation. "
    "Open to remote roles.",
    status="Open to fully remote roles",
    lead="I build and run production systems in **Java/Spring Boot**, **Vue.js** and **AWS**, and I "
    "use AI tooling to remove slow, repetitive engineering work. Currently at Samsung R&D Philippines. "
    "Looking for a fully remote, product-focused role.",
    profile=[
        ("Location", LOCATION),
        ("Work setup", "Remote · contractor or employer of record"),
        ("Visa", "No sponsorship needed for remote work"),
        ("Languages", "English, Filipino"),
    ],
    core_stack=["Java", "Spring Boot", "Vue.js", "AWS", "Python"],
    about_heading="I turn vague requests into plans, and repetitive work into software",
    about=[
        "I'm a full stack engineer who likes the part before the code: taking a vague request, turning "
        "it into a plan the team can execute, and finding the manual, repetitive steps that software "
        "should be doing instead.",
        "I write things down. Decisions, workflows and the reasons behind them go into documentation the "
        "whole team can use, so knowledge outlasts any one person or sprint. That habit is part of why I "
        "now own quarterly planning, feature scoping and new-hire onboarding, and work as an associate "
        "technical project manager / product owner.",
        "Next, I want a role with more product ownership, or one centred on AI-assisted software "
        "development.",
    ],
    work_intro="Production systems, and the tools I build to remove manual, inefficient work around them.",
    # kind: "prod" | "side". metric is optional.
    work=[
        dict(
            kind="prod", where="Samsung R&D Philippines",
            title="Carrier Services Platform",
            metric="Task-force lead · frontend and backend",
            rows=[
                ("Platform", "A secure service that partner carriers use to support Samsung phone "
                 "customers."),
                ("Role", "Leads the platform's main task force, which adds new capabilities, and builds "
                 "and maintains admin-portal features."),
                ("Built", "The frontend for the task force's new pages (analytics dashboards, a manual "
                 "override tool for device requests and a per-device history log) and the history log's "
                 "backend. In the admin portal: carrier certificate management and access control."),
            ],
            stack=["Vue.js", "Java", "Spring Boot", "AWS"],
        ),
        dict(
            kind="prod", where="Samsung R&D Philippines",
            title="Internal AI tooling and automation",
            metric="Feature workflows · sprint tools · test automation",
            rows=[
                ("Problem", "Team workflows, from building new features to sprint ceremonies and testing, "
                 "relied on slow, repetitive manual steps."),
                ("Built", "Solutions I regularly design and ship: AI workflows for new-feature "
                 "development, sprint retro and planning websites tailored to how the team runs them, "
                 "test and test-document automation with its own UI, and other AI tools."),
                ("Impact", "All of them are in regular use by the team."),
            ],
            stack=["Python", "JavaScript", "HTML/CSS", "AI-assisted development"],
        ),
        dict(
            kind="side", project="Retail Sales & Inventory Site",
            metric="Dashboards · weekly owners' report · staff scheduler · Excel export",
            rows=[
                ("Problem", "The retailer's data partner sends daily ERP exports in a format that doesn't "
                 "match what the merchandising manager, the site's user, needs to see. My earlier "
                 "Streamlit and PostgreSQL version never ran reliably, and store schedules were still "
                 "made by hand or in Excel."),
                ("Built", "A local web app shaped around the merchandising manager's view rather than the "
                 "partner's format: it imports the exports, reshapes them into the sales, inventory and "
                 "sell-through views that manager works from, and produces the weekly owners' report. It reuses my "
                 "existing ETL cleaning code, so its numbers match the Excel reports."),
                ("Scheduler", "A better way to schedule than hand and Excel: day, week and roster views, "
                 "auto-fill that proposes assignments and day offs, and Excel export in the layout the "
                 "team already used. It started as a standalone app and now lives in the same site, so "
                 "the client runs one app. Built with AI-assisted development; I maintain it."),
            ],
        ),
    ],
    # Site skills: the shared rows minus soft skills and baseline tools (audit 2026-10-25). The
    # documents keep the full SKILLS list for ATS keyword matching.
    skills=[row for row in SKILLS if row[0] in ("Languages", "Frameworks", "Data", "Cloud (AWS)")]
    + [("Practices & tools", ["REST APIs", "Agile/Scrum", "Claude", "Cline"])],
    contact_heading="Let's talk about your team",
    contact="I'm looking for a fully remote, product-focused engineering role. The fastest way to reach "
    "me is email.",
)
