class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                # current line is complete
                extra_space = maxWidth - length

                spaces = extra_space // max(1, len(line) - 1) # avoid / 0

                remainder = extra_space % max(1, len(line) - 1) # avoid / 0

                
                # max ensures it executes at least once
                for j in range(max(1, len(line) - 1)): # - 1 so we dont add space after last word
                    line[j] += " " * spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1

                res.append("".join(line))
                line, length = [], 0

                # don't increment i here because we didnt add the word
                # to the current line
            

            line.append(words[i])
            length += len(words[i])
            i += 1
        
        # handling last line
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        res.append(last_line + " " * trail_space)
        return res