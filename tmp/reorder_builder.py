from pathlib import Path
p=Path(r'E:\email-writer-sb\tmp\appendices.py'); s=p.read_text(encoding='utf-8')
a=s.index('# Two related subsections per page')
b=s.index('class NumberedDoc',a)
new=r'''# Two related subsections per page keep the appendices compact and readable.
def add_group(start_idx,end_idx):
    for idx in range(start_idx,end_idx,2):
        if idx in appendix_titles:
            story.append(Paragraph(appendix_titles[idx],styles["AppTitle"]))
        add_entry_content(entries[idx])
        story.append(Spacer(1,5))
        add_entry_content(entries[idx+1])
        story.append(PageBreak())

def add_screenshot_section():
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

add_group(0,10)      # Appendix A
add_group(10,18)     # Appendix B
add_screenshot_section() # Appendix C
add_group(18,28)     # Appendix D
add_group(28,40)     # Appendix E
add_group(40,46)     # Appendix F
add_group(46,58)     # Appendix G
add_group(58,70)     # Appendix H
add_group(70,82)     # Appendix I
add_group(82,90)     # Appendix J

'''
s=s[:a]+new+s[b:]
s=s.replace('The present revised PDF reserves screenshot locations but does not contain captured application screenshots or claim a live Gemini demonstration.','Two supplied screenshots are included: the web application initial state and the Gmail compose view with the AI Reply control. The remaining three figure areas are reserved for later captures; no live Gemini result is claimed.')
p.write_text(s,encoding='utf-8')
print('reordered sections')
