AI Coding Assistant Setup Notes
Environment & Tool Versions

Component	Name / Identifier	Version
Operating System	Linux / Windows / macOS	Your OS version
IDE	Visual Studio Code	Your VS Code version
Primary Extension	GitHub Copilot (GitHub.copilot)	Your installed version
Chat Extension	GitHub Copilot Chat (GitHub.copilot-chat)	Your installed version
Git	Git CLI	Your Git version
Step-by-Step Setup Process
1. Prerequisites
Active GitHub account with GitHub Copilot enabled.
Visual Studio Code installed.
2. Extension Installation
Open Visual Studio Code.
Navigate to Extensions (Ctrl+Shift+X).
Search for GitHub Copilot.
Install GitHub Copilot and GitHub Copilot Chat.
3. Authentication & Account Linking
Open the Accounts menu in VS Code.
Select Sign in with GitHub.
Authorize Visual Studio Code.
Verify that GitHub Copilot is active.
4. Configuration (settings.json)

json
{
  "github.copilot.enable": {
    "*": true,
    "plaintext": false,
    "markdown": true
  },
  "editor.inlineSuggest.enabled": true,
  "github.copilot.editor.enableAutoCompletions": true
}
5. Verification
Tested inline autocomplete in a Python or JavaScript file.
Verified ghost-text suggestions.
Tested GitHub Copilot Chat.
Confirmed that Copilot generates responses successfully.
