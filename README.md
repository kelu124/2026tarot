# 🔮 Signals from Tomorrow

> A Scenario Builder's Field Guide - An interactive tool for foresight professionals to discover weak signals and emerging trends

[![Live Demo](https://img.shields.io/badge/demo-live-success)](http://2025.kghosh.me/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📖 About

**Signals from Tomorrow** is an interactive web application designed for foresight professionals, scenario planners, and strategic thinkers. It serves as a serendipity engine that surfaces random combinations of change signals to spark imagination and inform scenario development.

Each visit presents a unique constellation of:
- 🌱 **Weak Signals** (5 items) - Early indicators of potential change
- 👥 **Behavioral Shifts** (3 items) - Evolving human patterns and adaptations  
- 💭 **Rising Concerns** (3 items) - Emerging anxieties and tensions
- ⚠️ **Issues in Motion** (3 items) - Evolving problems and challenges
- ⚡ **Technology Waves** (3 items) - New technological developments

## 🎯 Purpose

This tool helps foresight practitioners:
- Discover unexpected connections between signals
- Break out of familiar thinking patterns
- Generate scenario seeds through serendipitous combinations
- Explore the edges of change in multiple domains
- Practice pattern recognition across different types of signals

## 🌐 Live Demo

Visit the live application: [Your GitHub Pages URL]

## 📊 Data Sources

All signals in this collection are:
- **Curated at**: [substack.kghosh.me](https://substack.kghosh.me/)
- **Processed through**: [futures.kghosh.me](https://futures.kghosh.me/)
- **Human-guided**: Each link is selected and categorized in this newsletter

## 🚀 Features

- **Random sampling** for fresh perspectives each visit
- **Clean, distraction-free interface** optimized for reading and thinking
- **Direct linking** to source materials for deeper exploration
- **Responsive design** that works on desktop, tablet, and mobile
- **No tracking or analytics** - just you and the signals
- **Fast loading** with all data pre-compiled as JSON

## 🛠️ Technical Stack

- **Frontend**: Pure HTML5, CSS3, and vanilla JavaScript
- **Hosting**: GitHub Pages (static site)
- **Data Format**: JSON
- **Build Process**: Python scripts for data preparation

## 📁 Project Structure

```
.
├── docs/
│   ├── index.html              # Main application
│   └── data/
│       └── combined_data.json  # All signals data
├── transform.ipynb             # To create the jsons
└── README.md
```

## 🔧 Setup & Development

### Prerequisites

- Python 3.7+ (for data preparation)


### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/kelu124/2026tarot.git
   cd 2026tarot
   ```

2. **Prepare your data** (if updating signals)
   Run `Transform.ipynb`

3. **Run a local server**
   ```bash
   cd docs
   python -m http.server 8000
   ```

4. **Open in browser**
   ```
   http://localhost:8000
   ```

### Deploying to GitHub Pages

1. Push your changes to the `main` branch
2. Go to repository Settings → Pages
3. Set source to: `main` branch, `/docs` folder
4. Save and wait a few minutes for deployment

Your site will be live at: `https://yourusername.github.io/your-repo-name/`

## 📝 Data Format

The application expects a JSON file with this structure:

```json
{
  "seeds": [
    {
      "name": "Signal name",
      "description": "Description text",
      "change": "Type of change",
      "10-year": "10-year outlook",
      "driving-force": "Main driving force",
      "relevancy": "Relevance level",
      "src": "unique-id"
    }
  ],
  "behav": [
    {
      "name": "Behavior name",
      "description": "Description text",
      "relevancy": "Relevance level",
      "src": "unique-id"
    }
  ],
  "concern": [...],
  "issue": [...],
  "tech": [...]
}
```

## 🎨 Customization

### Change Number of Items

Edit the JavaScript in `index.html`:

```javascript
// For seeds (currently 5)
const seeds = getRandomSamples(data.seeds, 5);

// For other categories (currently 3)
const samples = getRandomSamples(groupData, 3);
```

### Modify Section Titles

Find the `dataGroups` array in `index.html`:

```javascript
const dataGroups = [
  { 
    name: '👥 Your Custom Title', 
    key: 'behav',
    intro: 'Your custom description here'
  },
  // ...
];
```

### Change Color Scheme

Modify the CSS gradient and accent colors:

```css
/* Main gradient */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Accent colors */
color: #667eea;
border-left: 4px solid #667eea;
```

## 🤝 Contributing

While this is a personal curation project, suggestions are welcome!

**Ways to contribute:**
- Report bugs or UI issues
- Suggest improvements to the interface
- Share how you're using this tool in your practice

Please open an issue to discuss any significant changes.

## 📚 Use Cases

This tool has been used for:
- **Scenario workshops** - Generating starting points for group exploration
- **Personal practice** - Daily inspiration for futures thinking
- **Research** - Discovering connections across domains
- **Teaching** - Introducing students to weak signals methodology
- **Consulting** - Client presentation of emerging trends

## 🔗 Related Projects

- [futures.kghosh.me](https://futures.kghosh.me/) - Full futures library
- [substack.kghosh.me](https://substack.kghosh.me/) - Signal curation and analysis

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**K Ghosh**

- Substack: [substack.kghosh.me](https://substack.kghosh.me/)
- Futures Library: [futures.kghosh.me](https://futures.kghosh.me/)

## 🙏 Acknowledgments

- To all the authors, researchers, and thinkers whose work is linked here
- To the foresight community for inspiring this methodology
- To everyone who believes in thinking carefully about tomorrow

## 💡 Philosophy

> "The future is already here—it's just not evenly distributed."  
> — William Gibson

This tool is built on the belief that:
- Weak signals matter as much as strong trends
- Serendipity is a feature, not a bug
- Pattern recognition is a learnable skill
- The most interesting futures emerge at intersections
- Good foresight requires both breadth and depth

---

**Note**: The signals displayed are curated interpretations of publicly available information. They are meant to inspire thinking and should not be taken as predictions or recommendations.

*Built with ❤️ for futures thinkers everywhere*