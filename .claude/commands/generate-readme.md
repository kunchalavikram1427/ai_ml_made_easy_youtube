---
description: Generate a beautifully formatted README (.md) from a PowerPoint (.pptx) file
allowed-tools: Bash, Read, Write, Edit, AskUserQuestion, WebFetch, Agent
---

# Generate README from PPTX

You are a README generator that converts PowerPoint (.pptx) files into well-formatted, visually appealing Markdown README files for the ai_ml_made_easy_youtube repository.

## Step 1: Get Input PPTX Path

If no PPTX file path was provided as an argument (`$ARGUMENTS`), ask the user:
- "What is the path to the .pptx file you want to convert?"

Validate the file exists using `ls -la <path>`. If it doesn't exist, inform the user and ask again.

## Step 2: Extract PPTX Content

Use python3 to extract text content from the PPTX file. Install python-pptx if needed:

```bash
pip3 install python-pptx 2>/dev/null
```

Then extract all slide text:

```python
python3 -c "
from pptx import Presentation
import json, sys

prs = Presentation(sys.argv[1])
slides = []
for i, slide in enumerate(prs.slides):
    slide_data = {'slide_number': i + 1, 'shapes': []}
    for shape in slide.shapes:
        if shape.has_text_frame:
            text = shape.text_frame.text.strip()
            if text:
                slide_data['shapes'].append(text)
        if shape.has_table:
            table_data = []
            for row in shape.table.rows:
                row_data = [cell.text.strip() for cell in row.cells]
                table_data.append(row_data)
            slide_data['shapes'].append({'table': table_data})
    if slide_data['shapes']:
        slides.append(slide_data)
print(json.dumps(slides, indent=2))
" "<PPTX_PATH>"
```

## Step 3: Determine Output Path and Filename

1. Derive the default markdown filename from the PPTX filename:
   - Example: `common_ai_ml_terminology_part01.pptx` → `common_ai_ml_terminology_part01.md`

2. Infer the likely course folder from the filename:
   - Look at the PPTX name and try to map it to an existing folder under `courses/`
   - For AI/ML related files → `courses/ai_ml_foundations`
   - For MCP related files → `courses/mcp`
   - For Claude Code related files → `courses/claude_code`
   - If unclear, suggest a reasonable folder name

3. Ask the user to confirm or override using AskUserQuestion:
   - header: "Output path"
   - question: "The output file will be `courses/<inferred_folder>/<filename>.md`. Is this correct?"
   - options:
     - "Yes, that's correct" — proceed with the inferred path
     - "No, let me specify" — ask for the full output path

4. Check if the output file already exists:
   ```bash
   ls -la <output_path>
   ```
   If it exists, use AskUserQuestion:
   - header: "File exists"
   - question: "The file `<filename>.md` already exists at the target location. What would you like to do?"
   - options:
     - "Overwrite it" — proceed with overwriting
     - "Use a different name" — ask user for a new filename
     - "Cancel" — abort the operation

## Step 4: Security Check

Before generating the README, scan the extracted content for potentially sensitive data:
- API keys, tokens, secrets (patterns like `sk-`, `api_key`, `token`, `password`, `secret`)
- Internal URLs, IP addresses, or hostnames that look non-public
- Email addresses or personal identifiers
- Credentials or connection strings

If any are found:
- Warn the user about the specific items found
- Ask if they want to proceed (those items will be redacted/omitted)
- Replace sensitive content with placeholder text like `[REDACTED]` or `<your-api-key-here>`

## Step 5: Generate the README

Using the extracted slide content, generate a beautifully formatted Markdown file following these guidelines:

### Formatting Rules

**Heading Icons** — Use relevant emojis/icons as prefixes for headings:
- `#` (H1): Use a prominent icon matching the topic (e.g., `# 🧠 Common AI/ML Terminology`)
- `##` (H2): Use section-relevant icons (e.g., `## 📚 Key Concepts`, `## 🔍 Deep Dive`, `## 🎯 Learning Objectives`)
- `###` (H3): Use contextual icons (e.g., `### 💡 Definition`, `### ⚙️ How It Works`)

**Table of Contents** — Always include a TOC near the top:
```markdown
## 📑 Table of Contents

- [Key Concepts](#-key-concepts)
- [Deep Dive](#-deep-dive)
- [Summary](#-summary)
- [References](#-references)
```

**Content Structure** — Follow this general layout:
1. Title with emoji
2. Brief description/intro paragraph
3. Table of Contents
4. Learning Objectives (if applicable)
5. Main content sections derived from slides
6. Code blocks (with language hints) for any shell commands or code snippets
7. Key takeaways / Summary
8. References / Further Reading (if applicable)

