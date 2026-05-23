# Installation Guide

Complete guide to installing and using FinanceSkills with AI coding agents.

## Quick Start

The fastest way to get started:

```bash
npx skills add GAJETOso/financeskills
```

This command installs all skills to `.agents/skills/` and creates the necessary symlinks for Claude Code compatibility.

## Installation Methods

### Method 1: CLI Install (Recommended for Most Users)

**Best for**: Quick setup, automatic updates, standard configurations

The [npx skills](https://github.com/vercel-labs/skills) CLI provides the easiest installation experience:

```bash
# Install all 30+ finance skills
npx skills add GAJETOso/financeskills

# Install only specific skills you need
npx skills add GAJETOso/financeskills --skill financial-analysis audit-checklist tax-planning

# See all available skills before installing
npx skills add GAJETOso/financeskills --list

# Update to latest version
npx skills update GAJETOso/financeskills
```

**What it does**:
- Downloads skills to `.agents/skills/` directory
- Creates `.claude/skills/` symlinks for Claude Code
- Validates skill structure
- Handles version updates
- Works with all Agent Skills spec-compatible agents

### Method 2: Claude Code Plugin System

**Best for**: Claude Code users who want native integration

Claude Code has a built-in plugin marketplace for one-command installation:

```bash
# Add the FinanceSkills marketplace
/plugin marketplace add GAJETOso/financeskills

# Install all finance skills
/plugin install finance-skills

# Or install specific skill categories
/plugin install finance-skills --category audit
/plugin install finance-skills --category compliance

# Update to latest version
/plugin update finance-skills
```

**Benefits**:
- Native Claude Code integration
- Automatic skill discovery
- Built-in update notifications
- Plugin-specific configuration options

### Method 3: Manual Clone and Copy

**Best for**: Custom configurations, offline work, development

For full control over the installation:

```bash
# Clone the repository
git clone https://github.com/GAJETOso/financeskills.git

# Copy all skills to your project
cp -r financeskills/skills/* .agents/skills/

# Or copy specific skills
cp -r financeskills/skills/financial-analysis .agents/skills/
cp -r financeskills/skills/audit-checklist .agents/skills/

# Create Claude Code symlinks (if needed)
ln -s .agents/skills .claude/skills
```

**Optional**: Copy additional resources
```bash
# Copy compliance documentation
cp -r financeskills/compliance .agents/compliance

# Copy foundation materials
cp -r financeskills/foundations .agents/foundations

# Copy tools and utilities
cp -r financeskills/tools .agents/tools
```

### Method 4: Git Submodule

**Best for**: Keeping in sync with updates, multi-project setups

Add FinanceSkills as a git submodule to track upstream changes:

```bash
# Add as submodule
git submodule add https://github.com/GAJETOso/financeskills.git .agents/financeskills

# Initialize and update
git submodule update --init --recursive

# Reference skills from the submodule
ln -s .agents/financeskills/skills .agents/skills
```

**Updating to latest**:
```bash
cd .agents/financeskills
git pull origin main
cd ../..
git add .agents/financeskills
git commit -m "Update financeskills to latest"
```

### Method 5: Fork and Customize

**Best for**: Organizations needing custom skills, compliance-specific modifications

Fork the repository to create your own customized version:

1. **Fork on GitHub**: Click "Fork" on https://github.com/GAJETOso/financeskills

2. **Clone your fork**:
```bash
git clone https://github.com/YOUR_USERNAME/financeskills.git
cd financeskills
```

3. **Customize skills**:
```bash
# Modify existing skills for your industry
vim skills/oil-gas-valuation/SKILL.md

# Add organization-specific compliance requirements
vim compliance/COMPANY_STANDARDS.md

# Create custom skills
mkdir skills/custom-industry-skill
vim skills/custom-industry-skill/SKILL.md
```

4. **Keep in sync with upstream**:
```bash
# Add original repo as upstream
git remote add upstream https://github.com/GAJETOso/financeskills.git

# Fetch updates
git fetch upstream
git merge upstream/main
```

### Method 6: SkillKit (Multi-Agent Support)

**Best for**: Using multiple AI agents (Claude, Cursor, Copilot), team environments

[SkillKit](https://github.com/rohitg00/skillkit) installs skills across all your AI coding agents:

```bash
# Install for all supported agents
npx skillkit install GAJETOso/financeskills

# Install for specific agents only
npx skillkit install GAJETOso/financeskills --agents claude,cursor

# Install specific skills
npx skillkit install GAJETOso/financeskills --skill financial-analysis audit-checklist

# List what gets installed where
npx skillkit install GAJETOso/financeskills --dry-run

# Update all agents
npx skillkit update GAJETOso/financeskills
```

**Supported agents**:
- Claude Code
- Cursor
- GitHub Copilot
- Windsurf
- Cody
- Continue

## Directory Structure After Installation

After installation, your project should have:

```
your-project/
├── .agents/
│   ├── skills/
│   │   ├── financial-analysis/
│   │   │   ├── SKILL.md
│   │   │   ├── evals/
│   │   │   └── references/
│   │   ├── audit-checklist/
│   │   ├── tax-planning/
│   │   └── [other skills]/
│   ├── compliance/          # Optional
│   ├── foundations/         # Optional
│   └── tools/              # Optional
└── .claude/
    └── skills/ -> ../.agents/skills  # Symlink for Claude Code
```

## Verification

Verify installation was successful:

```bash
# Check skills directory exists
ls .agents/skills/

# Verify specific skill
cat .agents/skills/financial-analysis/SKILL.md

# Test with your agent
# In Claude Code, Cursor, etc:
/skills list
```

## Configuration

### Customizing Skill Behavior

Each skill can be configured via environment variables or a config file:

**Option 1: Environment Variables**
```bash
# Set default accounting standard
export FINANCE_SKILL_STANDARD=IFRS

# Set currency
export FINANCE_SKILL_CURRENCY=USD

# Set date format
export FINANCE_SKILL_DATE_FORMAT=DD/MM/YYYY
```

**Option 2: Config File** (`.agents/finance-config.json`)
```json
{
  "standard": "IFRS",
  "currency": "USD",
  "dateFormat": "DD/MM/YYYY",
  "jurisdiction": "Nigeria",
  "skills": {
    "financial-analysis": {
      "defaultRatios": ["current", "quick", "debt-to-equity"]
    },
    "audit-checklist": {
      "framework": "ISA"
    }
  }
}
```

### Agent-Specific Configuration

**Claude Code** (`.claude/config.json`):
```json
{
  "skills": {
    "path": ".agents/skills",
    "autoload": true
  }
}
```

**Cursor** (`.cursorrules`):
```
# Load finance skills on startup
load_skills_from: .agents/skills
default_accounting_standard: IFRS
```

## Updating Skills

### Update All Skills

```bash
# Using npx skills
npx skills update GAJETOso/financeskills

# Using SkillKit
npx skillkit update GAJETOso/financeskills

# Using git submodule
cd .agents/financeskills && git pull origin main

# Using manual clone
cd financeskills && git pull origin main && cp -r skills/* ../.agents/skills/
```

### Update Specific Skills

```bash
# Download only updated skills
npx skills update GAJETOso/financeskills --skill financial-analysis audit-checklist
```

## Troubleshooting

### Skills Not Loading

**Problem**: Agent doesn't recognize skills

**Solutions**:
```bash
# Verify directory structure
ls -la .agents/skills/

# Check symlinks (Claude Code)
ls -la .claude/skills

# Rebuild symlink
rm .claude/skills
ln -s ../.agents/skills .claude/skills

# Restart your agent
```

### Permission Issues

**Problem**: Permission denied when installing

**Solutions**:
```bash
# Fix permissions
chmod -R 755 .agents/skills/

# Use sudo (if needed)
sudo npx skills add GAJETOso/financeskills
```

### Conflicts with Existing Skills

**Problem**: Skill names conflict

**Solutions**:
```bash
# Install to custom directory
npx skills add GAJETOso/financeskills --path .agents/finance-skills

# Rename conflicting skills
mv .agents/skills/financial-analysis .agents/skills/financial-analysis-custom
```

### Version Conflicts

**Problem**: Different skill versions across projects

**Solutions**:
```bash
# Lock to specific version (git submodule)
cd .agents/financeskills
git checkout v1.0.0

# Or use package.json for npm-based installs
# Add to package.json:
{
  "dependencies": {
    "@GAJETOso/financeskills": "1.0.0"
  }
}
```

## Uninstalling

### Remove All Skills

```bash
# Using npx skills
npx skills remove GAJETOso/financeskills

# Manual removal
rm -rf .agents/skills/
rm -rf .claude/skills

# Remove submodule
git submodule deinit .agents/financeskills
git rm .agents/financeskills
```

### Remove Specific Skills

```bash
# Remove individual skills
rm -rf .agents/skills/financial-analysis
rm -rf .agents/skills/audit-checklist
```

## Next Steps

After installation:

1. **Read the Learning Path**: Start with [foundations](../foundations/README.md)
2. **Try a Simple Skill**: Begin with `financial-analysis` or `budget-forecast`
3. **Review Compliance**: Check [compliance mapping](../compliance/REGULATORY_MAPPING.md)
4. **Explore Projects**: See example implementations in [projects](../projects/)
5. **Join Community**: Ask questions in [GitHub Discussions](https://github.com/GAJETOso/financeskills/discussions)

## Support

- 📚 [Full Documentation](../README.md)
- 🐛 [Report Issues](https://github.com/GAJETOso/financeskills/issues)
- 💬 [Ask Questions](https://github.com/GAJETOso/financeskills/discussions)
- 🤝 [Contributing Guide](../CONTRIBUTING.md)
