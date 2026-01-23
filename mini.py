import streamlit as st
st.title("VAK Quiz")
st.write("Welcome to the VAk Quiz! Please answer the following questions to find out the best learning style for you.")
v,s,k=0,0,0
#question-1
q1=st.radio("1.when you learn something new, you prefer to:",["some hands-on experience","watch a demonstration","listen to an experiance"],index=None)
if q1=="some hands-on experience":
    v+=1
elif q1=="watch a demonstration":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q1"):
    explain={
        "some hands-on experience":"You are Kinesthetic learner (you learn by doing / practicing).",
        "watch a demonstration":"You are Visual learner (you learn by seeing videos, images, diagrams).",
        "listen to an experiance":"You are Auditory learner (you learn by listening, discussions, audio)."
    }
    
    st.success("your selected option:")
    st.write("👉",q1)
    
    st.info("explain: ")
    st.write(explain[q1])
#question2
q2=st.radio("2.If I forget something, I remember it by...",["Picture in mind", "Hearing again", "Doing again"],index=None)
if q2=="Picture in mind":
    v+=1
elif q2=="Hearing again":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q2"):
    explain={
        "Picture in mind":"You are a Visual learner (you learn best by seeing videos, images, diagrams).",
        "Hearing again":"You are an Auditory learner (you learn best by listening, discussions, and audio).",
        "Doing again":"You are a Kinesthetic learner (you learn best by doing and practicing)."
    }
    st.success("your selected option: ")
    st.write("👉",q2)
    st.info("explanation:")
    st.write(explain[q2])
#question-3
q3=st.radio("3.In class, I understand better when the teacher...",["Shows slides/board", "Explains verbally", "Gives activities"],index=None)
if q3=="Shows slides/board":
    v+=1
if q3=="Explains verbally":
    s+=1
if q3=="Gives activities":
    k+=1
if st.button("submit",key="submit_q3"):
    explain={
        "Shows slides/board": "You prefer learning by seeing diagrams, charts, and pictures.",
        "Explains verbally": "You prefer learning by listening to explanations and discussions.",
        "Gives activities": "You prefer learning by doing hands-on practice."
    }
    st.success("your selected option:")
    st.write("👉",q3)
    st.info("explanation:")
    st.write(explain[q3])
#question4
q4=st.radio("4.When getting directions, I prefer...",["Map/picture", "Someone tells directions", "Go once & remember"],index=None)
if q4=="Map/picture":
    v+=1
elif q4=="Someone tells directions":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q4"):
       explain={
        "Map/picture": "You prefer directions using a map or visual landmarks.",
        "Someone tells directions": "You prefer directions when someone tells you the steps clearly.",
        "Go once & remember": "You prefer learning directions by going once and remembering the route."
       }
       st.success("your selected option:")
       st.write("👉",q4)
       st.info("explanation:")
       st.write(explain[q4])
#question5
q5=st.radio("5.While studying, I like to...",["Highlight notes", "Read aloud/audio", "Write & practice"],index=None)
if q5=="Highlight notes":
    v+=1
elif q5=="Read aloud/audio":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q5"):
        explain={
        "Highlight notes": "You study well when you use colors and highlighting in notes.",
        "Read aloud/audio": "You study well when you read aloud or listen to audio lessons.",
        "Write & practice": "You study well when you write and practice repeatedly."
        }
        st.success("your selected option:")
        st.write("👉",q5)
        st.info("explanation:")
        st.write(explain[q5])
#question6
q6=st.radio("6.To remember names, I focus on...",["Face/look", "Sound of name", "Handshake/experience"],index=None)
if q6=="Face/look":
    v+=1
elif q6=="Sound of name":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q6"):
        explain={
        "Face/look": "You remember people by their face and appearance.",
        "Sound of name": "You remember people by the sound of their name.",
        "Handshake/experience": "You remember people through meeting and interaction experience."
        }
        st.success("your selected option:")
        st.write("👉",q6)
        st.info("explanation:")
        st.write(explain[q6])
#question7
q7=st.radio("7.In free time, I enjoy...",["Watching videos", "Listening music/podcast", "Sports/games"],index=None)
if q7=="Watching videos":
    v+=1
elif q7=="Listening music/podcast":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q7"):
        explain={
         "Watching videos": "You enjoy learning or relaxing by watching videos and visuals.",
        "Listening music/podcast": "You enjoy music, podcasts, and audio learning.",
        "Sports/games": "You enjoy activities that involve movement like sports and games."
        }
        st.success("your selected option:")
        st.write("👉",q7)
        st.info("explanation:")
        st.write(explain[q7])