**Visual Enhancements:**
- Use **bold** for key terms on first introduction
- Use `inline code` for technical terms, commands, model names
- Use blockquotes (`>`) for important notes or callouts:
  ```markdown
  > 💡 **Key Insight:** Transformers are the backbone of modern LLMs.
  ```
- Use tables for comparisons or structured data
- Use bullet/numbered lists for sequential or grouped information
- Use horizontal rules (`---`) between major sections
- Use collapsible sections for optional/advanced content:
  ```markdown
  <details>
  <summary>🔎 Click to expand: Advanced Details</summary>

  Content here...

  </details>
  ```

**Content Enhancement — Go Beyond the Slides:**
- DO NOT just transcribe the slides — significantly enrich and expand upon them
- Add real-world architecture patterns and system design context where relevant
- Add latest industry examples (last year to current year era and beyond): mention current models, tools, companies, and trends
- Add "How It Works Under the Hood" explanations that go one level deeper than surface definitions
- Add architecture/flow diagrams using ASCII/text where they clarify a concept
- Add comparison tables that highlight trade-offs, not just definitions
- Add "When to Use What" practical guidance for practitioners
- Include real numbers where helpful (model sizes, training data scales, latency expectations)
- Use analogies and plain-English explanations to make technical concepts accessible
- Ensure technical accuracy — do not invent claims, but DO add well-known technical context
- Keep the tone educational and accessible — target a broad audience of learners, not just advanced engineers
- DO NOT include any images from the PPTX (they won't render in markdown without the files)
- DO NOT expose or include any sensitive data found during the security check

**Code Snippets Policy:**
- Do NOT include code snippets (Python, pseudo-code, or otherwise) by default
- Code snippets should ONLY be included when the PPTX topic is specifically about programming (e.g., Python programming, coding tutorials, API usage)
- For non-programming topics, explain concepts using plain English, analogies, ASCII flow diagrams, and tables instead of code
- Use `bash` / `shell` blocks ONLY for terminal commands when the topic requires them

## Step 6: Ask for YouTube Video/Playlist Link

Before writing the file, ask the user if they have a YouTube video or playlist link for this topic using AskUserQuestion:
- header: "YouTube link"
- question: "Do you have a YouTube video or playlist link for this topic?"
- options:
  - "Yes, let me provide it" — ask the user for the URL, then use it in the course README table
  - "No, mark as Pending" — use "Pending" in the YouTube column of the course README table

If the user provides a link, validate it looks like a YouTube URL (contains `youtube.com` or `youtu.be`). Store it for use in Step 8 when updating the course folder README table. Format it as a short markdown link: `[Video](url)` or `[Playlist](url)` based on whether it contains `/playlist?` or `/watch?`.

## Step 7: Write the README File

Write the generated markdown to the determined output path.

Ensure the parent directory exists:
```bash
mkdir -p <parent_directory>
```

Then write the file using the Write tool.

## Step 8: Update Course Folder README

Check if a `README.md` exists in the course folder (e.g., `courses/ai_ml_foundations/README.md`):

### If README.md does NOT exist — Create it:

Generate a course-level README.md with this structure:

```markdown
# <emoji> <Course Title>

<Brief description of the course — 1-2 sentences explaining what this course covers.>

---

## 📑 Table of Contents

- [Topics](#-topics)
- [How to Use](#-how-to-use)

---

## 📚 Topics

| # | Topic | Description | YouTube Video/Playlist |
|---|-------|-------------|---------------|
| 1 | [<Topic Title>](./<filename>.md) | <Brief 1-line description> | <YouTube link from Step 6, or "Pending"> |

---

## 🚀 How to Use

1. Start with the topics in order
2. Each topic links to a detailed README with explanations and examples
3. YouTube videos will be added as they are published

---

> 📺 **Channel:** [AI ML Made Easy](https://www.youtube.com/@DevOpsMadeEasy)
```

### If README.md DOES exist — Update it:

1. Read the existing README.md
2. Find the Topics table
3. Add a new row for the newly created topic README:
   - Derive a human-readable topic title from the filename (e.g., `common_ai_ml_terminology_part01` → `Introduction to Common AI ML Terminology Part 01`)
   - Increment the topic number
   - Add the link, description, and the YouTube link from Step 6 (or "Pending" if none provided)
4. Use the Edit tool to insert the new row into the existing table
5. DO NOT overwrite or remove any existing entries

## Step 9: Confirmation

After completing all steps, provide a summary to the user:

```
✅ README generated successfully!

📄 Output file: <output_path>
📁 Course folder: <course_folder>
📋 Course README: <course_readme_status — created/updated>

Summary:
- Extracted content from <N> slides
- Generated <N> sections
- <Security findings if any>
```
