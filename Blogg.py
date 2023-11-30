import streamlit as st 
import streamlit.components.v1 as com #para man bagan nis html basta
import base64 #ano ini kaning sa bg gani basta oii HAHAH

#pangalan sa web then emjoji sa kilid
st.set_page_config(page_title="My BLOG", page_icon=":📜:")

#para nis mga watermark kemerot for example adtong made with streamlit ah bastta amo nana
st.markdown("""
<style>
.stDeployButton
{
    visibility: hidden;
}
.st-emotion-cache-unwqvn.ea3mdgi1
{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

#sa background ni sha
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
    
img = get_img_as_base64("sunset.jpg")

page_bg_image = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
}}

[data-testid="stHeader"]{{
    background-color: rgba(0, 0, 0, 0);
}}

[data-testid="stSidebarContent"] {{
    background-image: url("data:image/png;base64,{img}");
    background-postion: center;
    background-size: cover;
}}

</style>
"""

st.markdown(page_bg_image, unsafe_allow_html=True)

#author details na naa sa sidebar

st.sidebar.image("side.png")

st.sidebar.image("ok.png")

st.sidebar.image("aboutme.png")

st.image("taytol.png", use_column_width=True)

st.markdown("<p style='text-align: center; font-family: serif; font-size: 14px;'>-Joriz Brent Rule-</p>", unsafe_allow_html=True)

#eme ra sie para change color sa barline
with open('first.css') as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)
#HEADER ni sja ok.
st.markdown("""<h2 style='text-align: left; color: black; font-size: 1.3em; font-style: italic; font-family: "Times New Roman", serif;'>
            Choosing a Major and University:
            </h2>""", unsafe_allow_html=True)

#the content of the chapter-wards english
with st.container():
    left_column, right_column = st.columns((1.5,2))
    with left_column:
        st.image("me.png")
    with right_column:
        st.write("""<div style="text-align: justify; font-family: 'Times New Roman', serif; font-size: 17.1px; color: Black;">
                 I had always enjoyed tinkering with computers, computer games and technology, but it wasn't until my last year of senior high school that I firmly decided I wanted to pursue College and choose a major that is related on what I want, it includes – Computer Engineering, Computer Science, Information Technology and etc. all about computer and programmings. 
                 When it comes to tech’s I am so interested that even my inner child of mine get excite on how computer works how those programming language organize or use and what are their functionality all of those curiosity hit me. However,    
                </div>""", unsafe_allow_html=True)
st.write("""<div style="text-align: justify; font-family: 'Times New Roman', serif; font-size: 17.1px;">
         given my background in Senior High School - HUMSS academic track, I knew getting into these competitive majors could be an uphill climb.
         </div>""", unsafe_allow_html=True)

#ako journey sa campus
st.markdown("""<h2 style='text-align: center; color: black; font-size: 1.1em; font-style: italic; font-family: "Times New Roman", serif;'>
            "My Journey to Surigao del Norte State University"
            </h2>""", unsafe_allow_html=True)