#question8
q8=st.radio("8.When solving a problem, I usually...",["Visualize", "Discuss/talk", "Try practical methods"],index=None)
if q8=="Visualize":
    v+=1
elif q8=="Discuss/talk":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q8"):
        explain={
        "Visualize": "You solve problems by imagining the steps in your mind.",
        "Discuss/talk": "You solve problems by talking through ideas or discussing with others.",
        "Try practical methods": "You solve problems by trying different methods practically."
        }
        st.success("your selected option:")
        st.write("👉",q8)
        st.info("explanation:")
        st.write(explain[q8])
#question9
q9=st.radio("9.I remember phone numbers better by...",["See number", "Repeat aloud", "Type again and again"],index=None)
if q9=="See number":
    v+=1
elif q9=="Repeat aloud":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q9"):
        explain={
        "See number": "You remember numbers by seeing them clearly in your mind.",
        "Repeat aloud": "You remember numbers by repeating them aloud again and again.",
        "Type again and again": "You remember numbers by typing or writing them repeatedly."
        }
        st.success("your selected option:")
        st.write("👉",q9)
        st.info("explanation:")
        st.write(explain[q9])
#question10
q10=st.radio("10.To learn a new app, I prefer...",["Watch tutorial", "Listen to instructions", "Try exploring"],index=None)
if q10=="Watch tutorial":
    v+=1
elif q10=="Listen to instructions":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q10"):
        explain={
        "Watch tutorial": "You learn new apps easily by watching tutorials and demonstrations.",
        "Listen to instructions": "You learn new apps easily by listening to step-by-step instructions.",
        "Try exploring": "You learn new apps easily by exploring and trying features yourself."
        }
        st.success("your selected option:")
        st.write("👉",q10)
        st.info("explanation:")
        st.write(explain[q10])
#question11
q11=st.radio("11.I feel comfortable when I...",["See clearly", "Hear clearly", "Move/do"],index=None)
if q11=="See clearly":
    v+=1
elif q11=="Hear clearly":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q11"):
        explain={
        "See clearly": "You feel comfortable when you can see your surroundings clearly.",
        "Hear clearly": "You feel comfortable when you can hear sounds properly.",
        "Move/do": "You feel comfortable when you can move around and stay active."
        }
        st.success("your selected option:")
        st.write("👉",q11)
        st.info("explanation:")
        st.write(explain[q11])
#question12
q12=st.radio("12.When reading, I enjoy...",["With pictures", "Reading aloud", "Apply/act out"],index=None)
if q12=="With pictures":
    v+=1
elif q12=="Reading aloud":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q12"):
        explain={
        "With pictures": "You enjoy reading more when the content has pictures and visuals.",
        "Reading aloud": "You enjoy reading by speaking the words and hearing your voice.",
        "Apply/act out": "You enjoy reading when you can apply it or act it out in real life."
        }
        st.success("your selected option:")
        st.write("👉",q12)
        st.info("explanation:")
        st.write(explain[q12])
#question13
q13=st.radio("13.When explaining something, I use...",["Drawings/examples", "Verbal explanation", "Demonstration"],index=None)
if q13=="Drawings/examples":
    v+=1
elif q13=="Verbal explanation":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q13"):
        explain={
        "Drawings/examples": "You explain things better by showing drawings and examples.",
        "Verbal explanation": "You explain things better by using words and speaking clearly.",
        "Demonstration": "You explain things better by showing how it works practically."
        }
        st.success("your selected option:")
        st.write("👉",q13)
        st.info("explanation:")
        st.write(explain[q13])
#question14
q14=st.radio("14.In exams, I perform best when...",["Remember visuals", "Recall voice", "Practice problems"],index=None)
if q14=="Remember visuals":
    v+=1
elif q14=="Recall voice":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q14"):
    explain={
        "Remember visuals": "You perform well in exams by remembering diagrams and visual notes.",
        "Recall voice": "You perform well in exams by remembering what the teacher said.",
        "Practice problems": "You perform well in exams by practicing lots of questions."
    }
    st.success("your option is:")
    st.write("👉",q14)
    st.info("explanation:")
    st.write(explain[q14])
#question15
q15=st.radio("15.I like teachers who...",["Use notes/slides", "Use stories", "Give tasks"],index=None)
if q15=="Use notes/slides":
    v+=1
