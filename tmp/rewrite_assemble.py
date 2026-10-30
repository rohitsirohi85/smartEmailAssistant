from pathlib import Path
p=Path(r'E:\email-writer-sb\tmp\appendices.py'); s=p.read_text(encoding='utf-8')
a=s.index('# Merge exactly 50 supplemental pages onto the existing 20-page report.')
new=r'''# Merge the 53-page appendix after rebuilding the front matter to match the supplied 75-page format.
base_reader=PdfReader(str(BASE)); add_reader=PdfReader(str(ADD))
assert len(base_reader.pages)==20, len(base_reader.pages)
assert len(add_reader.pages)==53, len(add_reader.pages)

# Build two contents pages using the printed chapter page numbers used in the report.
def make_toc_page(title,rows):
    out=BytesIO(); c=canvas.Canvas(out,pagesize=A4)
    c.setFont("Times-Bold",14); c.drawCentredString(A4[0]/2,775,title)
    y=742
    for label,page_no,level,is_heading in rows:
        if is_heading:
            y-=5
            font="Times-Bold"; size=10.2; indent=0; step=21
        else:
            font="Times-Roman"; size=9.4; indent=16 if level==1 else 31; step=16
        x=68+indent
        c.setFont(font,size); c.drawString(x,y,label)
        num=str(page_no); nw=c.stringWidth(num,font,size)
        labelw=c.stringWidth(label,font,size)
        dotw=c.stringWidth(". ","Times-Roman",8.5)
        count=max(0,int((526-x-labelw-nw-10)/dotw))
        if count:
            c.setFont("Times-Roman",8.5); c.drawString(x+labelw+5,y,". "*count)
        c.setFont(font,size); c.drawRightString(526,y,num)
        y-=step
    c.showPage(); c.save(); out.seek(0); return PdfReader(out).pages[0]

toc1_rows=[
("CHAPTER 1: INTRODUCTION","1-2",0,True),
("1.1 Need Identification","1",1,False),
("1.2 Identification of Problem","1",1,False),
("1.3 Identification of Tasks","1-2",1,False),
("1.3.1 Functional tasks","1",2,False),
("1.3.2 Engineering and documentation tasks","2",2,False),
("1.4 Timeline","2",1,False),
("1.5 Organization of the Report","2",1,False),
("CHAPTER 2: BACKGROUND STUDY","3-5",0,True),
("2.1 Timeline of the Reported Problem","3",1,False),
("2.2 Proposed Solution","3-4",1,False),
("2.3 Bibliometric Analysis","4",1,False),
("2.4 Review Summary","4",1,False),
("2.5 Problem Definition","5",1,False),
("2.6 Goals / Objectives","5",1,False),
("2.7 Why Use These Technologies Over Other Options","5",1,False),
("CHAPTER 3: DESIGN AND PROCESS","6-9",0,True),
("3.1 Evaluation and Selection of Specifications / Features","6",1,False),
("3.2 Design Constraints","6",1,False),
("3.3 Design Flow","7",1,False),
("3.4 Creation of SmartMail Assistant","7-8",1,False),
("3.4.1 React and Material UI client","7",2,False),
("3.4.2 Spring Boot and Gemini service","8",2,False),
("3.4.3 Gmail extension","8",2,False),
("3.5 Logo Designing and Naming","9",1,False),
("3.6 Implementation Plan / Methodology","9",1,False),
]
toc2_rows=[
("CHAPTER 4: RESULT ANALYSIS AND VALIDATION","10-11",0,True),
("4.1 Implementation of Solution","10",1,False),
("4.1.1 Report Preparation","10",2,False),
("4.1.2 Project Management and Communication","10",2,False),
("4.1.3 Testing / Characterization / Interpretation / Data Validation","11",2,False),
("CHAPTER 5: CONCLUSION AND FUTURE WORK","12-13",0,True),
("5.1 Conclusion","12",1,False),
("5.2 Future Work","12-13",1,False),
("5.2.1 Improve prompt and response handling","12",2,False),
("5.2.2 Strengthen privacy and security","12",2,False),
("5.2.3 Make the Gmail integration more reliable","12",2,False),
("5.2.4 Expand validation and usability","13",2,False),
("5.2.5 Complete deployment and accessibility work","13",2,False),
("REFERENCES","14",0,True),
("APPENDICES","15-67",0,True),
("A. Source code and system walkthrough","15-19",1,False),
("B. Operations and user guide","20-23",1,False),
("C. Application screenshots","24-25",1,False),
("D. API, data handling, and security","26-30",1,False),
("E. Extended validation plan","31-36",1,False),
("F. Maintenance and handover","37-39",1,False),
("G. Project requirements and design record","40-45",1,False),
("H. Interaction and component design","46-51",1,False),
("I. Detailed validation and evidence worksheets","52-57",1,False),
("J. Deployment, quality, and handover reference","58-61",1,False),
("K. Implementation reference and release evidence","62-67",1,False),
]

# Abstract continuation follows the format's two-page abstract placement.
abstract_style=ParagraphStyle(name="AbstractContinuation",fontName="Times-Roman",fontSize=10.8,leading=15.3,alignment=TA_JUSTIFY,spaceAfter=9)
abstract_title=ParagraphStyle(name="AbstractContinuationTitle",fontName="Times-Bold",fontSize=14,leading=18,alignment=TA_CENTER,spaceAfter=14)
abstract_parts=[
"The implementation is organized around a deliberately small request path. The React page captures a message and an optional tone, performs a blank-input check, and sends a JSON request to the backend. The Spring Boot controller binds the request and delegates prompt construction and provider communication to a service. The service submits a contents-and-parts payload to Gemini and extracts text from the first returned candidate. The web client displays the result and offers a copy action. The Chrome extension uses a separate browser-side path: it watches Gmail page changes, attempts to add an AI Reply control, reads visible message text, calls the same endpoint, and attempts to place the response in the compose area.",
"This separation demonstrates how a generative service can be shared across a standalone interface and a browser integration. It also creates integration responsibilities at each boundary. The request DTO and API currently accept a compact contract, while server-side validation, response typing, upstream error mapping, timeout policy, and deployment-specific configuration need further work. The model response parser assumes a fixed nested shape. The Gmail path depends on page selectors that can change, and the web and extension clients do not expose identical tone choices. These details should be addressed before users rely on the application for sensitive or time-critical correspondence.",
"The project is intended to support human drafting rather than autonomous communication. The generated wording may omit relevant context, introduce unsupported details, or adopt an unsuitable tone. For this reason, the user must compare the proposal with the original message, verify names, dates, amounts, and commitments, edit the text where needed, and decide independently whether to copy or insert it. The application source reviewed for this report does not describe an automatic send feature, persistent message history, user accounts, or analytics. These boundaries are important when presenting the prototype and when explaining the permissions of the browser extension.",
"The report uses source inspection to describe existing behavior and treats unexecuted validation as planned work. No live Gemini response, measured response time, controlled usability study, or production deployment record was provided as evidence. The supplied screenshots document the initial React form and the Gmail compose view with the AI Reply control. They are interface captures rather than proof of model generation or successful draft insertion. A follow-up validation should use synthetic messages, record the application revision and environment, and distinguish mock-provider tests from requests that reach a live model service.",
"The main contribution is an integrated prototype that connects a React interface, a Spring Boot API, a Gemini request, and an attempted Gmail drafting action. The recommended next steps are to validate request fields and tone values on the server, make the prompt instructions consistent, handle empty and blocked provider responses, remove development-only endpoint assumptions, protect credentials, and test Gmail insertion without disturbing existing draft content. Accessibility, privacy notice, and operational monitoring should also be reviewed against the actual deployment. The work establishes a clear foundation for these improvements while keeping the limits of the current implementation visible."
]
abstract_buffer=BytesIO()
abstract_doc=SimpleDocTemplate(abstract_buffer,pagesize=A4,leftMargin=.92*inch,rightMargin=.92*inch,topMargin=.82*inch,bottomMargin=.72*inch,title="Abstract continuation")
abstract_story=[Paragraph("ABSTRACT (CONTINUED)",abstract_title)] + [Paragraph(text,abstract_style) for text in abstract_parts]
abstract_doc.build(abstract_story); abstract_buffer.seek(0); abstract_page=PdfReader(abstract_buffer).pages[0]

# Recreate the list of figures as a clean page without stale/hidden placeholder text.
fig_buffer=BytesIO(); fc=canvas.Canvas(fig_buffer,pagesize=A4)
fc.setFont("Times-Bold",14); fc.drawCentredString(A4[0]/2,770,"LIST OF FIGURES")
figs=[
    "Fig. 1. Graphical abstract of SmartMail Assistant",
    "Fig. 2. High-level system architecture",
    "Fig. 3. Request and response sequence",
    "Fig. 4. User workflow for generating a reply",
    "Fig. 5. Software component view",
    "Fig. C.1. SmartMail Assistant web interface in its initial state",
    "Fig. C.2. Gmail compose view with the AI Reply extension action",
]
fc.setFont("Times-Roman",11)
for n,label in enumerate(figs): fc.drawString(66,738-n*25,label)
fc.save(); fig_buffer.seek(0); fig_page=PdfReader(fig_buffer).pages[0]

toc1=make_toc_page("TABLE OF CONTENTS",toc1_rows)
toc2=make_toc_page("TABLE OF CONTENTS (CONTINUED)",toc2_rows)

# Replace the original compressed TOC and figure list; insert the continuation pages in template order.
base_writer=PdfWriter()
for i,page in enumerate(base_reader.pages):
    if i==2:
        base_writer.add_page(toc1)
        base_writer.add_page(toc2)
    elif i==3:
        base_writer.add_page(page)
        base_writer.add_page(abstract_page)
    elif i==4:
        base_writer.add_page(fig_page)
    else:
        base_writer.add_page(page)
assert len(base_writer.pages)==22, len(base_writer.pages)
assert len(add_reader.pages)==53, len(add_reader.pages)

writer=PdfWriter(); writer.append_pages_from_reader(base_writer); writer.append_pages_from_reader(add_reader)
writer.add_metadata({"/Title":"SmartMail Assistant Project Report","/Author":"Rishi Soni","/Subject":"Project report in Chandigarh University format with two supplied screenshots and technical appendices"})
with open(FINAL,"wb") as f: writer.write(f)
print(FINAL)
print("front_matter_and_chapters",len(base_writer.pages),"appendix_pages",len(add_reader.pages),"total",len(writer.pages))
'''
s=s[:a]+new
p.write_text(s,encoding='utf-8')
print('replaced final assembly')
