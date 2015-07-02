#Write a program that looks for a file called sample.txt. contain the text of a book
# It reads this file and then returns the top 20 words used in the text
#and the number of times they are used.
# word_frequency()takes a string
#and returns a dictionary of all the words used in the string
#and the number of times they were used.
import re

def word_frequency(raw_string):
    """Given a string returns dictionary of word/frequency in string"""
    word_string = (re.sub(r'[^A-Za-z0-9]+', ' ', raw_string)).lower()
    print(word_string)
    word_list = word_string.split(" ")
    dict_of_all_words = {}

    for word in word_list:
        if word not in dict_of_all_words:
            dict_of_all_words[word] = 1
        else:
            dict_of_all_words[word] += 1
    #TODO replace below block with for loop of the chunk of banned words
    #if key in dict_of_all_words then delete it out of the dict
    #banned = []

    if '' in dict_of_all_words:
        del dict_of_all_words['']

    return sorted(dict_of_all_words.items(), key=lambda x :x[1], reverse=True)

def read_file(text_file):
    #"""Given a .txt, opens file, stringifies and closes file"""
    #text_to_open = open(text_file)
    #print(str(text_to_open.readlines()))
    #print("TEXT IS OPEN")
    #raw_string = (text_to_open.read())
    #raw_string = str(text_to_open.read())
    #print(text_to_open.read())
    #raw_string = repr(text_to_open.read())
    #text_to_open.close()
    #return raw_string
    with text_file as textfile:
        print(textfile.read())


#def flatten_nested_list(nested_list):
#        count = 0
#        while count < len(lst):
#            while True:
#                try:
#                    lst[count : count+1] = lst[count]
#                except (TypeError, IndexError):
#                    break
#            count += 1
#        #return flattened_list

