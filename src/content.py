"""Single source of truth for the portfolio site and the resume/CV.

Every fact here must be recorded in the knowledge base (Desktop/profile-knowledge-base:
resume/Resume.md, resume/CV.md, credentials/Credentials.md, projects/Current_Projects.md).
Do not add claims or metrics that are not recorded there. Credentials.md lists what may be
printed: items marked "context only" (e.g. Team Member of the Month) stay off every output.

Shared data (contact, skills, experience, projects, education, publication, certifications,
languages) feeds both outputs. The SITE block holds copy that only the website uses.

Emphasis rules (2026-10-21): dates only for employment, education and the certification/paper (years,
no months), none on projects or features; the IEEE paper is a minor credential; SSU is described as
a whole project, not by its features.

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
    "requests, and regularly uses AI-assisted automation to speed up support and testing. Also owns "
    "quarterly planning and new-hire onboarding, and works as an associate technical PM / product "
    "owner across teams. Strong written English; seeking a fully remote, product-focused role."
)

# --------------------------------------------------------------------------- skills
# Documents print "Label: a, b, c" exactly as written; the site shows each item as a tag with the
# first letter capitalized.
SKILLS = [
    ("Languages", ["Java", "JavaScript", "Python", "C#"]),
    ("Frameworks", ["Spring Boot", "Vue.js", "React.js", "Node.js", ".NET", "FastAPI"]),
    ("Data", ["MySQL", "DynamoDB", "Aurora RDS", "SQLite"]),
    ("Cloud (AWS)", ["Lambda", "SQS", "KMS", "S3", "Athena"]),
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
            "Leads the Samsung SIM Unlock (SSU) task force and builds admin-portal features such as "
            "carrier certificate management and access control, across a Vue.js frontend and a Spring "
            "Boot backend on AWS",
            "Handles client and stakeholder requests through production debugging and direct database "
            "fixes, and regularly builds AI-assisted scripts that speed up ticket resolution and endpoint "
            "testing",
            "Owns quarterly planning, feature scoping and new-hire onboarding; as associate technical "
            "PM / product owner, runs meetings, presents reports and coordinates work across teams",
        ],
        cv=[
            "Leads the Samsung SIM Unlock (SSU) task force, building its Vue.js frontend and Java/Spring "
            "Boot backend on AWS",
            "Builds and maintains carrier certificate management and access control for the admin portal",
            "Handles client and stakeholder requests through production debugging and direct database "
            "fixes",
            "Regularly builds AI-assisted scripts that speed up ticket resolution and endpoint testing",
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
            "Built and extended booking and ticketing features on an airline ticketing platform, working "
            "across a .NET/C# and SQL/MySQL backend, a React.js frontend, Python and AWS",
            "Integrated South African Airlines into the platform, extending access to international routes",
            "Supported production by investigating incidents and shipping hotfixes, reducing downtime and "
            "improving reliability",
            "Handled client and stakeholder requests, and kept quality up by reviewing teammates' code, "
            "testing releases and improving backend code and documentation",
        ],
        cv=[
            "Built and extended booking and ticketing features on an airline ticketing platform "
            "(.NET/C#, React.js, SQL/MySQL, Python, AWS)",
            "Integrated South African Airlines into the platform, extending access to international routes",
            "Investigated production incidents and shipped hotfixes and targeted fixes, reducing downtime "
            "and improving system reliability",
            "Handled client and stakeholder requests alongside feature work",
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
        tech=["Python", "FastAPI", "SQLite", "Vue.js", "Claude"],
        text="Builds and maintains a local web app for a multi-brand fashion retailer that turns daily "
        "ERP exports into sales, inventory and sell-through dashboards and a weekly owners' report, "
        "reusing the existing Python ETL cleaning code so its numbers match the Excel reports",
    ),
    dict(
        name="Staff Scheduling Application",
        tech=["Node.js", "SQLite", "REST API", "Claude"],
        text="Built a scheduling app with an auto-fill algorithm, REST API and browser frontend for "
        "store shifts and staff assignments",
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
        ("Languages", "English, Filipino, Japanese (N5)"),
    ],
    core_stack=["Java", "Spring Boot", "Vue.js", "AWS", "Python", "Claude"],
    about_heading="Engineer first, increasingly the person who plans the work",
    about=[
        "I'm a full stack engineer with production experience across enterprise platforms at Samsung "
        "and an airline ticketing platform. I'm comfortable across the stack: Spring Boot and .NET on "
        "the backend, Vue.js and React on the frontend, and AWS (Lambda, SQS, KMS, S3, Athena) underneath.",
        "Beyond building, I also own quarterly planning, feature scoping and breakdown, and onboarding "
        "of new hires on my team, and I work as an associate technical project manager / product "
        "owner coordinating across teams. That means I write for two audiences: engineers who need "
        "clear tasks, and stakeholders who need clear status.",
    ],
    work_intro="Three production projects and two self-directed builds. Employer work is described at "
    "the level I'm able to share publicly.",
    # kind: "prod" | "side". metric is optional.
    work=[
        dict(
            kind="prod", where="Samsung R&D Philippines",
            title="Samsung SIM Unlock (SSU) project",
            metric="Task-force lead · frontend and backend",
            rows=[
                ("Role", "Leads the task force for the project."),
                ("Built", "The Vue.js frontend and Java/Spring Boot backend, on AWS."),
            ],
            stack=["Vue.js", "Java", "Spring Boot", "AWS"],
        ),
        dict(
            kind="prod", where="Samsung R&D Philippines",
            title="AI-assisted support and testing automation",
            rows=[
                ("Problem", "Customer-ticket (VOC) investigations and endpoint testing involve repeated "
                 "manual steps."),
                ("Built", "Scripts that automate those steps, which I regularly build and extend with "
                 "AI-assisted development."),
            ],
            stack=["Scripting", "SQL", "AI-assisted development"],
        ),
        dict(
            kind="prod", where="Samsung R&D Philippines",
            title="Admin portal: carrier certificate management",
            rows=[
                ("Problem", "The admin portal needs carrier certificate management and control over who "
                 "can do what."),
                ("Built", "Carrier certificate management and access control features, which I build and "
                 "maintain."),
            ],
            stack=["Spring Boot", "Vue.js", "AWS"],
        ),
        dict(
            kind="side", project="Retail Sales & Inventory Site",
            metric="Dashboards · weekly owners' report · Excel export",
            rows=[
                ("Problem", "A multi-brand fashion retailer's daily ERP exports were only usable through "
                 "Excel reports, and an earlier Streamlit and PostgreSQL app never ran reliably."),
                ("Built", "A local web app that imports the exports, shows sales, inventory and "
                 "sell-through, and produces the weekly owners' report. It reuses the existing ETL "
                 "cleaning code, so its numbers match the Excel reports. Built with AI-assisted "
                 "development; I maintain it."),
            ],
        ),
        dict(
            kind="side", project="Staff Scheduling Application",
            metric="Auto-fill scheduling · REST API · browser UI",
            rows=[
                ("Problem", "Store shifts and sales-associate assignments were scheduled by hand."),
                ("Built", "A web app with an auto-fill scheduling algorithm, a REST API and a browser "
                 "frontend for managing shifts and assignments."),
            ],
        ),
    ],
    contact_heading="Let's talk about your team",
    contact="I'm looking for a fully remote, product-focused engineering role. Authorized to work in the "
    "Philippines, available as a contractor or through an employer of record, and no visa sponsorship "
    "needed. The fastest way to reach me is email.",
)
