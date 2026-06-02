#!/usr/bin/env node
"use strict";

const fs = require("fs");
const os = require("os");
const path = require("path");

const REQUIRED_SKILLS = [
  "product-forge",
  "pf-help",
  "pf-init",
  "pf-intake",
  "pf-discovery",
  "pf-research",
  "pf-roadmap",
  "pf-metrics",
  "pf-narrative",
  "pf-define",
  "pf-spec",
  "pf-prd",
  "pf-prototype",
  "pf-plan",
  "pf-project",
  "pf-review",
  "pf-accept",
  "pf-retro",
];

const PROTOTYPE_TEMPLATE_FILES = [
  "index.html",
  "styles.css",
  "app.js",
  "data/sample-data.json",
  "data/copy.zh-CN.json",
  "spec/product-spec.json",
];

const PROJECT_TEMPLATE_FILES = [
  "project-plan.md",
  "raid-log.md",
  "stakeholder-update.md",
  "decision-log.md",
  "launch-readiness.md",
  "acceptance-tracker.md",
];

const REQUIRED_REFERENCES = [
  "methodology.md",
  "method-library.md",
  "project-workspace.md",
  "prototype-demo.md",
  "review-checklist.md",
  "usage-guide.md",
  "domain-packages.md",
];

const REQUIRED_CONTENT = {
  "pf-discovery/SKILL.md": [
    "outcome",
    "opportunity",
    "solution",
    "assumption test",
    "evidence quality",
    "decision rule",
  ],
  "pf-metrics/SKILL.md": [
    "north star",
    "input metrics",
    "guardrails",
    "baseline",
    "target",
    "owner",
    "review cadence",
  ],
  "pf-narrative/SKILL.md": [
    "press release",
    "customer faq",
    "internal faq",
    "risks",
    "rejected alternatives",
    "open questions",
  ],
  "pf-project/SKILL.md": [
    "raid escalation rule",
    "stakeholder update cadence",
    "decision log",
    "launch readiness gate",
    "acceptance progress state",
  ],
  "product-forge/scripts/init_product_workspace.py": [
    "Assumption Test",
    "Evidence Quality",
    "Decision Rule",
    "Baseline",
    "Target",
    "Review Cadence",
  ],
  "product-forge/scripts/init_feature_pack.py": [
    "Assumption Test",
    "Evidence Quality",
    "Decision Rule",
    "Rejected Alternatives",
    "Baseline",
    "Target",
    "Review Cadence",
  ],
  "product-forge/scripts/init_project_pack.py": [
    "Escalation Rules",
    "Update Cadence",
    "Decision Requests",
    "Readiness Gate Summary",
    "Status Rules",
  ],
  "product-forge/assets/templates/project-pack/raid-log.md": [
    "Escalation Rules",
    "Severity",
    "Trigger",
    "Decision Needed",
  ],
  "product-forge/assets/templates/project-pack/stakeholder-update.md": [
    "Update Cadence",
    "Audience",
    "Decision Requests",
  ],
  "product-forge/assets/templates/project-pack/decision-log.md": [
    "Decision Type",
    "Status",
    "Evidence",
    "Revisit Condition",
  ],
  "product-forge/assets/templates/project-pack/launch-readiness.md": [
    "Readiness Gate Summary",
    "PASS/CONCERN/FAIL",
    "Required Evidence",
    "Actual Evidence",
  ],
  "product-forge/assets/templates/project-pack/acceptance-tracker.md": [
    "Status Rules",
    "Evidence Ready",
    "Business Rule / Permission / State Coverage",
  ],
  "product-forge/references/method-library.md": [
    "outcome",
    "assumption test",
    "baseline",
    "target",
    "rejected alternatives",
    "RAID escalation rules",
    "launch readiness gate",
  ],
};

function usage() {
  console.log(`ProductForge CLI

Usage:
  product-forge <command> [options]

Commands:
  install    Install ProductForge skills into Codex skills directory
  status     Show installed ProductForge skill status
  validate   Validate a local ProductForge skill source
  uninstall  Remove ProductForge skills from Codex skills directory
  list       List ProductForge commands

Options:
  --source <dir>  Skill source directory, default: skills
  --target <id>   Install target, currently only codex
  --home <dir>    Codex home, default: ~/.codex
`);
}

function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 0; i < argv.length; i += 1) {
    const item = argv[i];
    if (!item.startsWith("--")) {
      args._.push(item);
      continue;
    }
    const key = item.slice(2);
    const next = argv[i + 1];
    if (!next || next.startsWith("--")) {
      args[key] = true;
    } else {
      args[key] = next;
      i += 1;
    }
  }
  return args;
}

function expandHome(value) {
  if (!value) return value;
  if (value === "~") return os.homedir();
  if (value.startsWith("~/")) return path.join(os.homedir(), value.slice(2));
  return value;
}

function resolveSource(args) {
  return path.resolve(process.cwd(), args.source || "skills");
}

function resolveCodexSkills(args) {
  const target = args.target || "codex";
  if (target !== "codex") {
    throw new Error(`Unsupported target: ${target}. ProductForge currently supports codex only.`);
  }
  const home = path.resolve(expandHome(args.home || path.join(os.homedir(), ".codex")));
  return path.join(home, "skills");
}

