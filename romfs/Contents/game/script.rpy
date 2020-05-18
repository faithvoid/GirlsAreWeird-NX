# You can place the script of your game in this file.

init:
    # Declare images below this line, using the image statement.
    # eg. image eileen happy = "eileen_happy.png"
    
    image g = "images/girl_happy.png"
    image g angry = "images/girl_angry.png"
    image g sad = "images/girl_sad.png"
    image g bored = "images/girl_bored.png"
    
    image street = "images/background.png"

    # Declare characters used by this game.
   
    $ g = Character('Sakura-chan')
    $ m = Character(what_color="#bae9fb")

    $_game_menu_screen = "_quit_prompt"
    
# The game starts here.
label start:
    $ config.rollback_enabled = False
    scene street with pixellate
    show g
    m "There is this girl at my school."
    m "She's so goddamn cute."
    m "I heard from my mate that she's having boyfriend problems."
    m "What she really needs now, is a nice guy like me."
    "Hey, Sakura-chan!"
    show g bored
    g "Hey"
    m "She needs a nice guy."
    m "She is like a goddess."
    m "I think about her... every night."
    show g
    g "Do we know each other?"
    "I'm in your class!"
    show g bored
    g "Oh, right."
    g "Oh you must sit with... those... otaku guys. Uh."
    m "Bitch."
    "Yeah. Them."
    g "Sorry, school is so boring."
    g "I hate this stupid school!"
    show g
    g "Urgh, and I hate this uniform. It makes me look so fat."
    menu:
        "Yeah, lay off the doughnuts then.":
            "Yeah, you look a bit chunky in that."
            show g angry
            g "What the hell? Like you can talk."
            g "Idiot."
            g "It's 'cos of jerks like you that regular girls like me get eating disorders."
            g "Twat."
        "No, you look fine.":
            "No, you look fine!"
            show g sad
            g "Urgh but I'm sooo fat!"
            g "I gotta go on a diet, but I just like sweets too much!"
            g "I hate myself. Why does this happen to me?!?"
            
            
    show g
    g "Actually, I had a fight with my boyfriend because he said I was fat."
    show g sad
    g "He's such a... cunt."
    show g angry
    g "I hate him!"
    show g bored
    g "He's pretty thick too... Like, he comes out with the most moronic things."
    g "Makes me ashamed to be around him."
    show g
    g "He's pretty thick really."
    "Heh..."
    menu:
        "Yeah, sounds like a real idiot.":
            "Yeah, he sounds like a real idiot!"
            show g angry
            g "D-don't be mean to him!"
            g "What the hell, you don't even know him."
            g "Will you butt out?"
            g "We have enough problems without losers like you adding to them!!!"
            "Fine, whatever."
        
        "Aww, you're being unfair.":
            "Aww, don't you think you're being a little unfair to him?"
            show g sad
            g "Ah I knew you wouldn't understand."
            g "Stupid boys always stick together!"
            show g bored
            g "Guess you're just an idiot like him."
            
    show g bored
    g "Hey, do you have any cigarettes?"
    menu:
        "Yes!":
            "Y-yes."
            g "..."
            show g angry
            g "What the hell, this is made of fucking chocolate!?"
            g "Grow up a little... man, I can't believe you're the same age as me."
            
        "No.":
            "No, I don't think you should smoke."
            show g angry
            g "What are you, my mother?"
            g "Jeez..."
            
    show g bored
    g "Damn, I hate being a teenager."
    g "Stupid family, stupid school..."
    show g
    g "Wouldn't it be nice to do something fun?"
    menu:
        "Let's run away!":
            "We could run away together."
            show g bored
            g "No thanks."
            g "Besides, who has the money?"
            g "Do you ever think anything through?"
            g "...Stupid soft-headed boys."
        
        "Be more responsible.":
            "You should be more responsible."
            show g angry
            g "What?"
            g "What the hell? I have a job as well as school."
            g "So stop lecturing me!"
            g "I bet mummy and daddy buy you everything!"
            

    show g
    g "OK, I've gotta go soon... Got things to do."
    g "So what did you want?"
    m "Oh man, here we go."
    "Uhh..."
    m "Just say it, say it say it...!!!"
    "Would... you like to hang out?"
    show g bored
    g "..."
    g "I have a boyfriend."
    "But you were having trouble with him."
    g "Yeah."
    g "You're just... not my type."
    "..."
    g "I think I'm going to make up with my boyfriend now."
    m "Cow..."
    show g
    g "So, see you. It was, uh, nice chatting to you..."
    g "Uh... Akihiko was it?"
    m "That's not my name."
    "Yeah, Akihiko."
    g "So, maybe I'll see you in class!"
    m "Riiight."
    g "Bye!"
    hide g
    m "Stupid goddamn bitchy girls..."
    m "They can never appreciate a nice guy like me."
    m "Always clinging to popular neanderthal types."
    m "Oh man, if I had a girl like her..."
    m "..."
    m "...!"
    m "..."
    scene black with pixellate
