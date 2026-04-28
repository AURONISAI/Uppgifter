"""Rewrite both transcripts in human English (per engelska/REGLER.md)."""
from pathlib import Path

ROOT = Path(__file__).parent
SUB = ROOT / "submit"

LONG = """# Assignment 4 - Part A: Argumentative Speech
## Topic 1: Breaking Down Cultural Stereotypes
## Chosen society: United Kingdom

Good evening, everyone. Thanks for being here.
My name's Mohammad Sami Alsharef, and tonight I want to talk about something that sounds small but really isn't: cultural stereotypes.

My main message is simple. Stereotypes aren't harmless jokes. They change how people get treated in schools, at work, and on the street. And in mixed communities like ours here in the UK, that's a real problem. The good news? We can actually do something about it.

Why does this matter for the UK? Because we live, study and work in mixed places every day. If trust breaks down, everything else gets harder - learning, hiring, even local safety.

I'll make three points tonight.
First, stereotypes cause real damage in normal places.
Second, we already know what helps - and it's practical.
Third, local people and leaders can build better habits, starting now.

So, my first point. Stereotypes hit people in ordinary moments.
In schools, kids get labelled before teachers really know them. One student is called "aggressive". Another is told "your English isn't good enough", even when the work is fine. At work, people get judged by their accent or their name before anyone looks at their skills. In public, some folks get watched more closely than others, for no real reason.

I've seen this in everyday life too. Someone tells a joke, everyone laughs, and then one person goes quiet. That quiet moment isn't nothing. It means the joke wasn't really neutral - it pushed someone outside the group.

I know some people will say, "Come on, it's just banter." But here's the thing: if the same banter keeps targeting the same group, it stops being a joke. It becomes a rule about who's respected and who isn't. That's why this matters.

My second point. We already have tools that work.
In Lesson 13, the four-step reading method (pre-read, skim, scan, deeper read) basically says: slow down before you judge a text. The same idea works with people. Stereotypes grow when we judge fast and listen slow. The Open Letter to Fellow Students from Lesson 13 is a good example - a Muslim student living between Iranian and Italian customs. Her real life doesn't fit any neat label.

In Lesson 14, the critical reading questions push us to ask things like: what does this actually say? What is it assuming? What's the evidence? Honestly, those are great questions for real life too. What did that person actually say? What am I assuming? Do I have proof, or just a feeling?

There's also UK data we can look at. The UK Government's Ethnicity facts and figures resource shows that someone's background still affects opportunities and trust in institutions today. So this isn't only about feelings - it shows up in real outcomes.

So, what can we actually do?
One thing: in schools and at work, use clear, written criteria when you make decisions. Score sheets before interviews. Rubrics before grading. It cuts down on "gut feeling" calls.

Another thing: change how we talk. Swap "people like you always..." for "help me understand what you mean." It sounds tiny, but it changes the whole conversation.

And one more: mixed-group projects, where people actually need each other to finish a task. When you have to work with someone, you stop seeing a label and start seeing a person.

My third point. Local leadership has to make this normal, not special.
It's not enough for a council, school or company to say "we support diversity." They've got to check what's really happening:
- Are complaint systems easy to use, and do people trust them?
- Are families getting information in plain language?
- Are hiring and promotion patterns actually fair?
- Are young people invited into local conversations, not just talked about?

We can also do small things in the community. Monthly dialogue evenings in libraries, youth centres or faith spaces. Simple rule: listen first, debate second. If we only meet during a crisis, stereotypes win. If we meet regularly, trust wins.

Now let me deal with the "harmless joke" argument head-on.
If the same joke keeps targeting the same group, it sends a quiet message: this side is normal, that side is the problem. Over time that hits people's confidence, their willingness to speak up, even their ambition. So no - it's not harmless. It's a small act with a long shadow.

Time to wrap up.
My point tonight was that stereotypes do real damage, but we're not powerless. We've got course material that gives us thinking tools, public data that shows the problem is real, and very practical things we can do locally.

Three things I'd ask everyone to take away:
First, in your school or workplace, push for clearer, fairer decision routines.
Second, support and join regular dialogue spaces in the community.
Third, when you hear a stereotype-based joke, say something. Calmly, but clearly.

If we want a fairer, more united UK, this isn't extra work. This is the real work.

Thanks for listening.

---

## Reference list (to submit with transcript)
1. Lesson 13 - Reading in 4 Stages on Cultural Diversity and Stereotypes. Echo 2 reference texts: Open Letter to Fellow Students; Two Kinds; Jaymee's Extended Break.
2. Lesson 14 - Critical Reading on Structural Inequalities and Their Impact. Echo 2 reference texts: To My Old Master; School Shooters Feel Invisible; The Worldwide Phenomenon of Black American Culture.
3. UK Government - Ethnicity facts and figures (https://www.ethnicity-facts-figures.service.gov.uk/) - English-language UK source on inequality and community outcomes.
"""