function readFrontmatterName(skillFile) {
  const text = fs.readFileSync(skillFile, "utf8");
  const match = text.match(/^name:\s*(.+)$/m);
  return match ? match[1].trim() : null;
}

function validateSource(source) {
  const missing = [];
  const problems = [];
  for (const skill of REQUIRED_SKILLS) {
    const skillFile = path.join(source, skill, "SKILL.md");
    if (!fs.existsSync(skillFile)) {
      missing.push(skillFile);
      continue;
    }
    const declared = readFrontmatterName(skillFile);
    if (declared !== skill) {
      problems.push(`${skillFile}: frontmatter name is ${JSON.stringify(declared)}, expected ${JSON.stringify(skill)}`);
    }
  }

  const templateRoot = path.join(source, "product-forge", "assets", "templates", "prototype-demo");
  for (const rel of PROTOTYPE_TEMPLATE_FILES) {
    const file = path.join(templateRoot, rel);
    if (!fs.existsSync(file)) missing.push(file);
  }

  const projectTemplateRoot = path.join(source, "product-forge", "assets", "templates", "project-pack");
  for (const rel of PROJECT_TEMPLATE_FILES) {
    const file = path.join(projectTemplateRoot, rel);
    if (!fs.existsSync(file)) missing.push(file);
  }

  const referenceRoot = path.join(source, "product-forge", "references");
  for (const rel of REQUIRED_REFERENCES) {
    const file = path.join(referenceRoot, rel);
    if (!fs.existsSync(file)) missing.push(file);
  }

  for (const [rel, tokens] of Object.entries(REQUIRED_CONTENT)) {
    const file = path.join(source, rel);
    if (!fs.existsSync(file)) {
      missing.push(file);
      continue;
    }
    const text = fs.readFileSync(file, "utf8").toLowerCase();
    for (const token of tokens) {
      if (!text.includes(token.toLowerCase())) {
        problems.push(`${file}: missing required method/template field ${JSON.stringify(token)}`);
      }
    }
  }

  return { missing, problems };
}

function shouldSkipCopy(src) {
  const base = path.basename(src);
  return base === "__pycache__" || base === ".DS_Store" || base.endsWith(".pyc");
}

function copyRecursive(src, dest) {
  if (shouldSkipCopy(src)) return;
  const stat = fs.statSync(src);
  if (stat.isDirectory()) {
    fs.mkdirSync(dest, { recursive: true });
    for (const entry of fs.readdirSync(src)) {
      copyRecursive(path.join(src, entry), path.join(dest, entry));
    }
    return;
  }
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.copyFileSync(src, dest);
}

function commandValidate(args) {
  const source = resolveSource(args);
  const { missing, problems } = validateSource(source);
  if (missing.length || problems.length) {
    console.log("Validation failed.");
    for (const item of missing) console.log(`Missing: ${item}`);
    for (const item of problems) console.log(`Problem: ${item}`);
    process.exitCode = 1;
    return;
  }
  console.log(`Validation passed: ProductForge skill pack is complete at ${source}.`);
}

function commandList() {
  for (const skill of REQUIRED_SKILLS) {
    if (skill === "product-forge") continue;
    console.log(`$${skill}`);
  }
}

function commandInstall(args) {
  const source = resolveSource(args);
  const skillsDir = resolveCodexSkills(args);
  const { missing, problems } = validateSource(source);
  if (missing.length || problems.length) {
    commandValidate(args);
    process.exitCode = 1;
    return;
  }
  fs.mkdirSync(skillsDir, { recursive: true });
  for (const skill of REQUIRED_SKILLS) {
    const src = path.join(source, skill);
    const dest = path.join(skillsDir, skill);
    fs.rmSync(dest, { recursive: true, force: true });
    copyRecursive(src, dest);
    console.log(`Installed ${skill} -> ${dest}`);
  }
}

function commandStatus(args) {
  const skillsDir = resolveCodexSkills(args);
  for (const skill of REQUIRED_SKILLS) {
    const skillFile = path.join(skillsDir, skill, "SKILL.md");
    console.log(`${fs.existsSync(skillFile) ? "installed" : "missing"} ${skill}`);
  }
}

function commandUninstall(args) {
  const skillsDir = resolveCodexSkills(args);
  for (const skill of REQUIRED_SKILLS) {
    const dest = path.join(skillsDir, skill);
    fs.rmSync(dest, { recursive: true, force: true });
    console.log(`Removed ${dest}`);
  }
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  const command = args._[0] || "help";
  try {
    if (command === "help" || args.help) usage();
    else if (command === "validate") commandValidate(args);
    else if (command === "list") commandList(args);
    else if (command === "install") commandInstall(args);
    else if (command === "status") commandStatus(args);
    else if (command === "uninstall") commandUninstall(args);
    else {
      usage();
      process.exitCode = 1;
    }
  } catch (error) {
    console.error(error.message);
    process.exitCode = 1;
  }
}

main();
