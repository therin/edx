# This is the solution for the update method only. 

def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        
        word: string
        returns: Boolean (if the word was or was not made)
        """
        # Make a copy of the hand, and try to update it
        new_hand = self.hand.copy()
        for letter in word:
            try:
                new_hand[letter] -= 1
            except KeyError:
                # if 'letter' isn't in the hand, we can't make the word from this hand.
                return False
        for letter in new_hand.keys():
            # If any of the letter counts of the new hand are less than zero after the
            # update, then we can't make the word from this hand.
            if new_hand[letter] < 0:
                return False
        # If we've gotten to here, we must be able to make the word from this hand.
        # Set self.hand to the new, updated hand and return True.
        self.hand = new_hand
        return True