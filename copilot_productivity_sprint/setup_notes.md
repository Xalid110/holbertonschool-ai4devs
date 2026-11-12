## Step-by-Step Setup Process

### 1. Prerequisites
- Active **GitHub account** with GitHub Copilot enabled (Free, Pro, Business, or Enterprise).
- **Visual Studio Code** installed and accessible via CLI (\`code\`).

### 2. Extension Installation
1. Open Visual Studio Code and navigate to the **Extensions** view (\`Ctrl+Shift+X\` / \`Cmd+Shift+X\`).
2. Search for **GitHub Copilot** (published by \`GitHub\`) and click **Install** (this automatically bundles **GitHub Copilot Chat**).
3. Alternatively, install via terminal:
   \`\`\`bash
   code --install-extension GitHub.copilot
   code --install-extension GitHub.copilot-chat
   \`\`\`

### 3. Authentication & Account Linking
1. Click the **Accounts** icon in the bottom-left Activity Bar of VS Code.
2. Select **Sign in with GitHub** and authorize Visual Studio Code in the browser.
3. Confirm the Copilot status icon in the bottom-right Status Bar displays as active (\`GitHub Copilot: Ready\`).

### 4. Configuration (\`settings.json\`)
Configured VS Code user settings to enable inline suggestions across programming languages while disabling noise in plain text files:

\`\`\`json
{
  "github.copilot.enable": {
    "*": true,
    "plaintext": false,
    "markdown": true
  },
  "editor.inlineSuggest.enabled": true,
  "github.copilot.editor.enableAutoCompletions": true
}
\`\`\`

### 5. Verification
1. **Inline Autocomplete:** Opened a Python/JavaScript file, wrote a function comment, and verified inline ghost-text completion (\`Tab\` to accept).
2. **Copilot Chat:** Opened the Chat panel (\`Ctrl+Alt+I\` / \`Ctrl+Cmd+I\`), tested workspace context prompts, and confirmed response generation.
EOF
