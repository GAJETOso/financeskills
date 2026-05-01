const fs = require('fs');
const path = require('path');

const SKILLS_DIR = path.join(__dirname, '../../skills');
const MARKETPLACE_FILE = path.join(__dirname, '../../marketplace.json');

function syncSkills() {
    const skills = [];
    const directories = fs.readdirSync(SKILLS_DIR).filter(f => fs.statSync(path.join(SKILLS_DIR, f)).isDirectory());

    directories.forEach(dir => {
        const skillPath = path.join(SKILLS_DIR, dir, 'SKILL.md');
        if (fs.existsSync(skillPath)) {
            const content = fs.readFileSync(skillPath, 'utf8');
            const nameMatch = content.match(/name:\s*(.*)/);
            const descMatch = content.match(/description:\s*(.*)/);
            
            if (nameMatch) {
                skills.push({
                    id: dir,
                    name: nameMatch[1].trim(),
                    path: `skills/${dir}`,
                    category: "General" // Manual adjustment might be needed
                });
            }
        }
    });

    const marketplace = JSON.parse(fs.readFileSync(MARKETPLACE_FILE, 'utf8'));
    marketplace.skills = skills;
    fs.writeFileSync(MARKETPLACE_FILE, JSON.stringify(marketplace, null, 2));
    console.log(`Synced ${skills.length} skills to marketplace.json`);
}

syncSkills();
