class Func:

    def __init__(self):
        # Custom paragraph for words
        my_word = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
                  "Nullam sapien felis, aliquet sit amet placerat eu, scelerisque ac justo. " \
                  "In in augue nec sem ultricies venenatis. Pellentesque tortor diam, " \
                  "volutpat sit amet tellus vitae, molestie aliquet purus." \
                  " Donec consequat a ex id mattis. Phasellus et fringilla urna. " \
                  "Phasellus sed nibh vitae nunc laoreet ultricies." \
                  " Class aptent taciti sociosqu ad litora torquent per conubia nostra," \
                  " per inceptos himenaeos. Phasellus quis ex in enim faucibus lacinia a quis purus." \
                  " Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus"

        self.words = []
        a_word = ""
        # Words attending to words array
        for i in range(len(my_word)):
            if my_word[i] != " " and my_word[i] != "." and my_word[i] != ",":
                a_word += my_word[i].lower()
            elif my_word[i] == " ":
                self.words.append(a_word)
                a_word = ""
