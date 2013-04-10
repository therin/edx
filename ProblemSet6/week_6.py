def selfTest():
    story = "It is hard to write correct programs during a test!"
    listOfAdjs = ["correct"]    # a small list of adjectives
    listOfNouns = ["test"]      # a small list of nouns
    listOfVerbs = ["write"]     # a small list of verbs
    form = generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)
    
    newStory = generateStoryFromFormAndWords(form, ["write","correct","test"] )
    return story == newStory