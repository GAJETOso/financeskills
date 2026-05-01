#!/bin/bash

# Simple validation script for FinanceSkills
echo "🔍 Validating Finance Skills..."

error_count=0

# Check if skills directory exists
if [ ! -d "skills" ]; then
  echo "❌ Error: 'skills' directory not found."
  exit 1
fi

# Iterate through skills
for skill_dir in skills/*/; do
  if [ -d "$skill_dir" ]; then
    skill_name=$(basename "$skill_dir")
    echo "Checking skill: $skill_name"
    
    # Check for SKILL.md
    if [ ! -f "${skill_dir}SKILL.md" ]; then
      echo "  ❌ Missing SKILL.md"
      ((error_count++))
    fi
  fi
done

if [ $error_count -eq 0 ]; then
  echo "✅ All skills validated successfully!"
  exit 0
else
  echo "❌ Validation failed with $error_count errors."
  exit 1
fi
