# PyResume 📄🤖

An AI-powered resume analyzer that provides intelligent matching between resumes and job descriptions using Google's Gemini AI.

## 🚀 Features

- **Smart Resume Analysis**: Goes beyond keyword matching with contextual understanding
- **Multi-format Support**: Processes both PDF and DOCX resume files
- **Structured Reports**: Clean, formatted output with skills matching and recommendations
- **Compatibility Scoring**: Instant percentage-based matching for quick decisions
- **Actionable Insights**: Specific improvement suggestions for candidates
- **Recruiter-friendly**: Quick compatibility overview with detailed breakdowns

## 🛠️ How It Works

1. **Upload**: Place resume files (PDF/DOCX) in the `uploads/` folder
2. **Input**: Enter the job description when prompted
3. **Analysis**: Gemini AI compares resume content against job requirements
4. **Report**: Get detailed analysis with skills matching, strengths, and recommendations

## 📋 Requirements

```
google-generativeai
PyMuPDF (fitz)
python-docx
```

## ⚙️ Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/pyresume.git
   cd pyresume
   ```

2. **Install dependencies**
   ```bash
   pip install google-generativeai PyMuPDF python-docx
   ```

3. **Set up API key**
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```

4. **Create uploads folder**
   ```bash
   mkdir uploads
   ```

## 🚀 Usage

1. **Add resume files** to the `uploads/` folder
2. **Run the analyzer**:
   ```bash
   python main.py
   ```
3. **Enter job description** when prompted
4. **Get your analysis report**!

## 📊 Sample Output

```
📊 Resume Analysis Report

### 1. Candidate Information
- Resume File: john_doe_resume.pdf
- Key Details: John Doe, Software Engineer

### 2. Job Description Overview
- Length: 1,245 characters
- Excerpt: "Looking for a Python developer with AWS experience..."

### 3. Skills Matching
- ✅ Matched Skills: Python, AWS, Git, SQL
- ❌ Missing Skills: Docker, Kubernetes, React

### 4. Resume Strengths
- Strong Python development experience (3+ years)
- Proven AWS cloud architecture skills
- Leadership experience in cross-functional teams

### 5. Recommendations
- Add Docker/containerization experience to skills section
- Highlight specific AWS services used (EC2, S3, Lambda)
- Quantify achievements with metrics where possible

### 6. Summary
Strong technical foundation with 78% match. Candidate demonstrates solid Python and cloud experience but would benefit from adding modern DevOps tools and frontend technologies mentioned in the job requirements.
```

## 🔧 Project Structure

```
pyresume/
├── main.py              # Main application file
├── extractor.py         # Text extraction from PDF/DOCX
├── uploads/             # Folder for resume files
├── README.md            # This file
└── requirements.txt     # Dependencies
```

## 🎯 Future Enhancements

- [ ] Web interface with drag-and-drop upload
- [ ] Batch processing for multiple resumes
- [ ] Export reports to PDF/HTML
- [ ] Advanced scoring algorithms
- [ ] Resume optimization suggestions
- [ ] Integration with job boards

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Note

Make sure to keep your Gemini API key secure and never commit it to version control. Use environment variables for production deployments.

## 📧 Contact

Your Name - your.email@example.com
Project Link: https://github.com/yourusername/pyresume
