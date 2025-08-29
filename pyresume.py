import google.generativeai as Genai 
from extractor import extract_text

job_description = input("Enter the job description of the company: ")
def gemini_setup():
   Api_key = "your_gemini_api_key" 
   Genai.configure(api_key=Api_key) 
   model = Genai.GenerativeModel("gemini-2.0-flash")
   return model 

def get_report(): 
   model = gemini_setup()
   resume_text = extract_text()
   prompt = f''' You are an expert resume analyzer, This is the resume: {resume_text} and this is job description: {job_description} You are an expert career coach and ATS specialist. 
Analyze the given RESUME and JOB DESCRIPTION. 

Your task:
1. Identify candidate information (file name, basic details if available).
2. Summarize the Job Description in 2-3 lines.
3. Compare the skills in the resume vs. the skills required in the job description.
   - List Matched Skills with ✅
   - List Missing Skills with ❌
4. Highlight 3–5 Strengths of the resume.
5. Give 3–5 clear Recommendations for improvement.
6. Provide a final Summary with a match percentage estimate (out of 100).

Format the output EXACTLY like this:

📊 Resume Analysis Report

### 1. Candidate Information
- Resume File: <filename>
- Key Details: <name, role if found>

### 2. Job Description Overview
- Length: <number of characters>
- Excerpt: "<short snippet of JD>"

### 3. Skills Matching
-  Matched Skills: <comma separated>
-  Missing Skills: <comma separated>

### 4. Resume Strengths
- Point 1
- Point 2
- Point 3

### 5. Recommendations
- Point 1
- Point 2
- Point 3

### 6. Summary
<One paragraph summary + Match %>
give the report not in first person view but in statement wise.
'''
   chat = model.start_chat() 
   response = chat.send_message(prompt) 
   return response.text 

report = get_report()
print(report) 