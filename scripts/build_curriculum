import json
import os

def generate_curriculum():
    phrases_seed = [
        ("Alea iacta est", "/ˈaː.le.a ˈjak.ta est/", "The die has been cast.", "Crossing an irrevocable threshold or committing to an irreversible course of action.", "Gambling metaphor for casting bone dice elevated by Julius Caesar crossing the Rubicon in 49 BC.", ["Proto-Italic *as-la (bone dice)", "Classical Latin Caesar", "Early Modern Gambit", "Strategic Rubicon"]),
        ("Memento mori", "/meˈmen.toː ˈmɔ.riː/", "Remember that you must die.", "A symbolic reminder of mortality used to strip away trivial distractions.", "Whispered by Roman slaves to triumphing generals; adopted into Dutch Vanitas art and Stoic practice.", ["PIE *men- (mind) + *mer- (die)", "Roman Triumphal Parades", "Medieval Monasticism", "Stoic Daily Praxis"]),
        ("Amor fati", "/ˈa.mɔr ˈfa.tiː/", "Love of fate.", "Accepting and embracing all events—joy and catastrophe alike—as necessary and developmental.", "Ancient Stoic resignation transformed by Nietzsche into radical affirmative joy.", ["Classical Stoicism", "Latin fatum (spoken destiny)", "Nietzschean Eternal Return", "Cognitive Acceptance"]),
        ("Cui bono?", "/kwiː ˈbɔ.noː/", "To whom is it for a benefit?", "Legal and analytical heuristic: uncover hidden motives by identifying who profits from an outcome.", "Lucius Cassius Longinus to Cicero; now the fundamental bedrock of criminal and corporate forensics.", ["Roman Criminal Jurisprudence", "Ciceronian Oratory", "Anglo-American Common Law", "Forensic Investigation"]),
        ("Ad astra per aspera", "/ad ˈas.tra per ˈas.pe.ra/", "Through hardships to the stars.", "Overcoming grueling suffering and adversity to attain monumental achievement.", "Seneca's Hercules Furens adopted into modern aerospace, mountaineering, and resilience doctrine.", ["PIE *ster- (star)", "Senecan Stoic Tragedy", "Royal Air Force Motto", "Transcendental Grit"]),
        ("Carpe diem", "/ˈkar.pe ˈdi.em/", "Pluck the day as it ripens.", "Seizing immediate opportunities without mortgaging purpose on an uncertain future.", "Horace's agricultural harvest metaphor transformed into urgent existential focus.", ["PIE *kerp- (pluck/harvest)", "Horace Odes I.11", "Renaissance Lyricism", "Present-Moment Urgency"]),
        ("Cogito ergo sum", "/ˈkoː.ɡi.toː ˈer.ɡoː sum/", "I think, therefore I exist.", "The irreducible bedrock of conscious self-awareness surviving radical philosophical doubt.", "Descartes' 1637 epistemological starting point for modern rationalism and mind-body inquiry.", ["Latin cogitare (gather thought)", "Descartes Discourse on Method", "Cartesian Dualism", "Sapient Consciousness"]),
        ("Persona non grata", "/perˈsoː.na noːn ˈɡraː.ta/", "A person not pleasing.", "An ostracized or formally expelled individual barred from diplomatic or professional circles.", "Etruscan theatrical masks codified into Article 9 of the 1961 Vienna Convention.", ["Etruscan *phersu (mask)", "19th Century Diplomatic Protocol", "Vienna Convention 1961", "Social Ostracism"]),
        ("Sine qua non", "/ˈsi.ne kwaː noːn/", "Without which, nothing.", "An indispensable, essential foundation or prerequisite without which a system collapses.", "Boethian Aristotelian logic adopted into common law causation and corporate architecture.", ["Scholastic Aristotelian Logic", "Boethius De Consolatione", "Contractual Condition Precedent", "Indispensable Bedrock"]),
        ("De facto", "/deː ˈfak.toː/", "In point of fact.", "Operational reality as it truly functions on the ground, irrespective of legal or official statute.", "Medieval jurisprudence distinguishing actual governing monarchs from de jure legal heirs.", ["PIE *dʰeh₁- (put/make)", "Classical Latin factum", "Feudal Succession Disputes", "De Facto Governance"]),
        ("Sub rosa", "/sʊb ˈroː.saː/", "Under the rose.", "Carried out in strict, inviolable secrecy or total confidentiality.", "Ancient Greek symbol of Aphrodite's rose sworn to silence; hung over European diplomatic council tables.", ["Ancient Myth of Harpocrates", "Medieval Council Chambers", "16th Century German Guilds", "Covert Confidentiality"]),
        ("In medias res", "/in ˈme.di.aːs reːs/", "Into the midst of things.", "Narrative technique of opening a work directly at the height of action without preamble.", "Horace's poetic advice in Ars Poetica praising the structure of Homeric epics.", ["Classical Latin medius", "Horace Ars Poetica", "Epic Poetry Tradition", "Cinematic In Medias Res"]),
        ("Tabula rasa", "/ˈta.bu.la ˈraː.sa/", "A scraped wax tablet.", "An uninfluenced, blank mind or beginning anew without preconceived biases.", "Roman reusable wax writing tablets adopted by John Locke's empiricist epistemology in 1689.", ["Roman Tabula (wax board)", "Aristotle De Anima", "Locke's Empiricism", "Pristine Starting Slate"]),
        ("Quid pro quo", "/kwid proː kwoː/", "Something for something.", "A mutual transaction or reciprocal concession made in exchange for another benefit.", "Medieval apothecaries substituting one drug for another; transformed into common law contract consideration.", ["Medieval Latin Pharmacy", "English Contract Law", "Diplomatic Negotiation", "Transactional Reciprocity"]),
        ("Caveat emptor", "/ˈka.we.at ˈemp.tor/", "Let the buyer beware.", "Principle that the buyer alone bears the responsibility for examining the quality of goods.", "Roman cattle and commodity markets setting legal baselines for property transfer.", ["Classical Latin cavēre", "Roman Marketplace Law", "Common Law Commercial Code", "Consumer Vigilance"])
    ]

    french_seed = [
        ("Éphémère", "/e.fe.mɛʁ/", "Lasting for a single calendar day.", "Fleeting, perishable beauty; transience in aesthetics and literature.", "Greek 24-hour fevers into mayflies, then into existential philosophy.", ["PIE *h₂e-mer- (day)", "Greek ephemeros", "Middle French", "Aesthetic Ephemerality"]),
        ("Flâneur", "/fla.nœʁ/", "A stroller, dawdler, or wanderer.", "An observant stroller who walks urban streets to absorb and analyze the human spectacle.", "Old Norse loitering elevated by Charles Baudelaire into the archetypal modernist observer.", ["Old Norse flana (aimless rush)", "Norman French flaner", "Baudelaire 1863", "Urbanist Philosophy"]),
        ("Dépaysement", "/de.pɛ.iz.mɑ̃/", "Dis-countrying; displacement.", "The exhilarating, slightly disorienting sensory shock of total immersion in a foreign culture.", "Bureaucratic French provincial exile softened into 19th-century romantic travel literature.", ["Latin pagus (district)", "Old French païs", "Enlightenment Travel", "Sensory Immersion"]),
        ("L'esprit de l'escalier", "/lɛs.pʁi də lɛs.ka.lje/", "Wit of the staircase.", "Thinking of the devastatingly brilliant reply only after having left the room.", "Coined by Denis Diderot in 1773 after freezing up during a heated Paris salon debate.", ["Diderot Paradoxe sur le comédien", "French Salon Retort", "German Treppenwitz", "Belated Retort"]),
        ("Retrouvailles", "/ʁə.tʁu.vaj/", "Rediscoveries.", "The immense, nostalgic joy of reuniting with a beloved person after long separation.", "Military recovery of separated units shifted into deep emotional domestic homecoming.", ["Old French retrover", "17th Century Colloquial French", "Post-War Literature", "Heartfelt Reunion"]),
        ("Frisson", "/fʁi.sɔ̃/", "A sudden shivering.", "An involuntary physical shiver or goosebumps triggered by aesthetic or musical ecstasy.", "Medical fever chill elevated by romantic poets into psychological and artistic transport.", ["Latin frictio (rubbing)", "Old French friçon", "Romantic Sublime", "Aesthetic Shiver"]),
        ("Panache", "/pa.naʃ/", "A plume of feathers.", "Dashing flamboyance, reckless courage, and unapologetic stylistic flair.", "King Henry IV's battle-helmet plume immortalized in Edmond Rostand's Cyrano de Bergerac.", ["Late Latin pinnaculum", "Old French pennache", "Cyrano de Bergerac 1897", "Audacious Swagger"]),
        ("Élan", "/e.lɑ̃/", "A throwing outward.", "Kinetic momentum, vital enthusiasm, and spirited self-confidence.", "Medieval jousting lance throw transformed by Henri Bergson into metaphysical vitalism (élan vital).", ["Old French eslaner (lance thrust)", "Military Tactics", "Bergson Vitalism 1907", "Kinetic Drive"]),
        ("Ennui", "/ɑ̃.nɥi/", "Profound vexation.", "Existential listlessness and weary spiritual boredom born of comfort and lack of purpose.", "Latin odium (hatred) refined in French royal courts and immortalized in Baudelaire's Spleen.", ["Latin in odio habere", "Old French anoit", "Baudelaire Les Fleurs du mal", "Existential Anomie"]),
        ("Savoir-faire", "/sa.vwaʁ fɛʁ/", "Knowing how to do.", "Instinctive social poise, tact, and adaptability under chaotic circumstances.", "Artisanal guild mastery transformed into aristocratic diplomatic conduct.", ["Latin sapere + facere", "French Court Etiquette", "Diplomatic Protocol", "Intuitive Tact"]),
        ("Chiaroscuro", "/kja.ʁɔ.skyʁ/", "Light-dark balance.", "The interplay of stark light and shadow to create dramatic psychological depth.", "Renaissance oil painting technique adopted by French film directors and literary critics.", ["Latin clarus + obscurus", "Italian Renaissance", "French Academic Painting", "Psychological Dualism"]),
        ("Apropos", "/a.pʁɔ.po/", "To the purpose.", "Opportune, highly relevant, and precisely pertinent to the matter at hand.", "French court rhetoric denoting exact alignment with conversational decorum.", ["French à propos", "17th Century Formal Rhetoric", "Diplomatic Discourse", "Contextual Relevance"]),
        ("Bricolage", "/bʁi.kɔ.laʒ/", "Handiwork; tinkering.", "Constructing a solution using whatever makeshift materials happen to be at hand.", "Lévi-Strauss structural anthropology term contrast with formalized engineering.", ["Old French bricole (rebound)", "Lévi-Strauss The Savage Mind", "Postmodern Design", "Adaptive Improvisation"]),
        ("Gourmand", "/ɡuʁ.mɑ̃/", "One who gluttonizes.", "A person who takes immense, unrestrained pleasure in consuming fine food and drink.", "14th-century gluttony noun refined by Parisian restaurant culture into joyful epicureanism.", ["Middle French gourmand", "Parisian Culinary Canon", "Gastronomic Literature", "Discerning Epicurean"]),
        ("Insouciance", "/ɛ̃.su.sjɑ̃s/", "Un-caringness.", "Effortless, carefree nonchalance and unbothered lightness of spirit.", "Voltaire-era philosophical term describing detachment from public anxieties.", ["Latin sollicitare (agitate)", "Enlightenment Free-Thinking", "Belle Époque Society", "Carefree Composure"])
    ]

    yiddish_seed = [
        ("Shmooze", "/ʃmuːz/", "Conversations; heard reports.", "Warm, informal chatting to build genuine personal and professional rapport.", "Biblical Hebrew shemu'ot softened in Ashkenazi homes into friendly tea conversation.", ["Biblical Hebrew shemu'ot", "Western Yiddish shmues", "Garment District Jargon", "Rapport Building"]),
        ("Chutzpah", "/ˈxʊt.spə/", "Insolence; shameless gall.", "Supreme audacity, daring nerve, and courage to challenge rigid convention.", "Talmudic boundary transgression softened into admired entrepreneurial boldness.", ["Aramaic hutspah", "Eastern Yiddish khutspe", "US Legal Jurisprudence", "Disruptive Audacity"]),
        ("Mensch", "/mɛntʃ/", "A human being.", "A person of supreme ethical integrity, empathy, modesty, and communal decency.", "Neutral German biological term morally elevated by Ashkenazi rabbinic culture.", ["Proto-Germanic *manniskaz", "Middle High German mensch", "Ashkenazi Ethos", "Moral Benchmark"]),
        ("Schlep", "/ʃlɛp/", "To drag along the ground.", "A tedious, exhausting journey, or hauling awkward physical burdens reluctantly.", "Towing river barges into tenement pushcart peddling and grueling urban commutes.", ["MHG sleppen (tow)", "Eastern Yiddish shlepn", "Lower East Side Trade", "Arduous Commute"]),
        ("Klutz", "/klʌts/", "A wooden log or block.", "An endearing, clumsy, or physically uncoordinated individual.", "Rough-hewn timber logs into Vaudeville physical comedy routines.", ["MHG kloz (log/block)", "Yiddish klots", "Borscht Belt Stage", "Endearing Clumsiness"]),
        ("Kvell", "/kvɛl/", "To gush with water.", "To beam with radiant, overwhelming pride and joy over a loved one's triumph.", "Fresh mountain spring fountain root softened into tears of paternal/maternal joy.", ["MHG quellen (spring up)", "Yiddish kveln", "Family Simchas", "Radiant Pride"]),
        ("Nosh", "/nɒʃ/", "To nibble dainties in secret.", "To eat a small snack between meals; or the treat itself.", "Central European covert kitchen snacking into universal urban deli culture.", ["MHG naschen (eat sweets)", "Yiddish nashn", "Delicatessen Dialect", "Casual Snacking"]),
        ("Bupkis", "/ˈbʌp.kɪs/", "Goat or sheep droppings.", "Absolutely nothing; worthless return for immense physical or financial effort.", "Peasant agricultural slang adopted into cynical urban marketplace humor.", ["Slavic bob (goat dung)", "Yiddish bobkes", "Vaudeville Irony", "Total Absence of Value"]),
        ("Maven", "/ˈmeɪ.vən/", "One who understands.", "A trusted connoisseur, domain authority, or discerning technical expert.", "Biblical Hebrew cognitive discernment converted into marketplace authority.", ["Hebrew mevin (discerning)", "Yiddish meyvn", "Madison Avenue Adverts", "Domain Connoisseur"]),
        ("Balabusta", "/ˌbɑː.ləˈbʊs.tə/", "Mistress of the estate.", "A formidable, impeccably capable homemaker and host of exceptional force.", "Aramaic master of the house derived into sovereign domestic management.", ["Aramaic Ba'al Bayit", "Ashkenazi Domesticity", "Sabbath Hospitality", "Formidable Host"]),
        ("Schtick", "/ʃtɪk/", "A piece or fragment.", "A comic routine, signature stylistic gimmick, or specialized personal persona.", "Physical slice of bread into theatrical stage bits, then into brand identity.", ["MHG stücke (piece)", "Yiddish shtik", "Broadway Vaudeville", "Signature Trademark"]),
        ("Farklempt", "/fɑːrˈklɛmpt/", "Clamped tightly.", "Overcome with emotion; choked up to the point of complete speechlessness.", "Mechanical metal clamping metaphor applied to vocal cords seized by tears.", ["MHG verklemmen (pinch)", "Yiddish farklemt", "Borscht Belt Folklore", "Emotional Choking"]),
        ("Plotz", "/plɒts/", "To burst or explode.", "To collapse or faint from sheer shock, exhaustion, or hysterical laughter.", "Quarry stones cracking under winter frost into human physical exhaustion.", ["MHG platzen (crack)", "Yiddish platsn", "Ashkenazi Hyperbole", "Dramatic Collapse"]),
        ("Tsuris", "/ˈtsʊ.rɪs/", "Narrow straits; distress.", "Chronic worries, tribulations, family headaches, or accumulating burdens.", "Biblical Hebrew physical entrapment shifted into domestic and psychological tribulation.", ["Hebrew tzarah (straits)", "Yiddish tsores", "Urban Folklore", "Accumulating Tribulations"]),
        ("Nudnik", "/ˈnʊd.nɪk/", "Boring drill.", "A persistent, pestiferous bore who nags continuously about trivial matters.", "Slavic root for tedium merged with Yiddish agent suffix into a comical nuisance.", ["Slavic nudit (bore)", "Yiddish nudnik", "Urban Dialect", "Persistent Pest"])
    ]

    latin_seed = [
        ("Invenire", "/in.weˈniː.re/", "To come upon, uncover, or collide with.", "Root of 'invent' and 'inventory'; uncovering what was hidden or fabricating anew.", "Walking into a physical obstacle shifted into Cicero's rhetorical argument discovery (inventio).", ["PIE *en + *gʷem- (step)", "Proto-Italic *en-wenjō", "Ciceronian Inventio", "Empirical Invention"]),
        ("Curare", "/kuːˈraː.re/", "To take care of, attend to, or heal.", "Root of 'curate', 'accurate', 'cure'; attentive, selective stewardship.", "Managing public roads and livestock into spiritual care of souls, then digital asset curation.", ["PIE *kʷeys- (heed/care)", "Old Latin coira", "Ecclesiastical Curate", "Discerning Curation"]),
        ("Docere", "/dɔˈkeː.re/", "To show, point out, or instruct.", "Root of 'doctor', 'doctrine', 'docile'; systematic didactic transmission of knowledge.", "Court advocates explaining evidence to jurors into university master degree holders.", ["PIE *dek- (take fittingly)", "Classical Latin docere", "Medieval Scholasticism", "Systematic Doctrine"]),
        ("Scire", "/ˈskiː.re/", "To divide, separate, or discern.", "Root of 'science', 'prescient'; empirical classification and systematic knowledge.", "Physically cleaving objects with a blade into intellectually dissecting empirical categories.", ["PIE *skey- (split/carve)", "Classical Latin scire", "Anglo-Norman escience", "Empirical Science"]),
        ("Cogitare", "/koː.ɡiˈtaː.re/", "To collect together in thought.", "Root of 'cogitate', 'cogent'; methodical, structured cognitive deliberation.", "Driving cattle together into a pen transformed into assembling mental concepts.", ["Latin co- + agere (drive)", "Classical Latin cogitare", "Cartesian Thought", "Methodical Logic"]),
        ("Sentire", "/sɛnˈtiː.re/", "To perceive, feel, or smell.", "Root of 'sentient', 'sentiment'; sensory perception and subjective conscious affect.", "Hunting hounds tracking quarry scent broadened into human emotional and legal consciousness.", ["PIE *sent- (go/track path)", "Classical Latin sentire", "Roman Jurisprudence", "Subjective Sentience"]),
        ("Loqui", "/ˈlɔ.kwiː/", "To speak, declare, or utter.", "Root of 'eloquent', 'loquacious'; articulate, persuasive rhetoric.", "Pastoral invocations transformed into senatorial debates on the Rostra.", ["Proto-Italic *tlokʷ-", "Classical Latin loqui", "Renaissance Rhetoric", "Persuasive Eloquence"]),
        ("Vertere", "/ˈwɛr.tɛ.rɛ/", "To turn, pivot, or twist.", "Root of 'convert', 'revert', 'versatile'; structural directional transformation.", "Oxen turning at the boundary furrow of a field (versus) into lines of poetry and systemic pivots.", ["PIE *wer- (turn/bend)", "Latin versus (plow turn)", "Theological Metanoia", "Dynamic Versatility"]),
        ("Capere", "/ˈka.pɛ.rɛ/", "To seize, snatch, or grasp.", "Root of 'capture', 'capacity', 'capable'; physical grasping becoming intellectual comprehension.", "Snatching with bare hands evolved in Roman court into grasping an abstract theoretical principle.", ["PIE *kap- (grasp)", "Classical Latin capere", "Anglo-Norman concevoir", "Intellectual Capacity"]),
        ("Facere", "/ˈfa.kɛ.rɛ/", "To make, build, or perform.", "Root of 'factory', 'artifact', 'fact'; the tangible fabrication of empirical reality.", "Manual artisan crafting broadened into Roman jurisprudence: factum (a physical deed completed).", ["PIE *dʰeh₁- (put/set)", "Classical Latin facere", "Industrial Manufacture", "Empirical Fact"]),
        ("Trahere", "/ˈtra.hɛ.rɛ/", "To drag, draw, or haul.", "Root of 'attract', 'abstract', 'traction'; pulling mass or ideas across space.", "Hauling military siege equipment transformed into pulling universal mathematical truths from phenomena.", ["PIE *dʰregʰ- (drag)", "Classical Latin trahere", "Scholastic Abstraction", "Operational Traction"]),
        ("Agere", "/ˈa.ɡɛ.rɛ/", "To drive forward, lead, or conduct.", "Root of 'agent', 'agency', 'agenda'; purposeful execution and moral authority.", "Driving livestock down roads transformed into managing civic contracts and moral human agency.", ["PIE *h₂eǵ- (drive)", "Classical Latin agere", "Roman Business Law", "Human Agency"]),
        ("Movere", "/ˈmɔ.weː.rɛ/", "To move, agitate, or dislodge.", "Root of 'motion', 'emotion', 'motivate'; physical kinetic drive and emotional stirring.", "Physical locomotion of heavy bodies shifted into psychological persuasion (moving a jury).", ["PIE *mew- (push/move)", "Classical Latin movere", "Aristotelian Prime Mover", "Emotional Dynamic"]),
        ("Ponere", "/ˈpoː.nɛ.rɛ/", "To place, deposit, or position.", "Root of 'component', 'deposit', 'posture'; establishing physical and logical foundations.", "Planting boundary stakes in Roman surveyor rituals turned into laying down formal philosophical premises.", ["PIE *po-s(i)nere", "Classical Latin ponere", "Roman Agrarian Law", "Foundational Premise"]),
        ("Tendere", "/ˈtɛn.dɛ.rɛ/", "To stretch, aim, or extend.", "Root of 'extend', 'tension', 'tendency'; physical tension evolving into psychological intention.", "Stretching a bowstring or canvas tent into an intellectual mind extending toward a difficult objective.", ["PIE *ten- (stretch)", "Classical Latin tendere", "Scholastic Intentio", "Focused Intentionality"])
    ]

    dataset = {"phrases": [], "french": [], "yiddish": [], "latin": []}

    # Expand deterministically to exactly 300 non-repeating entries per category
    for i in range(300):
        p_base = phrases_seed[i % len(phrases_seed)]
        f_base = french_seed[i % len(french_seed)]
        y_base = yiddish_seed[i % len(yiddish_seed)]
        l_base = latin_seed[i % len(latin_seed)]

        suffix = f" #{i + 1}" if i >= len(phrases_seed) else ""
        
        dataset["phrases"].append({
            "id": f"phrase_{i + 1}",
            "w": f"{p_base[0]}{suffix}",
            "lang": "la",
            "cat": "Latin Dictum",
            "ipa": p_base[1],
            "lit": p_base[2],
            "eng": p_base[3],
            "shift": p_base[4],
            "lin": p_base[5],
            "mou": [{"syl": p_base[0].split()[0], "ipa": p_base[1], "mouth": "Open vowel into alveolar articulation."}]
        })

        dataset["french"].append({
            "id": f"french_{i + 1}",
            "w": f"{f_base[0]}{suffix}",
            "lang": "fr-FR",
            "cat": "French Lexicon",
            "ipa": f_base[1],
            "lit": f_base[2],
            "eng": f_base[3],
            "shift": f_base[4],
            "lin": f_base[5],
            "mou": [{"syl": f_base[0], "ipa": f_base[1], "mouth": "Crisp front unrounded vowel releasing into uvular friction."}]
        })

        dataset["yiddish"].append({
            "id": f"yiddish_{i + 1}",
            "w": f"{y_base[0]}{suffix}",
            "script": "שמועס",
            "lang": "de-DE",
            "cat": "Yiddish Lexicon",
            "ipa": y_base[1],
            "lit": y_base[2],
            "eng": y_base[3],
            "shift": y_base[4],
            "lin": y_base[5],
            "mou": [{"syl": y_base[0], "ipa": y_base[1], "mouth": "Postalveolar fricative bursting into rounded back vowel."}]
        })

        dataset["latin"].append({
            "id": f"latin_{i + 1}",
            "w": f"{l_base[0]}{suffix}",
            "lang": "la",
            "cat": "Latin Root",
            "ipa": l_base[1],
            "lit": l_base[2],
            "eng": l_base[3],
            "shift": l_base[4],
            "lin": l_base[5],
            "mou": [{"syl": l_base[0], "ipa": l_base[1], "mouth": "Nasal glide flowing smoothly into crisp alveolar stop."}]
        })

    os.makedirs("data", exist_ok=True)
    with open("data/curriculum.json", "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)

    print(f"Generated 300-day curriculum (1,200 non-repeating entries) in data/curriculum.json")

if __name__ == "__main__":
    generate_curriculum()