SHORT = """Good evening, everyone, and thanks for being here.
My name's Mohammad Sami Alsharef, and my message tonight is simple: stereotypes aren't harmless jokes. Here in the UK, they affect real people in real places, every single day.

In schools, students get labelled before teachers really know them. At work, people get judged by their accent or their name before anyone looks at their actual skills. In public, some folks just get watched more closely, for no real reason.

I know someone will say, "It's just banter." But if the same joke keeps hitting the same group, it isn't neutral anymore. It quietly tells people who belongs and who doesn't. And over time, that hurts confidence, trust and chances.

My first point: stereotypes pull people apart. People stop speaking up when they think they'll be mocked. The Open Letter to Fellow Students from Lesson 13 is a great example - a Muslim student living between Iranian and Italian customs, showing how lazy labels miss the real person.

My second point: we already know what helps. From Lesson 14, the critical reading method teaches us to ask what a text really says, what it assumes, and what proof it has. We can use that in real life too: stop, ask, and check before you judge. At school and at work, use clear criteria for decisions instead of gut feeling. Train people to ask questions, not assume things. And put people in mixed groups, because when you have to work together, you stop seeing labels.

My third point: local leaders matter. It's not enough to say "we support inclusion." They need to check the results: who actually gets heard, who gets opportunities, and whether complaint systems are trusted. The UK Government's Ethnicity facts and figures resource shows that someone's background still affects outcomes today. So this work isn't optional.

A quick word on the "harmless joke" argument. They're not harmless. They shape what we expect from people, and what we let people get away with. Repeated long enough, a stereotype turns into a wall.

So what now? Starting this month:
First, schools and workplaces should use clearer, fairer decision routines.
Second, communities should hold regular dialogue evenings.
Third, each of us should call out stereotype jokes - calmly, but clearly.

If we want a fairer, more united community, this isn't extra work. This is the work.

Thanks for listening.

References used in this speech:
1. Lesson 13 - Reading in 4 Stages on Cultural Diversity and Stereotypes (Echo 2: Open Letter to Fellow Students; Two Kinds; Jaymee's Extended Break).
2. Lesson 14 - Critical Reading on Structural Inequalities and Their Impact (Echo 2: To My Old Master; School Shooters Feel Invisible; The Worldwide Phenomenon of Black American Culture).
3. UK Government - Ethnicity facts and figures (English-language UK source on inequality and community outcomes).
"""

(SUB / "assignment4_community_voices_speech.md").write_text(LONG, encoding="utf-8")
(SUB / "assignment4_short_professional_transcript.txt").write_text(SHORT, encoding="utf-8")

# also refresh the plain transcript .txt to match the long version (without markdown headers)
plain = []
for line in LONG.splitlines():
    if line.startswith("#") or line.startswith("---"):
        continue
    plain.append(line)
plain_text = "\n".join(plain).strip() + "\n"
(SUB / "assignment4_community_voices_transcript.txt").write_text(plain_text, encoding="utf-8")

print("Rewrote 3 files in human English:")
print(" - assignment4_community_voices_speech.md")
print(" - assignment4_community_voices_transcript.txt")
print(" - assignment4_short_professional_transcript.txt")