elif q15=="Use stories":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q15"):
    explain={
        "Use notes/slides": "You like teachers who teach using notes, slides, and visual support.",
        "Use stories": "You like teachers who explain using speech and stories.",
        "Give tasks": "You like teachers who give tasks and practice activities."
    }
    st.success("your option is:")
    st.write("👉",q15)
    st.info("explanation:")
    st.write(explain[q15])
#question16
q16=st.radio("16.When I get bored, I usually...",["Look around", "Talk/hum", "Move hands/legs"],index=None)
if q16=="Look around":
    v+=1
elif q16=="Talk/hum":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q16"):
    explain={
        "Look around": "When bored, you start observing things around you.",
        "Talk/hum": "When bored, you start talking, humming, or making sounds.",
        "Move hands/legs": "When bored, you feel restless and start moving."
    }
    st.success("your option is:")
    st.write("👉",q16)
    st.info("explanation:")
    st.write(explain[q16])
#question17
q17=st.radio("17.If I buy something new, I first...",["Design look", "Reviews", "Touch & test"],index=None)
if q14=="Design look":
    v+=1
elif q14=="Reviews":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q17"):
    explain={
        "Design look": "You choose products mostly by their design and appearance.",
        "Reviews": "You choose products by listening to reviews and opinions.",
        "Touch & test": "You choose products by touching and testing them."
    }
    st.success("your option is:")
    st.write("👉",q17)
    st.info("explanation:")
    st.write(explain[q17])
#question18
q18=st.radio("18.In a lecture, I remember more by...",["Notes/slides", "Listening", "Activities"],index=None)
if q18=="Notes/slides":
    v+=1
elif q18=="Listening":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q18"):
    explain={
        "Notes/slides": "You remember lectures better by looking at notes and slides.",
        "Listening": "You remember lectures better by listening carefully.",
        "Activities": "You remember lectures better by doing activities and participation."
    }
    st.success("your option is:")
    st.write("👉",q18)
    st.info("explanation:")
    st.write(explain[q18])
#question19
q19=st.radio("19.I learn coding best when...",["Flowcharts/code view", "Listen explain", "Code + debug"],index=None)
if q19=="Flowcharts/code view":
    v+=1
elif q19=="Listen explain":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q19"):
    explain={
        "Flowcharts/code view": "You learn coding better by seeing code patterns and flowcharts.",
        "Listen explain": "You learn coding better when someone explains the logic verbally.",
        "Code + debug": "You learn coding better by writing code and debugging errors."
    }
    st.success("your option is:")
    st.write("👉",q19)
    st.info("explanation:")
    st.write(explain[q19])
#question20
q20=st.radio("20.When I’m stressed, I feel better by...",["Watch relax", "Music", "Walk/move"],index=None)
if q20=="Watch relax":
    v+=1
elif q20=="Music":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q20"):
    explain={
        "Watch relax": "You reduce stress by watching calm or enjoyable visuals.",
        "Music": "You reduce stress by listening to music or relaxing sounds.",
        "Walk/move": "You reduce stress by walking or doing physical movement."
    }
    st.success("your option is:")
    st.write("👉",q20)
    st.info("explanation:")
    st.write(explain[q20])
#question21
q21=st.radio("21.I prefer learning from...",["Books/images", "Lectures/podcasts", "Workshops"],index=None)
if q21=="Books/images":
    v+=1
elif q21=="Lectures/podcasts":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q21"):
    explain={
        "Books/images": "You learn best using books, images, and visual materials.",
        "Lectures/podcasts": "You learn best by listening to lectures and podcasts.",
        "Workshops": "You learn best in workshops with hands-on practice."
    }
    st.success("your option is:")
    st.write("👉",q21)
    st.info("explanation:")
    st.write(explain[q21])
#question22
q22=st.radio("22.When I meet someone, I notice first...",["Dress/face", "Voice", "Body language"],index=None)
if q22=="Dress/face":
    v+=1
elif q22=="Voice":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q22"):
    explain={
        "Dress/face": "You notice a person's face and dress style first.",
        "Voice": "You notice a person's voice and speaking style first.",
        "Body language": "You notice a person's gestures and body language first."
    }
    st.success("your option is:")
    st.write("👉",q22)
    st.info("explanation:")
    st.write(explain[q22])
#question23
q23=st.radio("23.When I plan my day, I like...",["Checklist", "Discuss", "Start doing"],index=None)
if q23=="Checklist":
    v+=1
