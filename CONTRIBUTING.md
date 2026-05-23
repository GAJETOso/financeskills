# Contributing to FinanceSkills

Thank you for your interest in contributing! This guide will help you add new skills, improve existing ones, and contribute to the broader FinanceSkills ecosystem.

## Ways to Contribute

### 1. Report Issues
Found a bug or error in a skill? [Open an issue](https://github.com/GAJETOso/financeskills/issues/new) with:
- Which skill has the problem
- What you expected vs. what happened
- Steps to reproduce
- Your environment (AI agent, OS, etc.)

### 2. Improve Documentation
- Fix typos or unclear instructions
- Add examples or use cases
- Improve skill descriptions
- Translate documentation

### 3. Add New Skills
- Industry-specific skills (healthcare, real estate, etc.)
- Compliance frameworks (SOX, GDPR, local regulations)
- Advanced analytics techniques
- Integration skills (QuickBooks, Xero, SAP)

### 4. Enhance Existing Skills
- Add more examples
- Improve prompts
- Add evaluation cases
- Update for new accounting standards

### 5. Share Skill Performance
- Report which skills work well for your use cases
- Share skill combinations that were effective
- Contribute evaluation results

## Skill Contribution Guidelines

### Skill Structure

Every skill must follow this directory structure:

```
skills/
└── your-skill-name/
    ├── SKILL.md              # Main skill file (REQUIRED)
    ├── evals/                # Test cases (OPTIONAL)
    │   └── evals.json
    └── references/           # Supporting documentation (OPTIONAL)
        ├── standards.md
        └── examples.md
```

### SKILL.md Template

Use this template for new skills:

```markdown
# [Skill Name]

[2-3 sentence description of what this skill does and when to use it]

## When to Use This Skill

Use this skill when:
- [Specific trigger 1]
- [Specific trigger 2]
- [Specific trigger 3]

## What This Skill Does

This skill helps you:
1. [Primary capability 1]
2. [Primary capability 2]
3. [Primary capability 3]

## Dependencies

This skill works best with:
- [Related skill 1](../related-skill-1) - [Why it's needed]
- [Related skill 2](../related-skill-2) - [Why it's needed]

## Accounting Standards

This skill implements:
- **IFRS**: [Relevant standards]
- **US GAAP**: [Relevant standards]
- **Other**: [Industry-specific standards]

## Workflow

### Step 1: [First Step Name]
[Detailed instructions for step 1]

**Example**:
```
[Code or example here]
```

### Step 2: [Second Step Name]
[Detailed instructions for step 2]

**Example**:
```
[Code or example here]
```

### Step 3: [Third Step Name]
[Detailed instructions for step 3]

## Common Use Cases

### Use Case 1: [Name]
**Scenario**: [Describe the scenario]

**Approach**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Expected Output**: [What the result should look like]

### Use Case 2: [Name]
**Scenario**: [Describe the scenario]

**Approach**:
1. [Step 1]
2. [Step 2]

**Expected Output**: [What the result should look like]

## Key Considerations

### Compliance Requirements
- [Important compliance point 1]
- [Important compliance point 2]

### Common Pitfalls
- **Pitfall 1**: [Description and how to avoid]
- **Pitfall 2**: [Description and how to avoid]

### Best Practices
- [Best practice 1]
- [Best practice 2]
- [Best practice 3]

## Examples

### Example 1: [Scenario Name]
**Input**:
```
[Sample input data or request]
```

**Process**:
[Explanation of what the skill does]

**Output**:
```
[Sample output]
```

### Example 2: [Scenario Name]
[Another detailed example]

## Tools & Resources

### Python Libraries
- [Library name]: [What it's used for]
- [Library name]: [What it's used for]

### External APIs
- [API name]: [What it provides]
- [API name]: [What it provides]

### Reference Documents
- [Document 1]: [Where to find it]
- [Document 2]: [Where to find it]

## Related Skills

Skills that complement this one:
- [skill-name-1](../skill-name-1) - [How it relates]
- [skill-name-2](../skill-name-2) - [How it relates]

## Regulatory References

### IFRS
- [Standard]: [Section reference]
- [Standard]: [Section reference]

### US GAAP
- [ASC Topic]: [Section reference]

### Other Standards
- [Standard]: [Description]

## Version History

- **v1.0** (YYYY-MM-DD): Initial release
- **v1.1** (YYYY-MM-DD): [What changed]

## Feedback

Have suggestions for improving this skill? [Open an issue](https://github.com/GAJETOso/financeskills/issues/new?title=[your-skill-name]%20Improvement)
```

### Skill Naming Conventions

**Good skill names**:
- Descriptive and specific
- Lowercase with hyphens
- 2-4 words maximum

**Examples**:
- ✅ `ecl-computation`
- ✅ `revenue-recognition`
- ✅ `oil-gas-valuation`
- ❌ `skill1`
- ❌ `RevenueRecognition`
- ❌ `calculate_expected_credit_loss_using_ifrs9`

### Description Quality Standards

Your skill description should be:
- **Clear**: Anyone reading should immediately understand what it does
- **Specific**: Not generic statements like "helps with finance"
- **Trigger-focused**: Include keywords that AI agents will recognize
- **Practical**: Focus on what users will actually do

**Bad description**:
> "This skill helps with accounting tasks"

**Good description**:
> "Calculate Expected Credit Loss (ECL) under IFRS 9 for loan portfolios using the three-stage impairment model, including PD, LGD, and EAD computation with forward-looking economic scenarios."

## Evaluation Guidelines

### Adding Test Cases

Create `evals/evals.json` for each skill:

```json
{
  "skill_name": "your-skill-name",
  "version": "1.0",
  "test_cases": [
    {
      "id": "test_001",
      "description": "Basic calculation test",
      "input": {
        "user_query": "Calculate current ratio for Q4 2024",
        "data": {
          "current_assets": 500000,
          "current_liabilities": 300000
        }
      },
      "expected_output": {
        "current_ratio": 1.67,
        "interpretation": "Healthy liquidity position"
      },
      "evaluation_criteria": [
        "Correct ratio calculation",
        "Proper interpretation",
        "Compliance with standards"
      ]
    },
    {
      "id": "test_002",
      "description": "Edge case: Zero liabilities",
      "input": {
        "user_query": "Calculate current ratio",
        "data": {
          "current_assets": 500000,
          "current_liabilities": 0
        }
      },
      "expected_output": {
        "error": "Cannot calculate ratio with zero liabilities",
        "suggestion": "Review balance sheet for completeness"
      },
      "evaluation_criteria": [
        "Proper error handling",
        "Helpful user guidance"
      ]
    }
  ]
}
```

### Test Coverage

Aim for test cases covering:
- ✅ Happy path (normal operation)
- ✅ Edge cases (extreme values, missing data)
- ✅ Error conditions (invalid inputs)
- ✅ Real-world scenarios
- ✅ Compliance validation

## Pull Request Process

### 1. Fork and Clone

```bash
# Fork the repository on GitHub first, then:
git clone https://github.com/YOUR_USERNAME/financeskills.git
cd financeskills
git remote add upstream https://github.com/GAJETOso/financeskills.git
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-skill-name
# or
git checkout -b fix/issue-description
```

### 3. Make Your Changes

Follow the skill structure and guidelines above.

### 4. Test Your Skill

```bash
# Validate skill format
./validate-skills.sh

# Run evals (if applicable)
cd skills/your-skill-name
# Test with your AI agent
```

### 5. Commit Your Changes

Use descriptive commit messages:

```bash
# Good commit messages
git commit -m "Add crypto-accounting skill with IFRS guidance"
git commit -m "Fix revenue-recognition IFRS 15 implementation"
git commit -m "Update oil-gas-valuation with Nigerian tax treatment"

# Bad commit messages
git commit -m "update stuff"
git commit -m "fix"
```

### 6. Push and Create PR

```bash
git push origin feature/your-skill-name
```

Then create a Pull Request on GitHub with:

**Title**: Clear, descriptive summary

**Description**: Should include:
- What the skill does
- Why it's needed
- Testing performed
- Screenshots (if UI changes)
- Checklist:
  ```
  - [ ] Skill follows template structure
  - [ ] Description is clear and specific
  - [ ] Examples are included
  - [ ] Test cases added (if applicable)
  - [ ] Documentation updated
  - [ ] Validated with AI agent
  ```

### 7. Respond to Feedback

- Be open to suggestions
- Respond promptly to review comments
- Make requested changes
- Re-request review when ready

## Skill Quality Checklist

Before submitting, verify:

### Structure
- [ ] Follows standard directory structure
- [ ] SKILL.md present and complete
- [ ] Uses proper markdown formatting
- [ ] All links work

### Content
- [ ] Clear, specific description
- [ ] When to use section is comprehensive
- [ ] Workflow steps are detailed
- [ ] At least 2 examples included
- [ ] Common pitfalls documented
- [ ] Best practices listed

### Technical
- [ ] Accounting standards referenced
- [ ] Dependencies listed
- [ ] Related skills linked
- [ ] Code examples work
- [ ] Test cases pass (if applicable)

### Compliance
- [ ] IFRS standards cited (if applicable)
- [ ] US GAAP standards cited (if applicable)
- [ ] Industry regulations noted (if applicable)
- [ ] Jurisdiction-specific guidance included (if applicable)

## Skill Categories

When adding a new skill, categorize it:

1. **Financial Analysis & Reporting** - Ratio analysis, statements, performance
2. **Audit & Compliance** - Audit procedures, controls, forensics
3. **Tax & Regulatory** - Tax planning, compliance, disclosures
4. **Risk & Treasury** - Risk management, cash, liquidity
5. **Corporate Finance** - M&A, valuation, capital structure
6. **Industry-Specific** - Sector-specialized skills
7. **Advanced Analytics** - ML, NLP, predictive models

## Examples of Good Contributions

### New Skill Example
**PR #42: Add real-estate-valuation skill**
- Comprehensive skill for property valuation
- Includes DCF, comparables, and cost approaches
- References IVS standards
- Has 5 detailed examples
- Includes 10 test cases

### Enhancement Example
**PR #38: Improve oil-gas-valuation with Nigerian tax**
- Added Nigerian Petroleum Industry Act guidance
- Updated for 2024 tax changes
- Added example calculations
- Cross-referenced tax-planning skill

### Bug Fix Example
**PR #35: Fix ecl-computation forward-looking scenarios**
- Corrected discount rate application
- Updated IFRS 9 references
- Added clarifying examples
- Improved error messages

## Code of Conduct

### Be Respectful
- Treat all contributors with respect
- Welcome newcomers
- Provide constructive feedback
- No harassment or discrimination

### Be Collaborative
- Share knowledge
- Help others learn
- Credit others' work
- Build on existing contributions

### Be Professional
- Use professional language
- Focus on facts, not opinions
- Admit mistakes gracefully
- Learn from feedback

## Getting Help

### Questions About Contributing
- 💬 [GitHub Discussions](https://github.com/GAJETOso/financeskills/discussions)
- 📧 [Open an Issue](https://github.com/GAJETOso/financeskills/issues/new?title=Question:%20)

### Technical Issues
- 🐛 [Report a Bug](https://github.com/GAJETOso/financeskills/issues/new?template=bug_report.md)
- 💡 [Request a Feature](https://github.com/GAJETOso/financeskills/issues/new?template=feature_request.md)

### Skill Development Support
- 📚 Review existing skills for examples
- 🔍 Check [SKILL_MATRIX.md](./SKILL_MATRIX.md) for dependencies
- 📖 Read [INSTALLATION.md](./INSTALLATION.md) for setup

## Recognition

Contributors will be recognized in:
- Contributors section of README
- Individual skill credits
- Release notes
- Community highlights

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](./LICENSE).

## Thank You!

Every contribution makes FinanceSkills better for the entire community of financial professionals using AI. Thank you for taking the time to contribute!

---

**Questions?** Reach out in [Discussions](https://github.com/GAJETOso/financeskills/discussions) or [open an issue](https://github.com/GAJETOso/financeskills/issues).