with st.container():
    left_column, right_column = st.columns((1,1))
    with left_column:
        st.write("""<div style="text-align: justify; font-family: 'Times New Roman', serif; font-size: 17px;">
                I try to register in many Universities in my place that offered major programs that I would like. I also asked my mom and friends on what Program would I fit, would it be Computer Engineering, Computer Science or Information Technology. 
                 While I pass on other university, I ultimately decided on Surigao del Norte State University since the entrance exam requirements seemed more achievable. SNSU was also close to home, which meant I could save money by living with my mom those first few years.  
                Come entrance
                 </div>""", unsafe_allow_html=True)
    with right_column:
        st.write("""<div style="text-align: justify; font-family: 'Times New Roman', serif; font-size: 17px;">
                 exam day, I could hardly eat breakfast, riddled with nerves over the technical concepts I struggled to grasp. The intense on the questions on the entrance exam paper, dejectedly convinced I had failed. The week-long wait tormented me. 
                 Spotting my name on the Entrance exam & and the other one exam (which is for the engineers only, I forgot what exam is that) list sparked utter disbelief and joy. My mom, previously worried over my chances, beamed with pride in me. I was so so happy to be a official SNSUAN’s!.
            </div>""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("---")
#sa header ni
    st.markdown("""<h2 style='text-align: left; color: black; font-size: 1.2em; font-style: italic; font-family: "Times New Roman", serif;'>
            Navigating the First Semester:
            </h2>""", unsafe_allow_html=True)
    
with st.container():
    center_column, right_column = st.columns((0.8,2))
    with center_column:
        st.image("logo.png")
    with right_column:
        st.write("""<div style="text-align: justify; font-family: 'Times New Roman', serif; font-size: 17px;">
                 Stepping foot onto the SNSU campus that first day felt strange, like I had entered some secret club I didn't belong to. Other freshmen seemed to easily fall into groups, 
                 while I mainly observed from the edge exchanging quick smiles. The classes themselves posed a shock - suddenly I was immersed in Calculus 1 and Programming that often mystified me. 
                </div>""", unsafe_allow_html=True)
    
with st.container():
    left_column, right_column = st.columns((1,1))
    with right_column:
        st.image("A4.png")
    with left_column:
        st.markdown("""<div style="text-align: justify; font-family: 'Times New Roman', serif; font-size: 17px; font-style: bold-italic;">
                 Building relationships felt like a gradual warming, as some of us uncovered a shared experience of being lost and overwhelmed.
                  My new group of comrades became central to surviving that initial transition - we spent hours studying in library and lrc, 
                 complaining about coursework, and motivating each other to power through self-doubts. Having that support system and knowing 
                 others related to the struggles made everything less intimidating.  
                </div>""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("---")
#Header napud
    st.markdown("""<h2 style='text-align: left; color: black; font-size: 1.2em; font-style: italic; font-family: "Times New Roman", serif;'>
            Overcoming College Challenges:
            </h2>""", unsafe_allow_html=True)
   
with st.container():
    left_column, right_column = st.columns((1.3,1))
    with left_column:
        st.image("comlb.png")
    with right_column:
        st.write("""<div style="text-align: justify; font-family: 'Times New Roman', serif; font-size: 17.38px;">
                 Despite developing those first precious friendships, my lowest point first semester came during Introduction to Computer Programming. 
                 While I had always enjoyed working with computers, the coding syntax seemed like a foreign language.
                  I labored for hours trying to absorb the logic structures to translate ideas into commands the machine could execute.
                </div>""", unsafe_allow_html=True)

st.write("""<div style="text-align: justify; margin-bottom: 18px; font-family: 'Times New Roman', serif; font-size: 17px;">
          My confidence went down when i received my written midterm exam results - 
         a score of 29/60 was like a punch in the gut after all the diligent studying.
         </div>""", unsafe_allow_html=True)

with st.container():
    left_column, right_column = st.columns((1.5,1.35))
    with right_column:
        st.image("https://media.giphy.com/media/zOvBKUUEERdNm/giphy.gif", use_column_width=True)
    with left_column:
        st.write("""<div style="text-align: justify; font-family: 'Times New Roman', serif; font-size: 15.3px; margin-bottom: 20px">
                 But worse still came the crushing realization that I had completely bombed the first hands-on coding (C-language) examination, scoring a 0/100, 
                I shuffled back to my house room feeling so defeated that I briefly questioned if I was cut out for this program after all. My mom's reassuring words lifted my spirits...
                as did the second chance my professor granted our class to redo the examination. 
                </div>""", unsafe_allow_html=True)
        
with st.container():
    left_column ,right_column= st.columns((2,0.5))
    with left_column:
        st.image("https://media.giphy.com/media/fhAwk4DnqNgw8/giphy.gif", use_column_width=True)
    with right_column:    
        st.write("""<div style="text-align: justify; font-size: 17px; font-family: 'Times New Roman', serif;">
        The night before our code retake, Sandyr, Mike, Kenan, and I began studying for our upcoming hands-on exam. 
        On the retake day, it was so intimidating because the aura of my classmate
        </div>""", unsafe_allow_html=True)
st.write("""<div style="text-align: justify; font-size: 16.8px;font-family: 'Times New Roman', serif; font-size: 17px;">
        seemed so different, but our instructor reassured us that the retake hands-on examination was easy. The timer started, 
        and Kurt Chua completed the code within 8 minutes. It's so amazing how he completed it so quickly.
        Fast forward: My friend Sandyr is also done with his code. Here comes the thrill part: after almost 2 hours of coding, 
        I only have 3 minutes left, and I haven’t finished my code yet. My code is running perfectly, but the compiler is    
         saying there's something wrong with it so at that time I was
        </div>""", unsafe_allow_html=True)

with st.container():
    left_column ,right_column= st.columns((1,1))
    with right_column:
        st.image("https://media.giphy.com/media/LHZyixOnHwDDy/giphy.gif", use_column_width=True)
    with left_column:
        st.write("""<div style="text-align: justify; font-size: 18.2px; font-family: serif;">
        starting to panic because the compiler wouldn’t read or run my code, but thank God! I clutched the 3 minutes and finished it, and I got a perfect score. I surprised even myself by completing the entire coding examination correctly! That small win restored my determination; with my friends by my side, I knew together we could master any programming obstacles ahead.
        </div>""", unsafe_allow_html=True)
st.markdown("---")
st.markdown("---")
#last nani na header lagi ay ay
st.markdown("""<h2 style='text-align: left; color: black; font-size: 1.2em; font-style: italic; font-family: serif;'>
            Looking Ahead:
            </h2>""", unsafe_allow_html=True)

with st.container():
    right_column, left_column = st.columns((1,1))
    with right_column:
       st.write("""<div style="text-align: justify; font-size: 17px;  font-family: serif;">
        That first semester's trials so far taught me problem-solving and perseverance.
        Having made it through my freshman challenges and now reaching the midpoint of my academic journey, 
        I feel wind at my back, propelling me towards new challenges. 
        Knowing the rewarding feeling of grasphing complex code  
        </div>""", unsafe_allow_html=True) 
    with left_column:
       st.write("""<div style="text-align: justify; font-size: 17px;font-family: serif;">
        giving me confidence to continue levelling up my skills. I'm thrilled at all I still have left to discover on my journey towards becoming a computer engineer. 
        he road has had some unexpected twists and turns - but by leaning on new friends who share this dream, 
        I know the next bend holds fresh adventures! 
        </div>""", unsafe_allow_html=True) 
st.markdown("---")
st.markdown("---")

#Contact form ni kung naay gusto mo pm sa ako fb ok rasab hihi
with st.container():
    st.markdown("""<h3 style='font-family: serif;font-style: italic; '>
                📬 Connect With Me
                </h3>""", unsafe_allow_html=True)

    st.write("##")

    Contact_form = """<form action="https://formsubmit.co/jorizrule0@gmail.com" method="POST">    
    <input type="hidden" name="_captcha" value="false">
    <label for="name" style = "font-family: serif;">Full name:</label>
    <input type="text" name="name" required>
    <label for="email" style = "font-family: serif;">Your Email:</label>
    <input type="email" name="email" required>
    <label for="message" style = "font-family: serif;" >Your Message:</label>
    <textarea name="message" required></textarea>
    <button type="submit" style = "font-family: serif;" >Send</button>
    </form>"""

left_column, right_column = st.columns(2)
with left_column:
        st.markdown(Contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()

with open('contact_form.css') as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)
