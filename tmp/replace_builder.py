from pathlib import Path
p=Path(r'E:\email-writer-sb\tmp\appendices.py'); s=p.read_text(encoding='utf-8')
a=s.index('story=[]\ndef add_entry_page')
b=s.index('class NumberedDoc',a)
new=r'''story=[]
appendix_titles={
    0:"APPENDIX A - SOURCE CODE AND SYSTEM WALKTHROUGH",
    10:"APPENDIX B - OPERATIONS AND USER GUIDE",
    18:"APPENDIX D - API, DATA HANDLING, AND SECURITY",
    28:"APPENDIX E - EXTENDED VALIDATION PLAN",
    40:"APPENDIX F - MAINTENANCE AND HANDOVER",
    46:"APPENDIX G - PROJECT REQUIREMENTS AND DESIGN RECORD",
    58:"APPENDIX H - INTERACTION AND COMPONENT DESIGN",
    70:"APPENDIX I - DETAILED VALIDATION AND EVIDENCE WORKSHEETS",
    82:"APPENDIX J - DEPLOYMENT, QUALITY, AND HANDOVER REFERENCE",
}
def add_entry_content(entry):
    story.append(Paragraph(entry["title"],styles["AppSub"]))
    story.append(p(entry["intro"]))
    story.append(p("Implementation notes", "AppSub"))
    story.append(bullets(entry["points"]))
    story.append(p("Review and interpretation", "AppSub"))
    story.append(p(entry["review"]))
    if entry["table"]:
        story.append(Spacer(1,2))
        story.append(table(entry["table"],[1.3*inch,1.7*inch,1.65*inch,1.35*inch] if len(entry["table"][0])==4 else [1.3*inch,2.3*inch,2.4*inch]))

# Two related subsections per page keep the appendices compact and readable.
for start_idx,end_idx in ((0,10),(10,18),(18,28),(28,40),(40,46),(46,58),(58,70),(70,82),(82,90)):
    for idx in range(start_idx,end_idx,2):
        if idx in appendix_titles:
            story.append(Paragraph(appendix_titles[idx],styles["AppTitle"]))
        add_entry_content(entries[idx])
        story.append(Spacer(1,5))
        add_entry_content(entries[idx+1])
        story.append(PageBreak())

# Appendix C keeps a full page for each workflow image or reserved capture area.
story.append(Paragraph("APPENDIX C - APPLICATION SCREENSHOTS",styles["AppTitle"]))
for title,intro,caption,image_path in screens:
    story.append(Paragraph(title,styles["AppSub"]))
    story.append(p(intro))
    story.append(Spacer(1,12))
    if image_path:
        img=Image(image_path,width=6.15*inch,height=4.05*inch,kind="proportional",hAlign="CENTER")
        story.append(img)
    else:
        frame=Table([[Paragraph("SCREENSHOT TO BE INSERTED HERE",styles["AppSmallBold"]),]],colWidths=[6.15*inch],rowHeights=[4.05*inch],hAlign="CENTER")
        frame.setStyle(TableStyle([("BOX",(0,0),(-1,-1),1.0,colors.HexColor("#555555")),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#FAFAFA"))]))
        story.append(frame)
    story.append(Paragraph(caption,styles["AppCaption"]))
    if not image_path:
        story.append(p("Capture note: use the current application build and fictional test data. Remove identifying inbox content and never show an API key.","AppSmall"))
    story.append(PageBreak())

'''
s=s[:a]+new+s[b:]
p.write_text(s,encoding='utf-8')
print('replaced builder')
