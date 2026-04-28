"""Shorten the long speech to fit a real 5-6 minute spoken delivery (~700 words)."""
from pathlib import Path

ROOT = Path(__file__).parent
SUB = ROOT / "submit"

LONG = """# Assignment 4 - Part A: Argumentative Speech
## Topic 1: Breaking Down Cultural Stereotypes
## Chosen society: United Kingdom

Good evening, everyone. Thanks for being here.
My name's Mohammad Sami Alsharef, and tonight I want to talk about something that sounds small but really isn't: cultural stereotypes.

My main message is simple. Stereotypes aren't harmless jokes. They change how people get treated in schools, at work, and in public. And in mixed communities like ours here in the UK, that matters. The good news? We can do something about it.

I'll make three points.

First, stereotypes hit people in ordinary moments.
In schools, kids get labelled before teachers really know them. One student is called "aggressive". Another is told "your English isn't good enough", even when the work is fine. At work, people get judged by their accent or their name before anyone looks at their skills. I've seen it in everyday life too. Someone tells a joke, everyone laughs, and one person goes quiet. That quiet moment isn't nothing. It means the joke wasn't neutral - it pushed someone outside the group.

I know some people will say, "Come on, it's just banter." But here's the thing: if the same banter keeps targeting the same group, it stops being a joke. It becomes a rule about who's respected and who isn't.

Second, we already have tools that work.
In Lesson 13, the four-step reading method basically says: slow down before you judge a text. The same idea works with people. Stereotypes grow when we judge fast and listen slow. The Open Letter to Fellow Students from Lesson 13 is a good example - a Muslim student living between Iranian and Italian customs. Her real life doesn't fit any neat label.

In Lesson 14, the critical reading questions push us to ask: what does this actually say? What is it assuming? What's the evidence? Honestly, those are great questions for real life too.

There's UK data too. The UK Government's Ethnicity facts and figures resource shows that someone's background still affects opportunities and trust in institutions. So this isn't only about feelings - it shows up in real outcomes.

So what can we do? In schools and at work, use clear written criteria when you make decisions. It cuts down on "gut feeling" calls. Change how we talk: swap "people like you always..." for "help me understand what you mean." And use mixed-group projects, where people actually need each other to finish a task. When you have to work with someone, you stop seeing a label and start seeing a person.

Third, local leadership has to make this normal, not special.
It's not enough for a council, school or company to say "we support diversity." They've got to check what's really happening: are complaint systems trusted, are families getting information in plain language, are hiring patterns actually fair, and are young people invited into local conversations?

We can do small things in the community too. Monthly dialogue evenings in libraries, youth centres or faith spaces. Simple rule: listen first, debate second. If we only meet during a crisis, stereotypes win. If we meet regularly, trust wins.

Now let me deal with the "harmless joke" argument head-on.
If the same joke keeps targeting the same group, it sends a quiet message: this side is normal, that side is the problem. Over time that hits people's confidence and even their ambition. So no - it's not harmless. It's a small act with a long shadow.

Time to wrap up.
Stereotypes do real damage, but we're not powerless. We've got course material that gives us thinking tools, public data that shows the problem is real, and practical things we can do locally.

Three takeaways. First, in your school or workplace, push for clearer, fairer decision routines. Second, support regular dialogue spaces in the community. Third, when you hear a stereotype-based joke, say something. Calmly, but clearly.

If we want a fairer, more united UK, this isn't extra work. This is the real work.

Thanks for listening.

---

## Reference list (to submit with transcript)
1. Lesson 13 - Reading in 4 Stages on Cultural Diversity and Stereotypes. Echo 2 reference texts: Open Letter to Fellow Students; Two Kinds; Jaymee's Extended Break.
2. Lesson 14 - Critical Reading on Structural Inequalities and Their Impact. Echo 2 reference texts: To My Old Master; School Shooters Feel Invisible; The Worldwide Phenomenon of Black American Culture.
3. UK Government - Ethnicity facts and figures (https://www.ethnicity-facts-figures.service.gov.uk/) - English-language UK source on inequality and community outcomes.
"""

(SUB / "assignment4_community_voices_speech.md").write_text(LONG, encoding="utf-8")

# also refresh the plain transcript .txt
plain = []
for line in LONG.splitlines():
    if line.startswith("#") or line.startswith("---"):
        continue
    plain.append(line)
(SUB / "assignment4_community_voices_transcript.txt").write_text(
    "\n".join(plain).strip() + "\n", encoding="utf-8"
)

# count words for spoken-time estimate
words = sum(len(l.split()) for l in LONG.splitlines() if not l.startswith(("#", "-", "1.", "2.", "3.")))
print(f"Word count of speech body: ~{words}")
print(f"Estimated spoken time at 130 wpm: ~{words/130:.1f} min")
print(f"Estimated spoken time at 150 wpm: ~{words/150:.1f} min")