if __name__ == "__main__":

    #read_file("jane_eyre.txt")
    #print(type(raw_string))
    input_text = """Project Gutenberg's The Hound of the Baskervilles, by A. Conan Doyle

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org


Title: The Hound of the Baskervilles

Author: A. Conan Doyle

Posting Date: December 8, 2008 [EBook #2852]
Release Date: October, 2001

Language: English


*** START OF THIS PROJECT GUTENBERG EBOOK THE HOUND OF THE BASKERVILLES ***




Produced by Shreevatsa R





THE HOUND OF THE BASKERVILLES

By A. Conan Doyle




Chapter 1. Mr. Sherlock Holmes



Mr. Sherlock Holmes, who was usually very late in the mornings, save
upon those not infrequent occasions when he was up all night, was seated
at the breakfast table. I stood upon the hearth-rug and picked up the
stick which our visitor had left behind him the night before. It was a
fine, thick piece of wood, bulbous-headed, of the sort which is known as
a "Penang lawyer." Just under the head was a broad silver band nearly
an inch across. "To James Mortimer, M.R.C.S., from his friends of the
C.C.H.," was engraved upon it, with the date "1884." It was just such a
stick as the old-fashioned family practitioner used to carry--dignified,
solid, and reassuring.

"Well, Watson, what do you make of it?"

Holmes was sitting with his back to me, and I had given him no sign of
my occupation.

"How did you know what I was doing? I believe you have eyes in the back
of your head."

"I have, at least, a well-polished, silver-plated coffee-pot in front of
me," said he. "But, tell me, Watson, what do you make of our visitor's
stick? Since we have been so unfortunate as to miss him and have no
notion of his errand, this accidental souvenir becomes of importance.
Let me hear you reconstruct the man by an examination of it."

"I think," said I, following as far as I could the methods of my
companion, "that Dr. Mortimer is a successful, elderly medical man,
well-esteemed since those who know him give him this mark of their
appreciation."

"Good!" said Holmes. "Excellent!"

"I think also that the probability is in favour of his being a country
practitioner who does a great deal of his visiting on foot."

"Why so?"

"Because this stick, though originally a very handsome one has been so
knocked about that I can hardly imagine a town practitioner carrying it.
The thick-iron ferrule is worn down, so it is evident that he has done a
great amount of walking with it."

"Perfectly sound!" said Holmes.

"And then again, there is the 'friends of the C.C.H.' I should guess
that to be the Something Hunt, the local hunt to whose members he has
possibly given some surgical assistance, and which has made him a small
presentation in return."

"Really, Watson, you excel yourself," said Holmes, pushing back his
chair and lighting a cigarette. "I am bound to say that in all the
accounts which you have been so good as to give of my own small
achievements you have habitually underrated your own abilities. It may
be that you are not yourself luminous, but you are a conductor of
light. Some people without possessing genius have a remarkable power of
stimulating it. I confess, my dear fellow, that I am very much in your
debt."

He had never said as much before, and I must admit that his words gave
me keen pleasure, for I had often been piqued by his indifference to my
admiration and to the attempts which I had made to give publicity to
his methods. I was proud, too, to think that I had so far mastered his
system as to apply it in a way which earned his approval. He now took
the stick from my hands and examined it for a few minutes with his naked
eyes. Then with an expression of interest he laid down his cigarette,
and carrying the cane to the window, he looked over it again with a
convex lens.

"Interesting, though elementary," said he as he returned to his
favourite corner of the settee. "There are certainly one or two
indications upon the stick. It gives us the basis for several
deductions."

"Has anything escaped me?" I asked with some self-importance. "I trust
that there is nothing of consequence which I have overlooked?"

"I am afraid, my dear Watson, that most of your conclusions were
erroneous. When I said that you stimulated me I meant, to be frank, that
in noting your fallacies I was occasionally guided towards the truth.
Not that you are entirely wrong in this instance. The man is certainly a
country practitioner. And he walks a good deal."

"Then I was right."

"To that extent."

"But that was all."

"No, no, my dear Watson, not all--by no means all. I would suggest, for
example, that a presentation to a doctor is more likely to come from a
hospital than from a hunt, and that when the initials 'C.C.' are placed
before that hospital the words 'Charing Cross' very naturally suggest
themselves."

"You may be right."

"The probability lies in that direction. And if we take this as a
working hypothesis we have a fresh basis from which to start our
construction of this unknown visitor."

"Well, then, supposing that 'C.C.H.' does stand for 'Charing Cross
Hospital,' what further inferences may we draw?"

"Do none suggest themselves? You know my methods. Apply them!"

"I can only think of the obvious conclusion that the man has practised
in town before going to the country."

"I think that we might venture a little farther than this. Look at it
in this light. On what occasion would it be most probable that such a
presentation would be made? When would his friends unite to give him
a pledge of their good will? Obviously at the moment when Dr. Mortimer
withdrew from the service of the hospital in order to start a practice
for himself. We know there has been a presentation. We believe there has
been a change from a town hospital to a country practice. Is it, then,
stretching our inference too far to say that the presentation was on the
occasion of the change?"

"It certainly seems probable."

"Now, you will observe that he could not have been on the staff of the
hospital, since only a man well-established in a London practice could
hold such a position, and such a one would not drift into the country.
What was he, then? If he was in the hospital and yet not on the staff he
could only have been a house-surgeon or a house-physician--little more
than a senior student. And he left five years ago--the date is on the
stick. So your grave, middle-aged family practitioner vanishes into
thin air, my dear Watson, and there emerges a young fellow under thirty,
amiable, unambitious, absent-minded, and the possessor of a favourite
dog, which I should describe roughly as being larger than a terrier and
smaller than a mastiff."

I laughed incredulously as Sherlock Holmes leaned back in his settee and
blew little wavering rings of smoke up to the ceiling.

"As to the latter part, I have no means of checking you," said I, "but
at least it is not difficult to find out a few particulars about the
man's age and professional career." From my small medical shelf I took
down the Medical Directory and turned up the name. There were several
Mortimers, but only one who could be our visitor. I read his record
aloud.

        "Mortimer, James, M.R.C.S., 1882, Grimpen, Dartmoor, Devon.
        House-surgeon, from 1882 to 1884, at Charing Cross Hospital.
        Winner of the Jackson prize for Comparative Pathology,
        with essay entitled 'Is Disease a Reversion?'  Corresponding
        member of the Swedish Pathological Society.  Author of
        'Some Freaks of Atavism' (Lancet 1882).  'Do We Progress?'
        (Journal of Psychology, March, 1883).  Medical Officer
        for the parishes of Grimpen, Thorsley, and High Barrow."

"No mention of that local hunt, Watson," said Holmes with a mischievous
smile, "but a country doctor, as you very astutely observed. I think
that I am fairly justified in my inferences. As to the adjectives, I
said, if I remember right, amiable, unambitious, and absent-minded.
It is my experience that it is only an amiable man in this world who
receives testimonials, only an unambitious one who abandons a London
career for the country, and only an absent-minded one who leaves his
stick and not his visiting-card after waiting an hour in your room."

"And the dog?"

"Has been in the habit of carrying this stick behind his master. Being a
heavy stick the dog has held it tightly by the middle, and the marks of
his teeth are very plainly visible. The dog's jaw, as shown in the space
between these marks, is too broad in my opinion for a terrier and not
broad enough for a mastiff. It may have been--yes, by Jove, it is a
curly-haired spaniel."

He had risen and paced the room as he spoke. Now he halted in the recess
of the window. There was such a ring of conviction in his voice that I
glanced up in surprise.

"My dear fellow, how can you possibly be so sure of that?"

"For the very simple reason that I see the dog himself on our very
door-step, and there is the ring of its owner. Don't move, I beg you,
Watson. He is a professional brother of yours, and your presence may be
of assistance to me. Now is the dramatic moment of fate, Watson, when
you hear a step upon the stair which is walking into your life, and you
know not whether for good or ill. What does Dr. James Mortimer, the man
of science, ask of Sherlock Holmes, the specialist in crime? Come in!"

The appearance of our visitor was a surprise to me, since I had expected
a typical country practitioner. He was a very tall, thin man, with a
long nose like a beak, which jutted out between two keen, gray eyes,
set closely together and sparkling brightly from behind a pair of
gold-rimmed glasses. He was clad in a professional but rather slovenly
fashion, for his frock-coat was dingy and his trousers frayed. Though
young, his long back was already bowed, and he walked with a forward
thrust of his head and a general air of peering benevolence. As he
entered his eyes fell upon the stick in Holmes's hand, and he ran
towards it with an exclamation of joy. "I am so very glad," said he.
"I was not sure whether I had left it here or in the Shipping Office. I
would not lose that stick for the world."

"A presentation, I see," said Holmes.

"Yes, sir."

"From Charing Cross Hospital?"

"From one or two friends there on the occasion of my marriage."

"Dear, dear, that's bad!" said Holmes, shaking his head.

Dr. Mortimer blinked through his glasses in mild astonishment. "Why was
it bad?"

"Only that you have disarranged our little deductions. Your marriage,
you say?"

"Yes, sir. I married, and so left the hospital, and with it all hopes of
a consulting practice. It was necessary to make a home of my own."

"Come, come, we are not so far wrong, after all," said Holmes. "And now,
Dr. James Mortimer--"

"Mister, sir, Mister--a humble M.R.C.S."

"And a man of precise mind, evidently."

"A dabbler in science, Mr. Holmes, a picker up of shells on the shores
of the great unknown ocean. I presume that it is Mr. Sherlock Holmes
whom I am addressing and not--"

"No, this is my friend Dr. Watson."

"Glad to meet you, sir. I have heard your name mentioned in connection
with that of your friend. You interest me very much, Mr. Holmes. I
had hardly expected so dolichocephalic a skull or such well-marked
supra-orbital development. Would you have any objection to my running my
finger along your parietal fissure? A cast of your skull, sir, until
the original is available, would be an ornament to any anthropological
museum. It is not my intention to be fulsome, but I confess that I covet
your skull."

Sherlock Holmes waved our strange visitor into a chair. "You are an
enthusiast in your line of thought, I perceive, sir, as I am in
mine," said he. "I observe from your forefinger that you make your own
cigarettes. Have no hesitation in lighting one."

The man drew out paper and tobacco and twirled the one up in the other
with surprising dexterity. He had long, quivering fingers as agile and
restless as the antennae of an insect.

Holmes was silent, but his little darting glances showed me the interest
which he took in our curious companion. "I presume, sir," said he at
last, "that it was not merely for the purpose of examining my skull that
you have done me the honour to call here last night and again today?"

"No, sir, no; though I am happy to have had the opportunity of doing
that as well. I came to you, Mr. Holmes, because I recognized that I am
myself an unpractical man and because I am suddenly confronted with a
most serious and extraordinary problem. Recognizing, as I do, that you
are the second highest expert in Europe--"

"Indeed, sir! May I inquire who has the honour to be the first?" asked
Holmes with some asperity.

"To the man of precisely scientific mind the work of Monsieur Bertillon
must always appeal strongly."

"Then had you not better consult him?"

"I said, sir, to the precisely scientific mind. But as a practical man
of affairs it is acknowledged that you stand alone. I trust, sir, that I
have not inadvertently--"

"Just a little," said Holmes. "I think, Dr. Mortimer, you would do
wisely if without more ado you would kindly tell me plainly what the
exact nature of the problem is in which you demand my assistance."




Chapter 2. The Curse of the Baskervilles



"I have in my pocket a manuscript," said Dr. James Mortimer.

"I observed it as you entered the room," said Holmes.

"It is an old manuscript."

"Early eighteenth century, unless it is a forgery."

"How can you say that, sir?"

"You have presented an inch or two of it to my examination all the time
that you have been talking. It would be a poor expert who could not give
the date of a document within a decade or so. You may possibly have read
my little monograph upon the subject. I put that at 1730."

"The exact date is 1742." Dr. Mortimer drew it from his breast-pocket.
"This family paper was committed to my care by Sir Charles Baskerville,
whose sudden and tragic death some three months ago created so much
excitement in Devonshire. I may say that I was his personal friend as
well as his medical attendant. He was a strong-minded man, sir, shrewd,
practical, and as unimaginative as I am myself. Yet he took this
document very seriously, and his mind was prepared for just such an end
as did eventually overtake him."

Holmes stretched out his hand for the manuscript and flattened it upon
his knee. "You will observe, Watson, the alternative use of the long s
and the short. It is one of several indications which enabled me to fix
the date."

I looked over his shoulder at the yellow paper and the faded script. At
the head was written: "Baskerville Hall," and below in large, scrawling
figures: "1742."

"It appears to be a statement of some sort."

"Yes, it is a statement of a certain legend which runs in the
Baskerville family."

"But I understand that it is something more modern and practical upon
which you wish to consult me?"

"Most modern. A most practical, pressing matter, which must be decided
within twenty-four hours. But the manuscript is short and is intimately
connected with the affair. With your permission I will read it to you."

Holmes leaned back in his chair, placed his finger-tips together, and
closed his eyes, with an air of resignation. Dr. Mortimer turned the
manuscript to the light and read in a high, cracking voice the following
curious, old-world narrative:

        "Of the origin of the Hound of the Baskervilles there
        have been many statements, yet as I come in a direct
        line from Hugo Baskerville, and as I had the story from
        my father, who also had it from his, I have set it down
        with all belief that it occurred even as is here set
        forth.  And I would have you believe, my sons, that the
        same Justice which punishes sin may also most graciously
        forgive it, and that no ban is so heavy but that by prayer
        and repentance it may be removed.  Learn then from this
        story not to fear the fruits of the past, but rather to
        be circumspect in the future, that those foul passions
        whereby our family has suffered so grievously may not
        again be loosed to our undoing.

        "Know then that in the time of the Great Rebellion (the
        history of which by the learned Lord Clarendon I most
        earnestly commend to your attention) this Manor of
        Baskerville was held by Hugo of that name, nor can it be
        gainsaid that he was a most wild, profane, and godless
        man.  This, in truth, his neighbours might have pardoned,
        seeing that saints have never flourished in those parts,
        but there was in him a certain wanton and cruel humour
        which made his name a by-word through the West.  It
        chanced that this Hugo came to love (if, indeed, so dark
        a passion may be known under so bright a name) the daughter
        of a yeoman who held lands near the Baskerville estate.
        But the young maiden, being discreet and of good repute,
        would ever avoid him, for she feared his evil name.  So
        it came to pass that one Michaelmas this Hugo, with five
        or six of his idle and wicked companions, stole down upon
        the farm and carried off the maiden, her father and
        brothers being from home, as he well knew.  When they had
        brought her to the Hall the maiden was placed in an upper
        chamber, while Hugo and his friends sat down to a long
        carouse, as was their nightly custom.  Now, the poor lass
        upstairs was like to have her wits turned at the singing
        and shouting and terrible oaths which came up to her from
        below, for they say that the words used by Hugo Baskerville,
        when he was in wine, were such as might blast the man who
        said them.  At last in the stress of her fear she did that
        which might have daunted the bravest or most active man,
        for by the aid of the growth of ivy which covered (and
        still covers) the south wall she came down from under the
        eaves, and so homeward across the moor, there being three
        leagues betwixt the Hall and her father's farm.

        "It chanced that some little time later Hugo left his
        guests to carry food and drink--with other worse things,
        perchance--to his captive, and so found the cage empty
        and the bird escaped.  Then, as it would seem, he became
        as one that hath a devil, for, rushing down the stairs
        into the dining-hall, he sprang upon the great table,
        flagons and trenchers flying before him, and he cried
        aloud before all the company that he would that very
        night render his body and soul to the Powers of Evil if
        he might but overtake the wench.  And while the revellers
        stood aghast at the fury of the man, one more wicked or,
        it may be, more drunken than the rest, cried out that
        they should put the hounds upon her.  Whereat Hugo ran
        from the house, crying to his grooms that they should
        saddle his mare and unkennel the pack, and giving the
        hounds a kerchief of the maid's, he swung them to the
        line, and so off full cry in the moonlight over the moor.

        "Now, for some space the revellers stood agape, unable
        to understand all that had been done in such haste.  But
        anon their bemused wits awoke to the nature of the deed
        which was like to be done upon the moorlands.  Everything
        was now in an uproar, some calling for their pistols,
        some for their horses, and some for another flask of
        wine.  But at length some sense came back to their crazed
        minds, and the whole of them, thirteen in number, took
        horse and started in pursuit.  The moon shone clear above
        them, and they rode swiftly abreast, taking that course
        which the maid must needs have taken if she were to reach
        her own home.

        "They had gone a mile or two when they passed one of the
        night shepherds upon the moorlands, and they cried to
        him to know if he had seen the hunt.  And the man, as
        the story goes, was so crazed with fear that he could
        scarce speak, but at last he said that he had indeed seen
        the unhappy maiden, with the hounds upon her track.  'But
        I have seen more than that,' said he, 'for Hugo Baskerville
        passed me upon his black mare, and there ran mute behind
        him such a hound of hell as God forbid should ever be at
        my heels.'  So the drunken squires cursed the shepherd
        and rode onward.  But soon their skins turned cold, for
        there came a galloping across the moor, and the black
        mare, dabbled with white froth, went past with trailing
        bridle and empty saddle.  Then the revellers rode close
        together, for a great fear was on them, but they still
        followed over the moor, though each, had he been alone,
        would have been right glad to have turned his horse's
        head.  Riding slowly in this fashion they came at last
        upon the hounds.  These, though known for their valour
        and their breed, were whimpering in a cluster at the
        head of a deep dip or goyal, as we call it, upon the
        moor, some slinking away and some, with starting hackles
        and staring eyes, gazing down the narrow valley before them.

        "The company had come to a halt, more sober men, as you
        may guess, than when they started.  The most of them
        would by no means advance, but three of them, the boldest,
        or it may be the most drunken, rode forward down the goyal.
        Now, it opened into a broad space in which stood two of
        those great stones, still to be seen there, which were
        set by certain forgotten peoples in the days of old.
        The moon was shining bright upon the clearing, and there
        in the centre lay the unhappy maid where she had fallen,
        dead of fear and of fatigue.  But it was not the sight
        of her body, nor yet was it that of the body of Hugo
        Baskerville lying near her, which raised the hair upon
        the heads of these three dare-devil roysterers, but it
        was that, standing over Hugo, and plucking at his throat,
        there stood a foul thing, a great, black beast, shaped
        like a hound, yet larger than any hound that ever mortal
        eye has rested upon.  And even as they looked the thing
        tore the throat out of Hugo Baskerville, on which, as it
        turned its blazing eyes and dripping jaws upon them, the
        three shrieked with fear and rode for dear life, still
        screaming, across the moor.  One, it is said, died that
        very night of what he had seen, and the other twain were
        but broken men for the rest of their days.

        "Such is the tale, my sons, of the coming of the hound
        which is said to have plagued the family so sorely ever
        since.  If I have set it down it is because that which
        is clearly known hath less terror than that which is but
        hinted at and guessed.  Nor can it be denied that many
        of the family have been unhappy in their deaths, which
        have been sudden, bloody, and mysterious.  Yet may we
        shelter ourselves in the infinite goodness of Providence,
        which would not forever punish the innocent beyond that
        third or fourth generation which is threatened in Holy
        Writ.  To that Providence, my sons, I hereby commend
        you, and I counsel you by way of caution to forbear from
        crossing the moor in those dark hours when the powers of
        evil are exalted.

        "[This from Hugo Baskerville to his sons Rodger and John,
        with instructions that they say nothing thereof to their
        sister Elizabeth.]"

When Dr. Mortimer had finished reading this singular narrative he pushed
his spectacles up on his forehead and stared across at Mr. Sherlock
Holmes. The latter yawned and tossed the end of his cigarette into the
fire.

"Well?" said he.

"Do you not find it interesting?"

"To a collector of fairy tales."

Dr. Mortimer drew a folded newspaper out of his pocket.

"Now, Mr. Holmes, we will give you something a little more recent. This
is the Devon County Chronicle of May 14th of this year. It is a short
account of the facts elicited at the death of Sir Charles Baskerville
which occurred a few days before that date."

My friend leaned a little forward and his expression became intent. Our
visitor readjusted his glasses and began:

        "The recent sudden death of Sir Charles Baskerville, whose
        name has been mentioned as the probable Liberal candidate
        for Mid-Devon at the next election, has cast a gloom over
        the county.  Though Sir Charles had resided at Baskerville
        Hall for a comparatively short period his amiability of
        character and extreme generosity had won the affection
        and respect of all who had been brought into contact with
        him.  In these days of nouveaux riches it is refreshing
        to find a case where the scion of an old county family
        which has fallen upon evil days is able to make his own
        fortune and to bring it back with him to restore the
        fallen grandeur of his line.  Sir Charles, as is well known,
        made large sums of money in South African speculation.
        More wise than those who go on until the wheel turns
        against them, he realized his gains and returned to England
        with them.  It is only two years since he took up his
        residence at Baskerville Hall, and it is common talk how
        large were those schemes of reconstruction and improvement
        which have been interrupted by his death.  Being himself
        childless, it was his openly expressed desire that the
        whole countryside should, within his own lifetime, profit
        by his good fortune, and many will have personal reasons
        for bewailing his untimely end.  His generous donations
        to local and county charities have been frequently
        chronicled in these columns.

        "The circumstances connected with the death of Sir Charles
        cannot be said to have been entirely cleared up by the
        inquest, but at least enough has been done to dispose of
        those rumours to which local superstition has given rise.
        There is no reason whatever to suspect foul play, or to
        imagine that death could be from any but natural causes.
        Sir Charles was a widower, and a man who may be said to
        have been in some ways of an eccentric habit of mind.
        In spite of his considerable wealth he was simple in his
        personal tastes, and his indoor servants at Baskerville
        Hall consisted of a married couple named Barrymore, the
        husband acting as butler and the wife as housekeeper.
        Their evidence, corroborated by that of several friends,
        tends to show that Sir Charles's health has for some time
        been impaired, and points especially to some affection
        of the heart, manifesting itself in changes of colour,
        breathlessness, and acute attacks of nervous depression.
        Dr. James Mortimer, the friend and medical attendant of
        the deceased, has given evidence to the same effect.

        "The facts of the case are simple.  Sir Charles Baskerville
        was in the habit every night before going to bed of walking
        down the famous yew alley of Baskerville Hall.  The evidence
        of the Barrymores shows that this had been his custom.
        On the fourth of May Sir Charles had declared his intention
        of starting next day for London, and had ordered Barrymore
        to prepare his luggage.  That night he went out as usual
        for his nocturnal walk, in the course of which he was in
        the habit of smoking a cigar.  He never returned.  At
        twelve o'clock Barrymore, finding the hall door still open,
        became alarmed, and, lighting a lantern, went in search
        of his master.  The day had been wet, and Sir Charles's
        footmarks were easily traced down the alley.  Halfway down
        this walk there is a gate which leads out on to the moor.
        There were indications that Sir Charles had stood for some
        little time here.  He then proceeded down the alley, and
        it was at the far end of it that his body was discovered.
        One fact which has not been explained is the statement
        of Barrymore that his master's footprints altered their
        character from the time that he passed the moor-gate, and
        that he appeared from thence onward to have been walking
        upon his toes.  One Murphy, a gipsy horse-dealer, was on
        the moor at no great distance at the time, but he appears
        by his own confession to have been the worse for drink.
        He declares that he heard cries but is unable to state
        from what direction they came.  No signs of violence were
        to be discovered upon Sir Charles's person, and though
        the doctor's evidence pointed to an almost incredible
        facial distortion--so great that Dr. Mortimer refused at
        first to believe that it was indeed his friend and patient
        who lay before him--it was explained that that is a symptom
        which is not unusual in cases of dyspnoea and death from
        cardiac exhaustion.  This explanation was borne out by
        the post-mortem examination, which showed long-standing
        organic disease, and the coroner's jury returned a
        verdict in accordance with the medical evidence.  It is
        well that this is so, for it is obviously of the utmost
        importance that Sir Charles's heir should settle at the
        Hall and continue the good work which has been so sadly
        interrupted.  Had the prosaic finding of the coroner not
        finally put an end to the romantic stories which have been
        whispered in connection with the affair, it might have been
        difficult to find a tenant for Baskerville Hall.  It is
        understood that the next of kin is Mr. Henry Baskerville,
        if he be still alive, the son of Sir Charles Baskerville's
        younger brother.  The young man when last heard of was
        in America, and inquiries are being instituted with a
        view to informing him of his good fortune."

Dr. Mortimer refolded his paper and replaced it in his pocket. "Those
are the public facts, Mr. Holmes, in connection with the death of Sir
Charles Baskerville."

"I must thank you," said Sherlock Holmes, "for calling my attention to a
case which certainly presents some features of interest. I had observed
some newspaper comment at the time, but I was exceedingly preoccupied
by that little affair of the Vatican cameos, and in my anxiety to oblige
the Pope I lost touch with several interesting English cases. This
article, you say, contains all the public facts?"

"It does."

"Then let me have the private ones." He leaned back, put his finger-tips
together, and assumed his most impassive and judicial expression.

"In doing so," said Dr. Mortimer, who had begun to show signs of some
strong emotion, "I am telling that which I have not confided to anyone.
My motive for withholding it from the coroner's inquiry is that a man of
science shrinks from placing himself in the public position of seeming
to indorse a popular superstition. I had the further motive that
Baskerville Hall, as the paper says, would certainly remain untenanted
if anything were done to increase its already rather grim reputation.
For both these reasons I thought that I was justified in telling rather
less than I knew, since no practical good could result from it, but with
you there is no reason why I should not be perfectly frank.

"The moor is very sparsely inhabited, and those who live near each other
are thrown very much together. For this reason I saw a good deal of
Sir Charles Baskerville. With the exception of Mr. Frankland, of Lafter
Hall, and Mr. Stapleton, the naturalist, there are no other men of
education within many miles. Sir Charles was a retiring man, but the
chance of his illness brought us together, and a community of interests
in science kept us so. He had brought back much scientific information
from South Africa, and many a charming evening we have spent together
discussing the comparative anatomy of the Bushman and the Hottentot.

"Within the last few months it became increasingly plain to me that
Sir Charles's nervous system was strained to the breaking point. He had
taken this legend which I have read you exceedingly to heart--so much
so that, although he would walk in his own grounds, nothing would induce
him to go out upon the moor at night. Incredible as it may appear to
you, Mr. Holmes, he was honestly convinced that a dreadful fate overhung
his family, and certainly the records which he was able to give of
his ancestors were not encouraging. The idea of some ghastly presence
constantly haunted him, and on more than one occasion he has asked me
whether I had on my medical journeys at night ever seen any strange
creature or heard the baying of a hound. The latter question he put
to me several times, and always with a voice which vibrated with
excitement.

"I can well remember driving up to his house in the evening some three
weeks before the fatal event. He chanced to be at his hall door. I had
descended from my gig and was standing in front of him, when I saw
his eyes fix themselves over my shoulder and stare past me with an
expression of the most dreadful horror. I whisked round and had just
time to catch a glimpse of something which I took to be a large black
calf passing at the head of the drive. So excited and alarmed was he
that I was compelled to go down to the spot where the animal had been
and look around for it. It was gone, however, and the incident appeared
to make the worst impression upon his mind. I stayed with him all the
evening, and it was on that occasion, to explain the emotion which he
had shown, that he confided to my keeping that narrative which I read to
you when first I came. I mention this small episode because it assumes
some importance in view of the tragedy which followed, but I was
convinced at the time that the matter was entirely trivial and that his
excitement had no justification.

"It was at my advice that Sir Charles was about to go to London. His
heart was, I knew, affected, and the constant anxiety in which he lived,
however chimerical the cause of it might be, was evidently having a
serious effect upon his health. I thought that a few months among the
distractions of town would send him back a new man. Mr. Stapleton, a
mutual friend who was much concerned at his state of health, was of the
same opinion. At the last instant came this terrible catastrophe.

"On the night of Sir Charles's death Barrymore the butler, who made
the discovery, sent Perkins the groom on horseback to me, and as I was
sitting up late I was able to reach Baskerville Hall within an hour of
the event. I checked and corroborated all the facts which were mentioned
at the inquest. I followed the footsteps down the yew alley, I saw the
spot at the moor-gate where he seemed to have waited, I remarked the
change in the shape of the prints after that point, I noted that there
were no other footsteps save those of Barrymore on the soft gravel, and
finally I carefully examined the body, which had not been touched until
my arrival. Sir Charles lay on his face, his arms out, his fingers dug
into the ground, and his features convulsed with some strong emotion to
such an extent that I could hardly have sworn to his identity. There was
certainly no physical injury of any kind. But one false statement was
made by Barrymore at the inquest. He said that there were no traces
upon the ground round the body. He did not observe any. But I did--some
little distance off, but fresh and clear."

"Footprints?"

"Footprints."

"A man's or a woman's?"

Dr. Mortimer looked strangely at us for an instant, and his voice sank
almost to a whisper as he answered.

"Mr. Holmes, they were the footprints of a gigantic hound!"




Chapter 3. The Problem



I confess at these words a shudder passed through me. There was a thrill
in the doctor's voice which showed that he was himself deeply moved by
that which he told us. Holmes leaned forward in his excitement and his
eyes had the hard, dry glitter which shot from them when he was keenly
interested.

"You saw this?"

"As clearly as I see you."

"And you said nothing?"

"What was the use?"

"How was it that no one else saw it?"

"The marks were some twenty yards from the body and no one gave them
a thought. I don't suppose I should have done so had I not known this
legend."

"There are many sheep-dogs on the moor?"

"No doubt, but this was no sheep-dog."

"You say it was large?"

"Enormous."

"But it had not approached the body?"

"No."

"What sort of night was it?'

"Damp and raw."

"But not actually raining?"

"No."

"What is the alley like?"

"There are two lines of old yew hedge, twelve feet high and
impenetrable. The walk in the centre is about eight feet across."

"Is there anything between the hedges and the walk?"

"Yes, there is a strip of grass about six feet broad on either side."

"I understand that the yew hedge is penetrated at one point by a gate?"

"Yes, the wicket-gate which leads on to the moor."

"Is there any other opening?"

"None."

"So that to reach the yew alley one either has to come down it from the
house or else to enter it by the moor-gate?"

"There is an exit through a summer-house at the far end."

"Had Sir Charles reached this?"

"No; he lay about fifty yards from it."

"Now, tell me, Dr. Mortimer--and this is important--the marks which you
saw were on the path and not on the grass?"

"No marks could show on the grass."

"Were they on the same side of the path as the moor-gate?"

"Yes; they were on the edge of the path on the same side as the
moor-gate."

"You interest me exceedingly. Another point. Was the wicket-gate
closed?"

"Closed and padlocked."

"How high was it?"

"About four feet high."

"Then anyone could have got over it?"

"Yes."

"And what marks did you see by the wicket-gate?"

"None in particular."

"Good heaven! Did no one examine?"

"Yes, I examined, myself."

"And found nothing?"

"It was all very confused. Sir Charles had evidently stood there for
five or ten minutes."

"How do you know that?"

"Because the ash had twice dropped from his cigar."

"Excellent! This is a colleague, Watson, after our own heart. But the
marks?"

"He had left his own marks all over that small patch of gravel. I could
discern no others."

Sherlock Holmes struck his hand against his knee with an impatient
gesture.

"If I had only been there!" he cried. "It is evidently a case of
extraordinary interest, and one which presented immense opportunities to
the scientific expert. That gravel page upon which I might have read so
much has been long ere this smudged by the rain and defaced by the clogs
of curious peasants. Oh, Dr. Mortimer, Dr. Mortimer, to think that you
should not have called me in! You have indeed much to answer for."

"I could not call you in, Mr. Holmes, without disclosing these facts to
the world, and I have already given my reasons for not wishing to do so.
Besides, besides--"

"Why do you hesitate?"

"There is a realm in which the most acute and most experienced of
detectives is helpless."

"You mean that the thing is supernatural?"

"I did not positively say so."

"No, but you evidently think it."

"Since the tragedy, Mr. Holmes, there have come to my ears several
incidents which are hard to reconcile with the settled order of Nature."

"For example?"

"I find that before the terrible event occurred several people had seen
a creature upon the moor which corresponds with this Baskerville demon,
and which could not possibly be any animal known to science. They all
agreed that it was a huge creature, luminous, ghastly, and spectral. I
have cross-examined these men, one of them a hard-headed countryman,
one a farrier, and one a moorland farmer, who all tell the same story of
this dreadful apparition, exactly corresponding to the hell-hound of the
legend. I assure you that there is a reign of terror in the district,
and that it is a hardy man who will cross the moor at night."

"And you, a trained man of science, believe it to be supernatural?"

"I do not know what to believe."

Holmes shrugged his shoulders. "I have hitherto confined my
investigations to this world," said he. "In a modest way I have combated
evil, but to take on the Father of Evil himself would, perhaps, be too
ambitious a task. Yet you must admit that the footmark is material."

"The original hound was material enough to tug a man's throat out, and
yet he was diabolical as well."

"I see that you have quite gone over to the supernaturalists. But now,
Dr. Mortimer, tell me this. If you hold these views, why have you come
to consult me at all? You tell me in the same breath that it is useless
to investigate Sir Charles's death, and that you desire me to do it."

"I did not say that I desired you to do it."

"Then, how can I assist you?"

"By advising me as to what I should do with Sir Henry Baskerville, who
arrives at Waterloo Station"--Dr. Mortimer looked at his watch--"in
exactly one hour and a quarter."

"He being the heir?"

"Yes. On the death of Sir Charles we inquired for this young gentleman
and found that he had been farming in Canada. From the accounts which
have reached us he is an excellent fellow in every way. I speak now not
as a medical man but as a trustee and executor of Sir Charles's will."

"There is no other claimant, I presume?"

"None. The only other kinsman whom we have been able to trace was Rodger
Baskerville, the youngest of three brothers of whom poor Sir Charles was
the elder. The second brother, who died young, is the father of this lad
Henry. The third, Rodger, was the black sheep of the family. He came of
the old masterful Baskerville strain and was the very image, they tell
me, of the family picture of old Hugo. He made England too hot to hold
him, fled to Central America, and died there in 1876 of yellow fever.
Henry is the last of the Baskervilles. In one hour and five minutes
I meet him at Waterloo Station. I have had a wire that he arrived at
Southampton this morning. Now, Mr. Holmes, what would you advise me to
do with him?"

"Why should he not go to the home of his fathers?"

"It seems natural, does it not? And yet, consider that every Baskerville
who goes there meets with an evil fate. I feel sure that if Sir Charles
could have spoken with me before his death he would have warned me
against bringing this, the last of the old race, and the heir to great
wealth, to that deadly place. And yet it cannot be denied that the
prosperity of the whole poor, bleak countryside depends upon his
presence. All the good work which has been done by Sir Charles will
crash to the ground if there is no tenant of the Hall. I fear lest I
should be swayed too much by my own obvious interest in the matter, and
that is why I bring the case before you and ask for your advice."

Holmes considered for a little time.

"Put into plain words, the matter is this," said he. "In your opinion
there is a diabolical agency which makes Dartmoor an unsafe abode for a
Baskerville--that is your opinion?"

"At least I might go the length of saying that there is some evidence
that this may be so."

"Exactly. But surely, if your supernatural theory be correct, it could
work the young man evil in London as easily as in Devonshire. A devil
with merely local powers like a parish vestry would be too inconceivable
a thing."

"You put the matter more flippantly, Mr. Holmes, than you would probably
do if you were brought into personal contact with these things. Your
advice, then, as I understand it, is that the young man will be as safe
in Devonshire as in London. He comes in fifty minutes. What would you
recommend?"

"I recommend, sir, that you take a cab, call off your spaniel who is
scratching at my front door, and proceed to Waterloo to meet Sir Henry
Baskerville."

"And then?"

"And then you will say nothing to him at all until I have made up my
mind about the matter."

"How long will it take you to make up your mind?"

"Twenty-four hours. At ten o'clock tomorrow, Dr. Mortimer, I will be
much obliged to you if you will call upon me here, and it will be
of help to me in my plans for the future if you will bring Sir Henry
Baskerville with you."

"I will do so, Mr. Holmes." He scribbled the appointment on his
shirt-cuff and hurried off in his strange, peering, absent-minded
fashion. Holmes stopped him at the head of the stair.

"Only one more question, Dr. Mortimer. You say that before Sir Charles
Baskerville's death several people saw this apparition upon the moor?"

"Three people did."

"Did any see it after?"

"I have not heard of any."
"""
    print(word_frequency("There is a light's And it NEver goes out. Take me to the ball game! "))
    print(word_frequency(input_text))