elif q23=="Discuss":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q23"):
    explain={
        "Checklist": "You plan your day using lists, schedules, and written notes.",
        "Discuss": "You plan your day by discussing and talking about it.",
        "Start doing": "You plan your day by starting work directly and learning as you go."
    }
    st.success("your option is:")
    st.write("👉",q23)
    st.info("explanation:")
    st.write(explain[q23])
#question24
q24=st.radio("24.I understand new topics better with...",["Graphs/images", "Discussion", "Practice"],index=None)
if q24=="Graphs/images":
    v+=1
elif q24=="Discussion":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q24"):
    explain={
        "Graphs/images": "You understand topics better when you see graphs and images.",
        "Discussion": "You understand topics better through discussion and explanation.",
        "Practice": "You understand topics better by practicing and doing examples."
    }
    st.success("your option is:")
    st.write("👉",q24)
    st.info("explanation:")
    st.write(explain[q24])
#question25
q25=st.radio("25.When I remember my past, it is mostly...",["Scenes", "Sounds", "Feelings/actions"],index=None)
if q25=="Scenes":
    v+=1
elif q25=="Sounds":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q25"):
    explain={
        "Scenes": "You remember the past as visual scenes like pictures.",
        "Sounds": "You remember the past through sounds and voices.",
        "Feelings/actions": "You remember the past through feelings and actions you did."
    }
    st.success("your option is:")
    st.write("👉",q25)
    st.info("explanation:")
    st.write(explain[q25])
#question26
q26=st.radio("26.While learning, I prefer to sit...",["Observe quietly", "Ask questions", "Move/do"],index=None)
if q26=="Observe quietly":
    v+=1
elif q26=="Ask questions":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q26"):
    explain={
        "Observe quietly": "You prefer sitting calmly and observing while learning.",
        "Ask questions": "You prefer learning by listening and asking questions.",
        "Move/do": "You prefer learning by moving around and doing tasks actively."
    }
    st.success("your option is:")
    st.write("👉",q26)
    st.info("explanation:")
    st.write(explain[q26])
#question27
q27=st.radio("27.To understand a concept, I...",["See diagrams", "Hear explanation", "Solve problems"],index=None)
if q27=="See diagrams":
    v+=1
elif q27=="Hear explanation":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q27"):
    explain={
        "See diagrams": "You understand concepts better by seeing diagrams and examples.",
        "Hear explanation": "You understand concepts better by hearing clear explanation.",
        "Solve problems": "You understand concepts better by solving and practicing problems."
    }
    st.success("your option is:")
    st.write("👉",q27)
    st.info("explanation:")
    st.write(explain[q27])
#question28
q28=st.radio("28.In group work, I usually...",["Make notes", "Explain ideas", "Do tasks"],index=None)
if q28=="Make notes":
    v+=1
elif q28=="Explain ideas":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q28"):
    explain={
        "Make notes": "In group work, you help by organizing and making notes.",
        "Explain ideas": "In group work, you help by speaking and explaining ideas.",
        "Do tasks": "In group work, you help by doing tasks and taking action."
    }
    st.success("your option is:")
    st.write("👉",q28)
    st.info("explanation:")
    st.write(explain[q28])
#question29
q29=st.radio("29.If I go to a new place, I remember it by...",["Landmarks", "Sounds", "Route experience"],index=None)
if q29=="Landmarks":
    v+=1
elif q29=="Sounds":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q29"):
    explain={
        "Landmarks": "You remember new places by landmarks and what you saw.",
        "Sounds": "You remember new places by the sounds you heard there.",
        "Route experience": "You remember new places by walking and experiencing the route."
    }
    st.success("your option is:")
    st.write("👉",q29)
    st.info("explanation:")
    st.write(explain[q29])
#question30
q30=st.radio("30.My best learning happens when...",["See it", "Hear it", "Do it"],index=None)
if q30=="See it":
    v+=1
elif q30=="Hear it":
    s+=1
else:
    k+=1
if st.button("submit",key="submit_q30"):
    explain={
        "See it": "You learn best when you can clearly see the information.",
        "Hear it": "You learn best when you can clearly hear the information.",
        "Do it": "You learn best when you can practice it by doing."
    }
    st.success("your option is:")
    st.write("👉",q30)
    st.info("explanation:")
    st.write(explain[q30])
if st.button("final"):
    st.success(f"Visual:{v/30*100}%,Auditry:{s/30*100}%,kinethic:{k/30*100}")